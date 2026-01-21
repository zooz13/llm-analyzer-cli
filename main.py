import typer
from rich.console import Console
from rich.panel import Panel

from orchestrator import run_pipeline

app = typer.Typer()
console = Console()

@app.callback()
def main():
    pass

@app.command()
def analyze(
    text: str = typer.Argument(None, help="질문 입력"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="대화형 모드 실행"),
):
    def run_once(content: str):
        console.print(Panel(content, title="입력", style="cyan"))
        console.print("[bold yellow]분석 중...[/bold yellow]")

        result = run_pipeline(content)

        if result is None:
            console.print(
                Panel(
                    "[red]분석 결과가 없습니다 (None 반환).[/red]",
                    title="오류",
                    style="red",
                )
            )
            return

        console.print(
            Panel(
                result["question"],
                title="📌 질문",
                style="bright_blue",
            )
        )

        for model_name, answer_text in result["answers"].items():
            console.print(
                Panel(
                    answer_text,
                    title=f"🤖 답변 — {model_name}",
                    style="magenta",
                )
            )

        console.print(
            Panel(
                result["analysis"],
                title="🧠 종합 분석",
                style="green",
            )
        )

    # interactive 모드
    if interactive or text is None: 
        console.print("[bold]대화형 모드입니다. 'exit' 입력 시 종료됩니다.[/bold]")
        while True:
            user_input = console.input("\n[bold cyan]> [/bold cyan]")
            if user_input.lower() in ("exit", "quit"):
                break
            if not user_input.strip():
                continue
            run_once(user_input)
        return

    # 단발 실행 모드
    try:
        with open(text, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = text

    run_once(content)

if __name__ == "__main__":
    app()