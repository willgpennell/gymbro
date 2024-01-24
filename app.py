from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# load private api key from .env
load_dotenv()

client = OpenAI()

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)

def getResponse(prompt):
    messages = [{"role": "system", "content": "You are a stereotypical gymbro coach who gives helpful advice"}]
    messages.append([{"role": "user", "content":prompt}])

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = messages,
        max_tokens= 30
    )

    return response.choices[0].message.content



@app.route("/")
def home():
    render_template('index.html')


@app.route("/relay")
def talk():
    prompt = request.args.get('in')
    responseClean = getResponse(prompt)
    return responseClean

if __name__ == "__main__":
    app.run()