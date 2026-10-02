# src/backend/ — 서버 코드

업무(도메인) 하나당 폴더 하나입니다. `utils/`, `common/` 같은 잡동사니 폴더를 늘리지 않습니다.

```text
backend/
├── <domain>/        예: orders, inventory, billing
│   ├── models       데이터 구조
│   ├── services     업무 규칙·계산 (화면/API와 무관한 로직)
│   ├── api          외부 입구 (HTTP 등) — 얇게
│   ├── tasks        백그라운드 작업
│   └── tests        이 도메인의 테스트
├── core/            설정·DB·인증처럼 모든 도메인이 쓰는 기반
└── config/          환경별 설정 (base / local / production / test)
```

**어느 도메인을 열어도 같은 역할 이름이 같은 자리에 있어야 합니다.** 이름이 제각각이면 `CLAUDE.md`에 대응표를 적습니다.
