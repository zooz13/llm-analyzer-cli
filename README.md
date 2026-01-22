# llm-analyzer-cli

이 프로젝트는 **동일한 질문을 여러 LLM에게 동시에 전달하고**,  
각 모델의 응답을 수집하여 **공통점과 관점 차이를 구조적으로 분석**하는 CLI 기반 도구입니다.

단순히 LLM의 성능을 비교하는 것이 아니라,  
**모델마다 어떻게 다르게 사고하고 답변하는지**를 한눈에 파악하는 데 초점을 두고 있습니다.  
이를 통해 하나의 질문에 대해 여러 관점을 동시에 확인하고,  
보다 균형 잡힌 판단을 할 수 있도록 돕는 것을 목표로 합니다.

본 저장소는 향후 서비스 형태로 확장하기 위한 **초기 MVP(Prototype)** 입니다.

## 🚀 향후 확장 계획 및 발전 가능성

### 1. CLI → 백엔드 API 구조 확장

- 현재 CLI에서 수행 중인
  - 다중 LLM 호출
  - 응답 수집
  - 분석 결과 생성
    로직을 백엔드 API 형태로 분리
- 향후 웹/앱 서비스에서 동일한 분석 파이프라인 재사용 가능

---

### 2. 웹 기반 분석 결과 시각화

- Next.js 기반 웹 인터페이스 추가
- 단순 텍스트 출력이 아닌
  - 공통 결론 요약
  - 관점 차이 비교
  - 모델별 응답 구조화
    형태로 시각적 제공
- 사용자가 여러 모델의 답변을 직관적으로 비교 가능

---

### 3. 분석 결과 구조화 방식 확장

- 모델 선택이나 결과 최적화를 목적으로 하지 않고,
  동일한 질문에 대한 응답을
  - 공통 주장
  - 관점 차이
  - 전제 조건의 차이
  - 강조점의 차이
    등으로 분리하여 표현
- 결과를 하나로 합치는 것이 아니라, **차이를 더 명확히 드러내는 방향의 분석 방식 확장**

---

### 4. 파인튜닝 모델 도입

- 상용 LLM API 결과를 Teacher로 활용하여
  - 특정 도메인에 특화된 Student 모델 파인튜닝
- API 기반 모델과 파인튜닝 모델의
  - 응답 특성 비교
  - 분석 결과 차이 검증
- 비용 및 응답 특성 측면에서의 장단점 분석 가능

---

### 5. 사용자 피드백 기반 개선

- 사용자가 참고한 관점이나 유용하다고 판단한 결과를 기반으로
  - 분석 방식 개선
  - 결과 구조 조정
- 정확도 평가가 아닌
  **“어떤 분석이 더 설득력 있었는지”에 대한 정성적 피드백 수집**

---

### 6. 분석 보조 도구로서의 확장 가능성

- 단일 정답을 제공하는 AI가 아닌
  **판단을 돕는 분석 보조 서비스**로 활용 가능
- 리서치, 기획, 학습, 토론 보조 등 다양한 활용 가능성 존재

## ⭐️ 예시 화면

### 1) 질문 예시

![Ask Example](./assets/ask.png)

### 2) 분석 결과 예시

![Analyze Example](./assets/analyze.png)

### 3) 개별 모델 답변 예시

![Answer Example](./assets/answer1.png)  
![Answer Example](./assets/answer2.png)

## ⚙️ 설치 방법

```bash
git clone https://github.com/zooz13/llm-analyzer-cli.git
```

```bash
cd llm-analyzer-cli
python -m venv venv

source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

```
pip install -r requirements.txt
```

## 실행 방법

```bash
python main.py analyze "여기에 질문 입력"
```

## 참고

- .env 파일에 API 키 설정 필요 (예: OPENROUTER_API_KEY, GEMINI_API_KEY) `.env_example`을 참고하세요.

- 해당 프로젝트에서는 `gemini-3-flash-preview`, `mimo-v2-flash` 모델을 사용하고있습니다.
