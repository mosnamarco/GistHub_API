from flask import Flask, request
from flask_cors import CORS

# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("summarization", model="facebook/bart-large-cnn")

# Load model directly
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

app = Flask(__name__)

# enabled to all routes.
# TODO: Change this to frontend only
CORS(app)

@app.route("/api/summarize", methods=['GET', 'POST'])
def hello_world():
    try:
        content = request.json

        if not content:
            return "Invalid input: No content found", 400

        if not content.get("payload"):
            return "Missing Input: No 'payload' key found.", 400

        payload = content.get("payload")

        # Tokenize input text
        inputs = tokenizer(payload, max_length=1024, return_tensors="pt", truncation=True)

        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=130, min_length=30, length_penalty=2.0, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return {"summary": summary}

    except Exception:
        print(f"Error: {Exception}")
        return "error occured while generating prediction", 400

@app.route("/<path:path>")
def catch_all(path):
    return "Page not found, sorry :(", 404
