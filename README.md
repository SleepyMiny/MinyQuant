# MinyQuant

국내·해외 주식 데이터 수집, 전략 연구, 백테스트, 모의 실행, 위험 검사, 주문·대사를 독립적으로 개발하는 개인 프로젝트입니다. MinyAI는 별도로 개발하는 비공개 중심 시스템이며 MinyQuant는 버전 있는 API와 이벤트로 연결되는 부가서비스입니다.

현재 상태는 **설계·개발 인계 완료, 런타임 구현 시작 전**입니다. 실행 가능한 프로그램이나 배포 설정은 아직 없습니다.

공개 범위는 엔진·연결 계약·예제·합성 시험입니다. 실제 계좌·키·개인 전략 설정·거래 원장·재배포 권한이 없는 시장 데이터는 외부에서 관리합니다. 라이선스는 아직 선택하지 않았습니다.

## 개발 시작

[START_HERE](START_HERE.md) → [현재 상태](docs/implementation/STATUS.md) → [작업 보드](docs/implementation/BOARD.md) 순서로 읽습니다. 첫 작업은 Q00입니다. MinyAI 구현 완료나 증권사 키 없이 로컬 모델·fake 브로커부터 개발할 수 있습니다.

| 문서 | 내용 |
|---|---|
| [설계](docs/design.md) | 시장·자금·주문·위험·대사 계약 |
| [작업 카드](docs/implementation/TASKS.md) | Q00 기준선, T06 연구·모의, T09 실전 게이트 |
| [수용시험](docs/validation/ACCEPTANCE.md) | 인계한 A33~A41/A44, 모두 NOT RUN |
| [MinyAI 연결](docs/integration/minyai.md) | 공통 서비스 계약과 소유권 |
| [운영·복구](docs/operations/RUNBOOK.md) | 운영 준비·정지·대사·복원 |
| [이전 기록](docs/MIGRATION.md) | 출처 커밋과 문서 매핑 |

코드는 향후 루트 `src/minyquant/`, 시험은 `tests/`에 구성합니다. 계좌·키·개인정보·실제 시장 원천 데이터·백업은 Git에 보관하지 않습니다.
