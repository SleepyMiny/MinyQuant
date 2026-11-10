# MinyQuant 개발 시작점

저장소는 `SleepyMiny/MinyQuant`, 기본 브랜치는 `main`이다. 최신 원격과 로컬 변경을 확인하고 보존한 뒤 작업한다.

1. [작업 지침](AGENTS.md), [현재 상태](docs/implementation/STATUS.md), [보드](docs/implementation/BOARD.md)를 읽는다.
2. `next_task: Q00`부터 [작업 카드](docs/implementation/TASKS.md)를 수행한다.
3. 관련 [설계](docs/design.md), [검증](docs/validation/ACCEPTANCE.md), [연결 계약](docs/integration/minyai.md), [운영 절차](docs/operations/RUNBOOK.md)를 확인한다.

현재는 문서와 Git 제외 규칙만 존재한다. 실행 가능한 금융 코드·런타임 테스트가 있는 것으로 가정하지 않는다. 공개 이력/문서 검사 CI는 기능 구현 검증과 별개다. Q00에서 현재 개발 환경에 맞는 Python 버전, 패키지/의존성, `src/minyquant/`와 `tests/`를 준비하고 최초 로컬 검증 명령을 기록한다. 빈 모듈 목록만 미리 만들지 않는다.

다음 채팅에 넘길 문장:

> SleepyMiny/MinyQuant의 START_HERE.md와 AGENTS.md를 읽고, STATUS와 BOARD의 next_task부터 구현을 이어가 줘. MinyAI와 분리된 주식 서비스로 개발하고 실제 검증 결과를 남겨 줘.

## 로컬 Git 설정

이 저장소의 커밋 이메일은 본인의 GitHub noreply 주소로 설정한다. 새 clone에서는 아래 훅 설정을 적용하고 push 전에 검사한다.

```bash
git config --local core.hooksPath .githooks
python3 scripts/check_public_history.py
python3 scripts/check_docs.py
```

공개 CI는 push 후 검사이므로 개인 이메일·비밀정보는 로컬에서 먼저 확인한다.
