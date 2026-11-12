# Gureumi Backend

로봇 상태신호를 수신하고 웹에 전달하기 위한 FastAPI 백엔드입니다.

## 프로젝트 구조

```text
gureumi_backend_new/
├── src/
│   └── app/
│       ├── __init__.py
│       └── main.py       # FastAPI 앱 생성
├── .gitignore
├── .python-version
├── pyproject.toml        # 프로젝트 정보와 의존성 설정
├── uv.lock               # 의존성 버전 잠금 파일
└── README.md
```

## 설치 및 실행

```bash
uv sync --locked
uv run uvicorn app.main:app --app-dir src --reload
```

- 서버: http://localhost:8000
- API 문서(Swagger): http://localhost:8000/docs
