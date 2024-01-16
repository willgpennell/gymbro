from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# load private api key 
load_dotenv()
OpenAI.api_key = os.environ["API_KEY"]

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bot", methods=["POST"])
def bot():

    client = OpenAI()

    input = request.form["message"]
    history = []

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=50,
        messages=[{"role": "system","content": "You are a helpful but stereotypical gymbro coach, you give helpful workout advice"}]
    )

    result = response['choices'][0]['message']['content']
    prompt = ("\nUser:",{input},"\nChatbot: ",{result})
    history.append(prompt)


if __name__ =="__main__":
    app.run()