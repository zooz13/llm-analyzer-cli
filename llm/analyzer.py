import os
from dotenv import load_dotenv
from google import genai
from prompt.analyze import ANALYZE_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY가 설정되지 않았습니다.")

client = genai.Client(api_key=API_KEY)


def analyze_answers(question: str, answers: dict[str, str]) -> str:
    formatted_answers = []
    for name, answer in answers.items():
        formatted_answers.append(f"[{name} 답변]\n{answer}")

    joined_answers = "\n\n".join(formatted_answers)

    prompt = ANALYZE_PROMPT.format(
        question=question,
        answers=joined_answers,
    )

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )

        if not response or not getattr(response, "text", None):
            return "[분석 오류] 응답은 받았으나 내용이 비어 있습니다."

        return response.text.strip()

    except Exception as e:
        return f"[분석 오류] {e}"
