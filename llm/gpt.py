from model import GPT_NAME, GPT_MODEL

LLM_NAME = GPT_NAME
MODEL_NAME = GPT_MODEL

import os
import time
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from prompt.answer import ANSWER_PROMPT

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY가 설정되지 않았습니다.")

client = OpenAI(api_key=api_key)

def ask_gpt(question: str) -> str:

    prompt = ANSWER_PROMPT.format(question=question)
    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )

            if not response or not getattr(response, "text", None):
                return f"[{LLM_NAME}오류] 응답은 받았으나 내용이 비어 있습니다."

            return response.text.strip()

        except Exception as e:
            if attempt == max_retries:
                return f"[{LLM_NAME}오류] {e}"

            time.sleep(1.5 * attempt)