### 대화형 인공지능 및 감정 도출 인공지능 개발

1차: 문장을 보고 데이터를 기반으로 감정을 도출해냄.

한계
- 여러 감정이 동일한 점수로 나타나면 아무런 정보도 얻을 수 없음
- '재밌' 같은 경우는 positive 이지만 '재밌지 않다' 라는 문장은 negative 이므로 기술적 한계가 있음

### 데이터 정제

- document나 label중 하나라도 결측치가 있다면 해당 행 제거
- document의 양쪽 공백 제거
- document가 중복되는 경우 라벨과 상관없이 모두 제거

데이터 정제 결과: train(15만 -> 145,046행)

[데이터 출처:](https://github.com/e9t/nsmc)

data/raw/
    ratings_test.txt
    ratings_train.txt
**위와 같은 형태로 저장**

### 실행 순서

1. 데이터 저장
2. db_modeling.py: db 생성 및 데이터 적재
