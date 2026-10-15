import streamlit as st
# import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon=":🎥",
    layout="centered",
)

MODEL_PATH = "Rookie1111agag/sentiment_model"
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()  # Set the model to evaluation mode
    return tokenizer, model



st.title("Sentiment Analysis App")
st.write("""
Enter a movie review below, and the app will predict whether the sentiment is positive or negative.
""")

try:
    tokenizer, model = load_model()
except Exception as error:
    st.error(f"Error loading model: {error}")
    st.exception(error)
    st.stop()

review = st.text_area("Movie Review", height=150)
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a movie review before analyzing.")
    else:
        try:
            inputs = tokenizer(review, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                probabilities = model(**inputs).logits.softmax(dim=1)[0]
                predicted_class = int(torch.argmax(probabilities).item())
                confidence = float(probabilities[predicted_class].item())

                if predicted_class == 1:
                    sentiment = "Positive"
                    st.success(f"The sentiment of the review is: {sentiment} (Confidence: {confidence:.2f})")
                else:
                    sentiment = "Negative"
                    st.error(f"The sentiment of the review is: {sentiment} (Confidence: {confidence:.2f})")
                st.metric(
                    label="Confidence Score",
                    value=f"{confidence:.2f}",
                )
                st.subheader("Probability Distribution")
                st.write(f"Positive: {probabilities[1]:.2f}")
                st.progress(float(probabilities[0].item()))  # Show progress bar for negative sentiment
                st.write(f"Negative: {probabilities[0]:.2f}")
                st.progress(float(probabilities[0].item()))  # Show progress bar for positive sentiment

                st.caption("Note: The confidence score indicates the model's certainty about its prediction. A higher score means the model is more confident in its prediction.")
        except Exception as error:
            st.error(f"Error during sentiment analysis: {error}")
            st.exception(error)
            
