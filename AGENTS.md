# MinyQuant 작업 지침

- 이 저장소는 개인 프로젝트 MinyQuant다. MinyAI는 비공개로 유지한다. 공개 계약과 fake adapter를 사용하며 MinyAI 내부 코드·설정·자격증명·원문을 복사하지 않는다.
- 커밋 author/committer는 GitHub noreply 주소를 쓴다. 개인 이메일을 Git 이력·문서·로그에 넣지 않는다. 로컬 `core.hooksPath=.githooks`를 설정하고 push 전 `python3 scripts/check_public_history.py`를 실행한다.
- 이 저장소는 MinyQuant다. MinyAI와 분리된 주식 서비스이며 사용자의 최신 지시가 우선한다.
- 작업 전 START_HERE.md, docs/implementation/STATUS.md, BOARD.md, TASKS.md와 실제 브랜치·HEAD·미커밋 변경을 확인한다. 사용자 변경과 다른 작업자의 원격 커밋을 보존한다.
- 코드 예정 위치는 루트 `src/minyquant/`, 시험은 루트 `tests/`다. 현재 실행 가능한 패키지는 없으며 Q00에서 환경·패키지·로컬 테스트를 준비한다.
- MinyAI 소스나 내부 DB를 직접 import/공유하지 않는다. 연결은 docs/integration/minyai.md를 따른다. MinyAI의 개발 완료와 무관하게 fake·합성 데이터로 독립 개발한다.
- 국내·해외 모델을 지원하되 첫 외부 구현은 한 broker adapter·한 시장부터 검증한다. 증권사·계좌·해외 국가 미정이 로컬 구현을 막지 않는다.
- LLM은 브로커 키·한도 변경권·승인 발급권을 갖지 않는다. 금융 승인 검증/소비·자금 예약·주문 의도는 금융 DB 내부에서 원자 처리한다. UNKNOWN은 자동 재주문하지 않고 대사한다. 사고 latch는 재부팅으로 해제하지 않는다.
- 실제 키·계좌·데이터·백업을 Git이나 테스트 로그에 넣지 않는다. 합성 fixture를 사용하고 live/유료 접근은 미설정 시 꺼 둔다. 저장소 생성·구현 요청을 실거래 활성화로 해석하지 않는다.
- MinyAI/OpsLoop/다른 저장소의 운영 서비스·계정·배포를 임의로 변경하지 않는다.
- 실제 실행한 검증만 PASS로 기록한다. 작업 후 BOARD/STATUS에 변경·검증·남은 조건·다음 한 작업을 남긴다. 상세 금융 문서의 정본은 이 저장소다.
