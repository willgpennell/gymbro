from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# load private api key from .env
load_dotenv()

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__, template_folder='templates', static_url_path='static')

def getResponse(prompt):
    messages = [{"role": "system", "content": "You are a stereotypical gymbro coach who gives helpful advice"}]
    messages.append([{"role": "user", "content":prompt}])



@app.route("/")
def home():
    return
if __name__ == "__main__":
    app.run()