Movie Review Sentiment Analyzer

A web application that uses a fine-tuned DistilBERT NLP model to classify movie reviews as positive or negative. Built with Python, PyTorch, Hugging Face Transformers, and Streamlit.

Live Demo

"Try the app here" (YOUR_LIVE_DEMO_URL)

Project Overview

This project demonstrates how to fine-tune a pretrained Transformer model for sentiment analysis and deploy it as an interactive web application.

Users can enter a movie review and receive a predicted sentiment along with the model's estimated probabilities for positive and negative sentiment.

Features

- Positive and negative movie review classification
- Fine-tuned DistilBERT model
- Interactive web application built with Streamlit
- Prediction probabilities and confidence display
- Hugging Face Hub model hosting
- Streamlit web application interface
- IMDb Dataset for movie review sentiment analysis

How It Works

1. A user enters a movie review.
2. The tokenizer converts the text into model inputs.
3. The fine-tuned DistilBERT model processes the inputs.
4. The application predicts positive or negative sentiment.
5. The result and predicted class probabilities are displayed.

Project Structure

sentiment_streamlit/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

The trained model and tokenizer are hosted separately on Hugging Face rather than stored in the GitHub repository.

Installation and Setup

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/sentiment-streamlit.git
cd sentiment-streamlit

Replace "YOUR_USERNAME" with your GitHub username and use the correct repository URL.

2. Create a Virtual Environment

python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Install Dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure the Model

In "app.py", set the model path to your public Hugging Face model repository:

MODEL_PATH = "YOUR_USERNAME/sentiment-distilbert"

Replace "YOUR_USERNAME" with your Hugging Face username.

5. Run the Application

python -m streamlit run app.py

Open the local URL displayed in your terminal, usually:

http://localhost:8501

Example Predictions

Positive Review

Input:

"The movie was fantastic, and the actors delivered excellent performances."

Expected result: Positive sentiment.

Negative Review

Input:

"The movie was boring, poorly written, and disappointing."

Expected result: Negative sentiment.

Predictions may vary depending on the review and the model's learned patterns.

Model Evaluation

The model was fine-tuned for binary sentiment classification using the IMDb movie review dataset.

Add your actual test accuracy and evaluation results here after training. Do not report an accuracy value unless it comes from your evaluation.

Limitations

- The model was trained for movie review sentiment classification and may not generalize well to other types of text.
- Sarcasm, mixed opinions, and ambiguous reviews may lead to incorrect predictions.
- Predicted probabilities are estimates, not guarantees of correctness.

Future Improvements

- Add a review history feature.
- Evaluate the model on additional datasets.
- Improve performance on sarcasm and ambiguous reviews.
- Enhance the user interface and visualization of prediction probabilities.