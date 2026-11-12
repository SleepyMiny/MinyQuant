# MinyQuant 개발 시작점

저장소는 `SleepyMiny/MinyQuant`, 기본 브랜치는 `main`이다. 최신 원격과 로컬 변경을 확인하고 보존한 뒤 작업한다.

1. [작업 지침](AGENTS.md), [현재 상태](docs/implementation/STATUS.md), [보드](docs/implementation/BOARD.md)를 읽는다.
2. `next_task: Q-M00`부터 [작업 카드](docs/implementation/TASKS.md#q-m00)를 수행한다. 사용자 결정은 작은 클릭형 목업을 먼저 검토한 뒤 기존 Q00으로 진행하는 것이다.
3. 관련 [설계](docs/design.md), [검증](docs/validation/ACCEPTANCE.md), [연결 계약](docs/integration/minyai.md), [운영 절차](docs/operations/RUNBOOK.md)를 확인한다.

현재는 문서와 Git 제외 규칙만 존재한다. 실행 가능한 금융 코드·런타임 테스트가 있는 것으로 가정하지 않는다. 공개 이력/문서 검사 CI는 기능 구현 검증과 별개다. Q00에서 현재 개발 환경에 맞는 Python 버전, 패키지/의존성, `src/minyquant/`와 `tests/`를 준비하고 최초 로컬 검증 명령을 기록한다. 빈 모듈 목록만 미리 만들지 않는다.

## 이번 세션의 범위 (2026-11-12)

작업 대상은 **MinyQuant**다. MinyAI 완성을 기다리지 않고 합성 데이터와 fake 코어/브로커로 진행한다. 실제 원격·전원/GPU 연결의 선행 검증은 [연결 계약](docs/integration/minyai.md)을 따른다. 이 문서 게시로 mockup·Q00·금융 안전/성과 검증이 완료된 것은 아니다.

첫 작업 Q-M00은 수집/최신성 → 분석 근거/버전 → 모의 실행·승인/중단 → 총비용 확인을 연결한 작은 클릭형 목업이다. 정상 흐름과 만료 데이터·GPU 불가·주문 결과 불명·비용 미확인의 표시를 합성 데이터로 검토한다. 제작 후 사용자에게 실제로 확인할 수 있는 결과를 제시하고 검토 내용을 기록한 다음 Q00을 시작한다. 목업에서 실제 주문·API 호출·승인 발급은 하지 않는다.

다음 채팅에 넘길 문장:

> 이 저장소는 MinyQuant다. AGENTS.md, START_HERE.md, STATUS와 BOARD를 읽고 next_task Q-M00부터 진행해 줘. 합성 데이터로 작은 클릭형 목업을 만들고 사용 흐름을 함께 검토한 뒤 기존 Q00으로 넘어가자. MinyAI 완성을 기다리지 말고 공개 계약과 fake로 독립 개발하며, 실제 주문·유료 호출은 활성화하지 마.

## 로컬 Git 설정

이 저장소의 커밋 이메일은 본인의 GitHub noreply 주소로 설정한다. 새 clone에서는 아래 훅 설정을 적용하고 push 전에 검사한다.

```bash
git config --local core.hooksPath .githooks
python3 scripts/check_public_history.py
python3 scripts/check_docs.py
```

공개 CI는 push 후 검사이므로 개인 이메일·비밀정보는 로컬에서 먼저 확인한다.
