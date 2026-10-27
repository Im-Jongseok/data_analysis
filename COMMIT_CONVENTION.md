---
title: "데이터 분석 실습 커밋 규칙"
course: "웹기반시스템"
semester: "2026-2"
---

# Commit Convention

`flask-practice1`의 커밋 규칙과 동일하게 주차별 작업 범위와 변경 유형을 대괄호로 구분합니다.

## 기본 형식

주차별 실습과 과제는 아래 형식을 사용합니다.

```text
[작업 범위][변경 유형] 작업 내용
```

README와 커밋 규칙 등 저장소 공통 문서는 `[docs] 작업 내용` 형식을 사용합니다. 콜론은 사용하지 않고, 작업 내용은 한국어로 짧게 작성합니다.

## 작업 범위

| 범위 | 용도 |
| --- | --- |
| `week{N}-prac{N}` | 주차별 실습. 첫 번째 `N`은 주차, 두 번째 `N`은 실습 순서입니다. |
| `week{N}-hw{N}` | 주차별 과제. 첫 번째 `N`은 주차, 두 번째 `N`은 과제 순서입니다. |
| `docs` | 저장소 README와 커밋 컨벤션 등 문서 변경 |

분석 코드와 데이터, 환경 설정은 해당 실습이나 과제의 범위를 사용합니다. 실습·과제별 설명 문서는 해당 범위와 `docs` 유형을 함께 사용합니다.

## 변경 유형

| 유형 | 용도 |
| --- | --- |
| `feat` | 분석 코드, 데이터 또는 시각화 추가 |
| `chore` | 환경, 의존성, 기본 설정 변경 |
| `fix` | 분석 코드나 데이터 오류 수정 |
| `docs` | 문서 작성 및 수정 |

한 커밋에는 하나의 목적에 해당하는 변경을 담습니다. 여러 변경이 함께 포함되면 핵심 변경에 맞는 범위와 유형을 사용합니다.

## 예시

```text
[week10-prac1][feat] 매출 데이터 분석 노트북과 데이터 추가
[week10-prac1][feat] 결측치와 중복 데이터 확인 추가
[week10-prac1][fix] 매출 합계 계산 오류 수정
[week10-prac1][docs] 전처리 과정 설명 추가
[week10-prac1][chore] pandas 의존성 추가
[week10-hw1][feat] 매출 분석 과제 추가
[docs] 2026년 2학기 README와 front matter 추가
[docs] 데이터 분석 실습 커밋 규칙 정리
```

## 커밋 찾기

작업 범위나 변경 유형을 기준으로 `git log`에서 검색합니다.

```bash
git log --oneline --grep='week10-prac'
git log --oneline --grep='week10-hw'
git log --oneline --grep='\[fix\]'
git log --oneline --grep='\[docs\]'
```
