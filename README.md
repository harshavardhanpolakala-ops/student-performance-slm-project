# Student Guidance AI – Student Performance SLM

## 1. Project Overview

Student Guidance AI is a Small Language Model (SLM)-based application designed to provide personalized academic guidance to students using their academic performance and study-related information.

The project uses **Qwen2.5-0.5B-Instruct**, a compact language model, with a LoRA fine-tuned model converted into GGUF format for local inference through Ollama.

## 2. Project Objectives

- Provide students with academic guidance.
- Identify areas where students may need improvement.
- Generate personalized study recommendations.
- Demonstrate the application of a Small Language Model in student support.
- Run the trained model locally using Ollama.

## 3. Dataset Collection and Preparation

The project uses the Student Performance dataset available on Hugging Face.

**Dataset:** `Harsha282007/student-performance-dataset`

**Dataset link:**  
https://huggingface.co/datasets/Harsha282007/student-performance-dataset

The dataset contains information such as:
- Student demographics
- Study time
- Previous academic performance
- Absences
- Family and school-related information
- Student lifestyle and study habits

The original dataset was divided into:

| Dataset | Records |
|---|---:|
| Training | 276 |
| Validation | 59 |
| Testing | 60 |

Additional student-guidance prompt-and-answer examples were prepared for the project. The prepared guidance files contain 276 training examples and 50 validation examples.

## 4. Model Information

- **Base model:** Qwen/Qwen2.5-0.5B-Instruct
- **Fine-tuning method:** LoRA (Low-Rank Adaptation)
- **LoRA rank:** 8
- **LoRA alpha:** 16
- **LoRA dropout:** 0.05
- **Target modules:** q_proj, v_proj
- **Model format:** GGUF
- **Quantization:** Q4_K_M
- **Inference platform:** Ollama

The previously fine-tuned model was converted into GGUF format for local execution.

## 5. Repository Structure

```text
Student-Guidance-AI/
│
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
├── students_performance.parquet
├── test.parquet
├── train.parquet
└── validation.parquet
```

### File Description

- **.gitignore:** Specifies files Git should ignore.
- **README.md:** Contains project documentation and setup instructions.
- **app.py:** Main application code.
- **requirements.txt:** Contains the required Python libraries.
- **students_performance.parquet:** Student performance dataset.
- **train.parquet:** Training data.
- **validation.parquet:** Validation data.
- **test.parquet:** Testing data.

## 6. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Prepare the dataset

Download the dataset from the Hugging Face dataset repository and place the required dataset files in the project directory.

### Step 4: Run the application

```bash
python app.py
```

## 7. Model Hosting on Hugging Face

The model and prepared guidance dataset files are hosted on Hugging Face.

**Model repository:**  
https://huggingface.co/Harsha282007/student-guidance-ai

The repository includes:
- Fine-tuned model in GGUF format.
- Training guidance examples.
- Validation guidance examples.
- Model documentation.

## 8. Ollama Model Import and Chat Demo

Ollama is used to run the GGUF model locally and demonstrate its responses.

### Step 1: Install Ollama

Download and install Ollama:

https://ollama.com/

### Step 2: Download the GGUF model

Download `student_guidance_finetuned_q4_k_m.gguf` from the Hugging Face model repository.

### Step 3: Create a Modelfile

Create a file named `Modelfile` in the same folder as the GGUF model.

Add:

```text
FROM ./student_guidance_finetuned_q4_k_m.gguf
```

### Step 4: Import the model into Ollama

Open the terminal in that folder and run:

```bash
ollama create student-guidance -f Modelfile
```

### Step 5: Start the chat demo

```bash
ollama run student-guidance
```

The model is now available for local interaction through the terminal.

## 9. Training and Evaluation Information

The earlier fine-tuning run recorded the following values:

| Parameter | Recorded Value |
|---|---:|
| Training steps | 170 |
| Training epochs | Approximately 4.93 |
| Best recorded evaluation loss | Approximately 0.0937 |
| LoRA rank | 8 |
| LoRA alpha | 16 |

These values are from the earlier model training logs. The prepared guidance examples are separate project artifacts and should not be assumed to have been used to train the uploaded GGUF model.

Further evaluation using held-out student queries and appropriate performance metrics is required.

## 10. Limitations

- The model is small and may generate inaccurate or incomplete responses.
- Recommendations should be treated as academic guidance, not professional counselling.
- The model requires further testing on unseen student queries.
- Model responses depend on the quality and coverage of the training data.

## 11. Future Enhancements

- Expand the student-guidance dataset.
- Perform additional fine-tuning and evaluation.
- Improve response accuracy and consistency.
- Include additional student performance indicators.
- Develop a user-friendly interface.
- Evaluate the model using a larger set of unseen student queries.

## 12. Technologies Used

- Python
- Hugging Face
- Transformers
- PEFT / LoRA
- Pandas
- Parquet
- GGUF
- Ollama

## 13. Conclusion

Student Guidance AI demonstrates the application of a compact language model for academic guidance and student support. By using a fine-tuned model in GGUF format and deploying it through Ollama, the project provides a foundation for locally running an AI-based student guidance assistant.

The project can be further improved through expanded datasets, additional model training, and systematic evaluation.
