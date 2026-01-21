from llm.gemini import ask_gemini
from llm.mimo import ask_openrouter
from llm.analyzer import analyze_answers

def run_pipeline(question: str) -> dict:
    gemini_answer = ask_gemini(question)
    openrouter_answer = ask_openrouter(question)

    answers = {
        "gemini": gemini_answer,
        "openrouter": openrouter_answer,
    }

    analysis = analyze_answers(question=question, answers=answers)

    return {
        "question": question,
        "answers": answers,
        "analysis": analysis,
    }