# MinyQuant 작업 보드

```yaml
next_task: Q-M00
next_implementation_task: Q00
mockup_reviewed: false
active_task: null
implementation_started: false
runtime_tests_run: false
broker_connected: false
live_trading_enabled: false
paid_api_enabled: false
```

| ID | 상태 | 산출물 | 선행 조건 |
|---|---|---|---|
| [Q-M00](TASKS.md#q-m00) | TODO | 합성 데이터의 작은 클릭형 목업·사용 흐름 검토 | 사용자 목업 우선 결정 |
| [Q00](TASKS.md#q00) | TODO | 독립 패키지·개발환경·첫 로컬 시험 | Q-M00 검토 |
| [T06](TASKS.md#t06) | TODO | 국내외 데이터·연구·모의·위험·대사 | Q00; 실제 MinyAI 연결만 공통 계약 검증 필요 |
| T06-A | TODO | 수집·정제·근거/데이터 버전·입력 보안 | Q00 |
| T06-B | TODO | GPU 분석 계약·백테스트·비용 반영 비교 평가 | T06-A |
| T06-C | TODO | 승인/위험·모의 실행·실제/예상 비용 대조 | T06-B |
| T06-D | TODO | 장애·대사·안전 감독 지속 검증 | T06-C |
| [T09](TASKS.md#t09) | TODO | 실전 활성화 게이트와 제한 운영 | T06 관련 검증·실제 모의 결과·구체적 활성화 승인 |

큰 카드는 구현 시 검증 가능한 작은 변경으로 나눈다. T06은 단계별 오프라인/실제 모의 결과를 구분하며, 일부 fake 시험만으로 실제 모의까지 완료했다고 표시하지 않는다. TODO → IN_PROGRESS → DONE이며 실제 차단 범위만 BLOCKED로 기록한다.

T06은 하위 A~D의 집계 카드다. 상세 완료 기준은 [TASKS](TASKS.md#t06)를 따른다. Q00은 첫 런타임 구현 작업이며 전체 경제성 엔진을 선행 구현하지 않는다. 2026-11-12 사용자 결정으로 Q-M00 목업 검토를 앞에 추가했다. Q00→T06-A→B→C→D→T09와 실제 MinyAI 연결의 의존성은 유지한다. 목업·런타임 시험·활성화는 아직 시작하지 않았다.
