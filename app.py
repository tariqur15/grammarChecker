from flask import Flask, render_template, request
from language_tool_python import LanguageTool

app = Flask(__name__)
grammar_checker = LanguageTool('en-US')

@app.route('/')
def index():
    return render_template('index.html', input_text="")

@app.route('/correct', methods=['POST'])
def correct():
    input_text = request.form['inputText']
    file_content = request.files['fileInput'].read().decode('utf-8', errors='ignore') if 'fileInput' in request.files else None

    # Perform grammar checking on user input or file content
    corrected_text = grammar_checker.correct(input_text) if not file_content else grammar_checker.correct(file_content)
    
    # Get mistakes found
    mistakes = grammar_checker.check(input_text) if not file_content else grammar_checker.check(file_content)
    


    return render_template('index.html', corrected_text=corrected_text, mistakes=mistakes, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
