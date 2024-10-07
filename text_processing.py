
from transformers import pipeline

def extract_keywords(text):
    """Extracts keywords or summarizes the input text."""
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']






