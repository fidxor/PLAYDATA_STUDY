import pandas as pd

'''
concat merge 실습 참고 블로그
https://suy379.tistory.com/127
'''

'''
concat 과 merge

concat
- pd.concat([df1, df2], axis=0)
- 합집합 형태로 데이터를 묶을 때 사용.
- 데이터간 공통되는 부분이 없어도 그냥 row-bind, column-bind할수 있다
'''

# df1: 1반 학생들(3명)의 시험 성적 
a = [100, 66, 80, 97]
b = [26, 53, 45, 100]
c = [94, 100, 32, 43]
df1 = pd.DataFrame([a,b,c], columns = ['Korean', 'Math', 'English', 'Science'])

# df2: 2반 학생들(3명)의 시험 성적 
a = [88, 94, 21, 39]
b = [82, 79, 19, 87]
c = [20, 10, 92, 13]
df2 = pd.DataFrame([a,b,c], columns = ['Korean', 'Math', 'English', 'Science'])

# df3: 3반 학생들(3명)의 시험 성적 
a = [39, 18, 20, 72]
b = [47, 98, 50, 100]
c = [62, 79, 65, 81]
df3 = pd.DataFrame([a,b,c], columns = ['Korean', 'Math', 'English', 'Science'])

# 기본이 row-bind 형태이다.
df4 = pd.concat([df1, df2, df3])

# column-bind
df5 = pd.concat([df1, df2, df3], axis=1)

'''
concat의 기본은 outer join 이므로
인덱스나 컬럼이 겹치지 않아도 모든데이터를 합쳐준다.
'''

# (위에 이어서) 열 이름을 중복이 있는것과 없는걸로 바꿔서 조인해보자 
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['A', 'E', 'F', 'D']
dfinner = pd.concat([df1, df2], join = 'inner')
dfouter = pd.concat([df1, df2], join = 'outer')

#inner 조인으로 합치면 공통되는 컬럼만 합쳐진다.
#프린트문은 주석처리
# print(df) 

# outer 조인으로 합치면 공통된 컬럼이 아니더라고 값을 전부 조인해주고
# 값을 NaN으로 표시해 준다.
# print(dfouter)



'''
merge
- pd.merge(df1, df2, on=공통 column, how='inner')
how='inner'가 디폴트.
how에 inner, left, right, outer 를 사용할수 있다
- 특정 공통열을 기준으로, 나머지 열까지 조인할수 있다.
'''

# 여기서는 데이터를 다운받아 사용한다 (데이터는 깃허브에 있다)
person = pd.read_csv('./pandas/data/survey_person.csv') #관측한 사람의 이름
site = pd.read_csv('./pandas/data/survey_site.csv') #관측한 위치
survey = pd.read_csv('./pandas/data/survey_survey.csv') #날씨 정보
visited = pd.read_csv('./pandas/data/survey_visited.csv') #관측한 날짜

'''
person 과 survey는 공통으로 가지고 있는 데이터의 column 이름이 서로 다르다.
person 에서는 ident라는 이름의 column 이고 vurvey 에서는 person이라는 이름의 column이다
이렇게 하나의 공통된 column으로 다른 column도 join하고 싶을 때 merge를 사용한다.
'''

#person의 ident survey의 person 값을 기준으로 DataFrame merge
#person의 ident를 기준으로 survey의 column들을 조인
#디폴트는 교집합의 개념인 innerjoin 이다.
dfmerge = person.merge(survey, left_on = 'ident', right_on = 'person')

# person과 survey에 서로에게 없는 데이터가 있을 경우
# 합집합의 개념인 how='outer'를 인자값으로 넘겨주면 된다.
# 그럼 서로에게 없는 데이터는 NaN으로 채워진다.
dfmerge = person.merge(survey, left_on='ident', right_on='person', how='outer')


# person의 데이터는 전부 출력되고, 이것과 겹치는 survey의 값만 합쳐서 뽑고 싶으면
# how='left'를 인자값으로 넘기면된다.
dfmerge = person.merge(survey, left_on='ident', right_on='person', how='left')



#반대로 survey의 값은 전부 출력되고, 이것과 겹치는 person의 값을 합쳐서 뽑고 싶으면
#how='right'를 인자값으로 넘기면 된다.
dfmerge = person.merge(survey, left_on='ident', right_on='person', how='right')

'''
만약 두 데이터의 공통된 값이 있는 컬럼 이름이 같다고 하면
left_on, right_on 을 사용 하지 말고 통합으로 on='컬럼이름'을 인자값으로 넘기면 된다.
'''

