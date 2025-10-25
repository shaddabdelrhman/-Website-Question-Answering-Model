from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

# Load the QA JSON once when app starts
with open('model.json', 'r', encoding='utf-8') as f:
    qa_data = json.load(f)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "question is required"}), 400

    # Check if the question exists in the JSON
    for category, qa_list in qa_data.get("filgoal_qa", {}).items():
        for item in qa_list:
            if item.get('question') == question:
                return jsonify({"answer": item.get('answer')})
    
    return jsonify({"answer": "no answer found"})

if __name__ == '__main__':
    app.run(debug=True)
