# 변수
message = "hello"
num1 = 7
num2 = 3.5
print(message, num1, num2)

# 입출력
user_message = input('메세지를 입력하세요: ')
print(user_message)

# 조건문
user = input('가위/바위/보 중 하나를 내세요.: ')
comp = "바위" #그냥 간단히 바위만 내게 설정
if user == "가위":
    print("당신이 졌습니다!")
elif user == "바위":
    print("비겼습니다!")
else:
    print("당신이 이겼습니다!")

# 반복문
for i in range(0, 5):
    print("Hello world!")

for j in range(0,5):
    print(j)

h = 0
while h < 5:
    print("Hello world!")
    h += 1

while 1 == 1:
    print("Hello!")
    break

# 함수
def sum(a,b):
    result = a + b
    return result

num1 = int(input('첫번째 숫자 입력>> '))
num2 = int(input('두번째 숫자 입력>> '))
print(sum(num1, num2))