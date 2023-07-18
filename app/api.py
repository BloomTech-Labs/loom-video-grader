from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import openai
from dotenv import load_dotenv
import os

with open("README.md", "r") as file:
    next(file)
    description = file.read()

VERSION = "0.0.1"
API = FastAPI(
    title='Loom Validator API',
    description=description,
    version=VERSION,
    docs_url='/',
)
API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


@API.get("/version", tags=["General"])
async def version():
    """<h3>Version</h3>
    Returns the current version of the API
    <pre><code>
    @return: String </code></pre>"""
    return VERSION


@API.get("/validate", tags=["Loom Video Validation"])
async def validate(transcript: str):
    """<h3>validate</h3>
    Returns a boolean indicating whether the transcript is a valid Loom video submission
    <pre><code>
    @param transcript: String
    @return: String </code></pre>"""
    context = "You are a master coding instructor and you are reviewing a student's Loom video submission."
    prompt = f"Assess whether the submission was an honest attempt at solving a problem." \
             f"Use the following video transcript to make this determination: {transcript}." \
             f"Make sure the student actually tried to answer the question. Getting it correct is not required." \
             f"Ensure that the student tried to explain their thought process and did not just copy and paste code." \
             f"Make sure the student did not just submit a random video that has nothing to do with the problem." \
             f"If you think the student made an honest effort, repond `validated` otherwise respond `not valid`."
    result, *_ = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ],
    ).choices
    validate_message = result.get("message").get("content").replace("\n", "<br>")
    return {
        "response": validate_message,
    }