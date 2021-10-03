from translate import Translator
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def trans():
    if request.method == 'POST':
        translator = Translator(to_lang='ru')
        result = request.form['text_for_trans']
        result = translator.translate(result)
        return render_template("index.html", text_after_trans=result)
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/<name>')
def hello_with_name(name):
    return render_template("index.html", name=name)


if __name__ == '__main__':
    app.run()
