from flask import Flask, render_template, request
import openai
import os
import pyperclip

# setup flask
app = Flask(__name__)

# home route
@app.route("/")
def hello():
    return render_template("index.html")

# copy code route
@app.route("/copycode")
def copycode():
    pyperclip.copy(html)
    return "<h1>Code copied to clipboard</h1>"

# preview route
@app.route('/Text', methods=['POST'])
def processtext():
    global html
    text = request.form['textboxinputdata']
    openai.api_key = os.environ["OPENAI_KEY"]
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [{"role": "system", "content" : "You are FridayAI, a large language model trained by Parth Gupta. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-04-10"},
    {"role": "user", "content" : "i will be giving you a prompt on how a webpage should look like and what will its function be. you will give me the code for it but not explain how the code works. the code should contain css and javscript code too so that the page is responsive. use the <script> and <style> tags instead of creating separate files"},
    {"role": "assistant", "content" : "Sure, I will generate the code for the prompt and won't be explaining the code. Give me the prompt."},
    {"role": "user", "content" : text}]
    )
    print(completion['choices'][0]['message']['content'])
    html=completion['choices'][0]['message']['content']
    try:
        html=(html.split("```"))[1].split("```")[0]
        ehtml=html[:html.find("</body>")]+"<center><a href='/copycode'>Copy Code</a></center>"+html[html.find("</body>"):]
        return render_template("result.html", textboxdata=ehtml)
    except:
        return "<h2> FridayAI was unable to extract information regarding the same. Please retry !</h2>"


if __name__ == "__main__":
    app.run(debug=True)