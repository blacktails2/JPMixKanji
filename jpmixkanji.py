from flask import Flask, request, render_template_string, url_for, jsonify
import random
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    text = ""
    kanji_list = ""
    if request.method == 'POST':
        text = request.form['text']
        kanji_list = request.form['kanji_list'].split()
        result = replace_kanji(text, kanji_list)
    return render_template_string(html_template, text=text, kanji_list=" ".join(kanji_list), result=result)

@app.route('/get-examples', methods=['GET'])
def get_examples():
    try:
        with open('text_example.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return jsonify({"error": "Internal server error"}), 500

def replace_kanji(text, kanji_list):
    kanji_in_text = [char for char in text if char >= '\u4e00' and char <= '\u9faf']
    replaced_text = text
    random.shuffle(kanji_list)
    kanji_iterator = iter(kanji_list)

    for kanji in kanji_in_text:
        try:
            replaced_kanji = next(kanji_iterator)
        except StopIteration:
            random.shuffle(kanji_list)
            kanji_iterator = iter(kanji_list)
            replaced_kanji = next(kanji_iterator)
        replaced_text = replaced_text.replace(kanji, replaced_kanji, 1)
    return replaced_text

html_template = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>Kanji Replace Tools</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  </head>
  <body>
  <section class="section">
    <div class="container is-fluid">
      <h1>Kanji Replace Tools</h1>
      <div class="columns">
        <div class="column">
          <form method="post">
            <label for="text">Sentense</label><br />
            <textarea id="text" name="text" rows="4" cols="50">{{ text }}</textarea>
            <button class="example_button" type="button" onclick="insertExample(0)">Sample: Kokoro</button>
            <button class="example_button" type="button" onclick="insertExample(1)">Sample: Sangetsuki</button>
            <button class="example_button" type="button" onclick="insertExample(2)">Sample: Tsumi to Batsu</button>
            <button class="example_button" type="button" onclick="insertExample(3)">Sample: Mainz (Wikipedia)</button>
        </div>
        <div class="column">
          <h2>Result</h2>
          <div class='textwrap'>
            <p id="resultText">
              {{ result|replace('\n', '<br>')|safe }}
            </p>
            <button type="button" onclick="copyToClipboard()">Copy Result</button>
          </div>
          
        </div>
      </div>
      <div class="columns">
        <div class="column is-10">
            <label for="kanji_list">Kanji List</label><br />
            <textarea id="kanji_list" name="kanji_list" rows="2" cols="50">{{ kanji_list }}</textarea>
        </div>
        <div class="column">
          <input type="submit" value="Replace" />
          </form>
        </div>
      </div>
    </div>
  </section>
  <script>
      function copyToClipboard() {
        var resultText = document.getElementById("resultText");
        var textArea = document.createElement("textarea");
        textArea.value = resultText.innerText;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("copy");
        document.body.removeChild(textArea);
        alert("結果がクリップボードにコピーされました！");
      }

      function insertExample(index) {
        fetch('/get-examples')
        .then(response => response.json())
        .then(data => {
          var examples = data.examples;
          if (index < examples.length) {
            var exampleText = examples[index].replace(/\\n/g, '<br>');
            document.getElementById("text").value = examples[index]; // テキストエリアにはそのまま挿入
            document.getElementById("resultText").innerHTML = exampleText; // 表示部分には改行をHTMLで
          }
        })
        .catch(error => console.error('Error fetching examples:', error));
      }
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
