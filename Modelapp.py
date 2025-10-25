from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)
CORS(app)
api = Api(app)

# Load the AraGPT2 model
model_name = "aubmindlab/aragpt2-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_answer(prompt):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=50, pad_token_id=tokenizer.eos_token_id)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer[len(prompt):].strip()  # remove prompt from output
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "Question is required"}), 400

    answer = generate_answer(question)
    return jsonify({"answer": answer})

if __name__== '_main_':
    app.run(debug=True)