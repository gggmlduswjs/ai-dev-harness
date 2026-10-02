# src/frontend/ — 화면 코드

화면 코드와 그 설정(빌드, 린트, 화면 테스트)을 한 폴더에 모읍니다. 백엔드와 **같은 업무 이름**의 폴더를 쓰면 서로 찾기 쉽습니다.

화면 구현 세부(부품·props)는 코드가 정본입니다. 기획 문서에 복제하지 않습니다.

## UI 스택 (Vue + Element Plus 프로젝트일 때)

> 다른 프레임워크를 쓰면 이 절만 그 스택에 맞게 바꿉니다.

| 층 | 도구 | 역할 |
|---|---|---|
| 부품 | [Element Plus](https://github.com/element-plus/element-plus) | 표·폼·모달 같은 공식 컴포넌트 (npm 의존성 — 버전은 정확히 고정) |
| 디자인 규칙 | [refactoring-ui-skill](https://github.com/s0xDk/refactoring-ui-skill) | 간격·글자·색·그림자를 정해진 단계에서만 고르게 하는 Claude 스킬 (코드가 아님) |
| 토큰 | 토큰 파일 1개 (예: `styles/tokens.css`) | 색·간격·글자 값의 정본. Element Plus의 `--el-*` 변수를 여기서 한 번만 덮어씀 |

규칙은 [`docs/UI_GUIDE.md`](../../docs/UI_GUIDE.md), 스킬 설치는 [`.claude/README.md`](../../.claude/README.md)에 있습니다.

