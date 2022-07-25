# 리스트

# 지하철 칸별로 10명, 20명 , 30명
subway = [10,20,30]
print(subway)

subway = ["유재석" , "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가
print(subway.index("조세호"))

# 하하씨가 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort();
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20 , True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 모두 지우기
num_list.clear();
print(num_list)

# 딕셔너리
# key에 대한 중복이 허용되지 않는다
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# 없는 키를 사용하여 value를 가져오려는 경우
#print(cabinet[5]) # key에 해당하는 값이 없으면 에러가 발생한다
#print(cabinet.get(5)) # 값이 없으면 None

print(3 in cabinet)
print(3 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key , value 함께 출력
print(cabinet.items())

# 삭제
print(cabinet.clear)