import time

I = 0
F = 0
N = 0
P = 0

M = ""
B = ""
T = ""
I2 = ""

print("MBTI 성격유형 검사를 시작하겠습니다.")
time.sleep(2)
print("1과 2로 응답하지 않으면 검사 결과가 정확하지 않을 수 있습니다.")
time.sleep(2)
#여기부터 E,I 코드
print("처음 보는 사람과도 쉽게 친해질 수 있다. (예 : 1, 아니오 : 2)")
if input() == "1":
    I += 1
else:
    I -= 1
print("항상 신중하게 행동하는 것이 중요하다. (예 : 1, 아니오 : 2)")
if input() == "2":
    I += 1
else:
    I -= 1
print("매사에 적극적이다. (예 : 1, 아니오 : 2)")
if input() == "1":
    I += 1
else:
    I -= 1
#여기부터 T, F 코드
print("뭐든지 논리적으로 생각하고 행동한다. (예 : 1, 아니오 : 2)")
if input() == "1":
    F += 1
else:
    F -= 1
print("감정보다 이성을 더 중요시 여기지 않는다. (예 : 1, 아니오 : 2)")
if input() == "2":
    F += 1
else:
    F -= 1
print("다른 사람과의 관계가 가장 중요하다. (예 : 1, 아니오 : 2)")
if input() == "1":
    F += 1
else:
    F -= 1
#여기부터 S, N 코드
print("뭐든지 철저하게 행동한다. (예 : 1, 아니오 : 2)")
if input() == "1":
    N += 1
else:
    N -= 1
print("내 감각에 의존한다. (예 : 1, 아니오 : 2)")
if input() == "1":
    N += 1
else:
    N -= 1
print("미래지향적이다. (예 : 1, 아니오 : 2)")
if input() == "2":
    N += 1
else:
    N -= 1
#여기부터 J, P 코드
print("일정을 쉽게 변경 가능하다. (예 : 1, 아니오 : 2)")
if input() == "2":
    P += 1
else:
    P -= 1
print("분명한 목적을 가지고 행동한다. (예 : 1, 아니오 : 2)")
if input() == "1":
    P += 1
else:
    P -= 1

print("뭐든지 논리적으로 생각하고 행동한다. (예 : 1, 아니오 : 2)")
if input() == "1":
    P += 1
else:
    P -= 1
#여기부터 결과 코드
if I >= 0:
    M = "E"
else:
    M = "I"

if F >= 0:
    B = "T"
else:
    B = "F"

if N >= 0:
    T = "S"
else:
    T = "N"

if P >= 0:
    I2 = "J"
else:
    I2 = "P"

print("당신의 MBTI는,")
time.sleep(2)
print(M+T+B+I2+"입니다.")
