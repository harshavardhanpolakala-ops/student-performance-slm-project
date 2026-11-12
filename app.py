
import streamlit as st
import pandas as pd
import joblib
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SLM_DIR = "Qwen/Qwen2.5-0.5B-Instruct"

st.set_page_config(
    page_title="AI Student Performance System",
    page_icon="🎓",
    layout="wide"
)

@st.cache_resource
def load_models():
    ml_model = joblib.load(
        os.path.join(BASE_DIR, "student_performance_model.pkl")
    )

    tokenizer = AutoTokenizer.from_pretrained(SLM_DIR)
    llm = AutoModelForCausalLM.from_pretrained(SLM_DIR)

    return ml_model, tokenizer, llm

@st.cache_data
def load_data():
    return pd.read_parquet(os.path.join(BASE_DIR, "test.parquet"))

model, tokenizer, llm = load_models()
data = load_data()

st.title("🎓 AI-Based Student Performance Prediction")
st.write("Predict academic performance and receive AI-generated study guidance.")

sample = data.drop(columns=["G3"]).iloc[0]
categorical_columns = data.select_dtypes(include=["object"]).columns.tolist()

with st.form("student_form"):
    st.subheader("Enter Student Details")
    student_input = {}

    for column in sample.index:
        if column in categorical_columns:
            options = sorted(data[column].dropna().unique().tolist())
            student_input[column] = st.selectbox(
                column.replace("_", " ").title(),
                options,
                index=options.index(sample[column])
            )
        else:
            student_input[column] = st.number_input(
                column.replace("_", " ").title(),
                min_value=int(data[column].min()),
                max_value=int(data[column].max()),
                value=int(sample[column]),
                step=1
            )

    submitted = st.form_submit_button("Predict Performance")

if submitted:
    input_df = pd.DataFrame([student_input])
    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted Final Grade: {prediction:.2f} / 20")

    if prediction < 10:
        st.warning("The student may need additional academic support.")
    else:
        st.success("The predicted grade is satisfactory.")

    st.subheader("🤖 AI Study Guidance")

    messages = [
        {
            "role": "system",
            "content": "You are a friendly academic advisor. Give practical, simple and encouraging study advice."
        },
        {
            "role": "user",
            "content": (
                f"A student's predicted final grade is {prediction:.1f} out of 20. "
                "Suggest three practical ways to improve academic performance. "
                "Use simple English."
            )
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    with st.spinner("Generating AI study recommendations..."):
        with torch.no_grad():
            outputs = llm.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=False,
                repetition_penalty=1.1,
                pad_token_id=tokenizer.eos_token_id
            )

        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        guidance = tokenizer.decode(
            new_tokens,
            skip_special_tokens=True
        )

    st.info(guidance)

st.caption("Educational prototype. Predictions are estimates, not guarantees.")
