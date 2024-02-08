import openai
from flask import Flask, render_template, request
from openai import ChatCompletion

app = Flask(__name__)

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = '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'

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        messages = [{"role": "system", "content": "Elgar Zeynalov, Xos geldin.."}, {"role": "user", "content": user_input}]
        chat = ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return render_template('chat.html', messages=messages)

    return render_template('chat.html', messages=[])

if __name__ == '__main__':
    app.run(debug=True)
