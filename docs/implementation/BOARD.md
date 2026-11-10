# MinyQuant 작업 보드

```yaml
next_task: Q00
active_task: null
implementation_started: false
runtime_tests_run: false
broker_connected: false
live_trading_enabled: false
paid_api_enabled: false
```

| ID | 상태 | 산출물 | 선행 조건 |
|---|---|---|---|
| [Q00](TASKS.md#q00) | TODO | 독립 패키지·개발환경·첫 로컬 시험 | 없음 |
| [T06](TASKS.md#t06) | TODO | 국내외 데이터·연구·모의·위험·대사 | Q00; 실제 MinyAI 연결만 공통 계약 검증 필요 |
| [T09](TASKS.md#t09) | TODO | 실전 활성화 게이트와 제한 운영 | T06 관련 검증·실제 모의 결과·구체적 활성화 승인 |

큰 카드는 구현 시 검증 가능한 작은 변경으로 나눈다. T06은 단계별 오프라인/실제 모의 결과를 구분하며, 일부 fake 시험만으로 실제 모의까지 완료했다고 표시하지 않는다. TODO → IN_PROGRESS → DONE이며 실제 차단 범위만 BLOCKED로 기록한다.
