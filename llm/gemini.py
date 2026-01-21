from model import GEMINI_NAME, GEMINI_MODEL

LLM_NAME = GEMINI_NAME
MODEL_NAME = GEMINI_MODEL

import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

from prompt.answer import ANSWER_PROMPT

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY가 설정되지 않았습니다.")

client = genai.Client(api_key=api_key)

def ask_gemini(question: str) -> str:
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