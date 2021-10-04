from translate import Translator
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def trans():
    if request.method == 'POST':
        translator_ru = Translator(to_lang='ru')
        resultRu = request.form['text_for_transToRu']
        resultRu = translator_ru.translate(resultRu)
        translator_en = Translator(to_lang='en', from_lang='ru')
        resultEn = request.form['text_for_transToEn']
        resultEn = translator_en.translate(resultEn)
        return render_template("index.html", text_after_transToEn=resultEn, text_after_transToRu=resultRu)
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/<name>')
def hello_with_name(name):
    return render_template("index.html", name=name)


if __name__ == '__main__':
    app.run()
