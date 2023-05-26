## 데이터 전처리

1. 결측치 처리
2. 이상치 처리
3. 데이터 변경(로그함수 , 지수함수, ..)
4. 스케일링(데이터 범위 맞춰서 데이터를 좀더 정확하게 맞추기 위해서) 
 - 표준화 ((표준)정규분포화 : 평균:U (0), 표준편차(1시그마 ~ 6시그마)) : StandardScaler()
 - 정규화 (데이터의 범위를 0 ~ 1 사이로 줄여주거나 늘려주는것) : MinMaxScaler(), MaxAbsScaler()
 - RobustScaler()

 -Row 단위 스케일러
 -- Normalizer(각 행의 값을 변경시켜 주는것)

 5. 피처링(Featuring)
 6. 더미 베리어블(Dummy Variable) - 코드화



 === CRISP-DM ===
 1. Business UnderStanding
 2. Data
 3. Data preparing
     - 필요한 데이터 정의
     - 수집
     - 가공
        1. 누락치(결측치)
        2. 이상치
        3. 데이터 변형
        4. 스케일링(정규화, 표준화)
        5. 피처링
        6. 코드화(get_dummies(), encode() => one-hot-encoding) 
    - 필요한 정보를 요약 => 하나의 데이터 셋
4. Modeling
    - 판다스
    - 넘파이
    - sklearn
    - Preprocessing
5. Evaluation

## 회귀 분석

1. 단항 회귀 분석 (선형 회귀) y = a * X + b
    - a(회귀 계수 / 기울기) : coef_
    - b(절편) : intercept_
