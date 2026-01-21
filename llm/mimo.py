from model import OPENROUTER_LLM_NAME, OPENROUTER_MODEL

LLM_NAME = OPENROUTER_LLM_NAME
MODEL_NAME = OPENROUTER_MODEL

import os
import time
import requests

from prompt.answer import ANSWER_PROMPT

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY가 설정되지 않았습니다.")

def ask_openrouter(question: str) -> str:
    prompt = ANSWER_PROMPT.format(question=question)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "너는 명확하게 답하는 AI다."},
            {"role": "user", "content": prompt},
        ],
    }

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            # OpenRouter API는 OpenAI와 동일하게 choices 구조
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            if attempt == max_retries:
                return f"[{LLM_NAME} 오류] {e}"
            time.sleep(1.5 * attempt)