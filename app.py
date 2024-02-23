from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# load private api key from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
print(client.api_key)

#OpenAI.api_key = os.environ["OPENAI_API_KEY"]
#client.api_key = os.getenv("OPENAI_API)")

app = Flask(__name__)

def getResponse(prompt):
    messages = [{"role": "system", "content": "You are a stereotypical gymbro coach who gives helpful advice"}]
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
         model = "gpt-3.5-turbo",
         messages = messages
    )

    print(response)
    return response.choices[0].message.content



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/relay")
def talk():
    prompt = request.args.get('input')
    responseClean = getResponse(prompt)


    return responseClean

if __name__ == "__main__":
    app.run()