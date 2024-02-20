import pandas as pd
from transformers import AutoTokenizer, pipeline

# Load the CSV dataset
dataset_path = r'malicious_phish.csv'
df = pd.read_csv(dataset_path)

# Assuming your CSV has a column named 'url' that contains URLs
urls = df['url'].tolist()

# Load the pre-trained model and tokenizer
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ealvaradob/bert-finetuned-phishing")
model = AutoModelForSequenceClassification.from_pretrained("ealvaradob/bert-finetuned-phishing")
# model_name = "laiyer/codebert-base-Malicious_URLs-onnx"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = ORTModelForSequenceClassification.from_pretrained(model_name)

# Create a text classification pipeline
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
)

# Function to classify a given URL
def classify_url(input_url):
    result = classifier(input_url)
    return result




# User input for URL
user_input_url = input("Enter the URL to check: ")

# Perform classification
output = classify_url(user_input_url)

# Print the classification result
print("Classification Result:")
print(f"URL: {user_input_url}")
print(f"Predicted Label: {output[0]['label']}")
print(f"Confidence Score: {output[0]['score']}")