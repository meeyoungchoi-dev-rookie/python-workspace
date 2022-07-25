sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence)

# slicing
jumin = "990120-1234567"

print("성별: " + jumin[7])
print("연: " + jumin[0:2]) # 0 부터 2 인덱스 직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:]) # 7인덱스 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python[0].isupper()) # 0인덱스의 값이 대문자인지 판별
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 첫번째 n이 나온 인덱스 위치부터 계산해서 또 n이 나오는 위치를 찾는다
print(index)

print(python.find("n"))
print(python.find("Java")) # 원하는 값을 찾을 수 없을때 : -1
#print(python.index("Java")) # 원하는 값을 찾을 수 없는 경우 ValueError 발생

print(python.count("n"))

# 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
