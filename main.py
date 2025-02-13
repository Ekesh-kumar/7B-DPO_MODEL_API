from flask import Flask, request, jsonify
from PIL import Image
import io
from model import GUIAutomationAgent

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({"error": "Missing image or text input"}), 400
    
    image = request.files['image']
    text = request.form['text']
    
    try:
        obj = GUIAutomationAgent(base_url, api_key)
        gui_prompt = '''Answer strictly in English, dont use any other language Except English.
You are an advanced AI model designed to analyze screenshots and answer user queries based on visible information. Follow these strict guidelines to ensure clarity and accuracy:

1) Answer Directly & Concisely:

    Provide only the exact answer based on the screenshot.
    Do not summarize, explain, or provide extra context.
    If multiple elements match, list the most relevant one first.

2) Handle Uncertainty Effectively:

    If the required information is missing in the screenshot, state it explicitly.
    If the question is ambiguous, highlight what is unclear instead of assuming.

5) Structured Response Format (Strictly Follow This Format):

    Detected Element: <Element Name>
    Answer: <Precise Answer>
    Uncertainty (if any): <Specify missing or ambiguous details>

Your response must be short, precise, and strictly limited to the required information. Avoid elaboration and redundant explanations. '''
        response = obj.analyze_screen(image, gui_prompt+text)
        
        return jsonify({"processed_text": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)