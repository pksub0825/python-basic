#숫자형
# print(5)
# print(-10)
# print(1000)
# print(3.14)
# print(4+5)
# print(2*8)
# print(3*(3+1))

#문자형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*8)

#참/거짓
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not (5<10))

#변수
#애완동물을 소개해 주세요~
# animal="고양이"
# name="야옹이"
# age=2
# hobby="산책"
# is_adult=age>=3

# print("우리집 "+animal+"의 이름은 "+name+"예요")
# hobby="공놀이" #변수를 재선언하면 뒤에로 된다
# #print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요") # + 대신 , 로 연결이 가능 // 단, 띄어쓰기됨
# print(name+"는 어른일까요? "+str(is_adult))

'''
Q)변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력

출력문장:XX행 열차가 들어오고 있습니다.
'''
'''
station="사당"
p="행 열차가 들어오고 있습니다."
print(str(station+p))
station="신도림"
print(str(station+p))
station="인천공항"
print(str(station+p))
'''

#연산자
# print(1+1)
# print(2**3) #2^3
# print (10%3) #1
# print(10//3) #3

# print(10<3)#false
# print(4>=10)#false
# print(10<=10)#true

# print(3==3)#true
# print(4==2)#false
# print(3+4==7)#true

# print(1!=3)#true
# print(not(1!=3))#false

# print((3>0) and (3<5)) #true
# print((3>0)&(3<5))#true

# print((3>0) or (3<5)) #true
# print((3>0)|(3<5))#true

# print(5>4>3) #true
# print(5>4>7) #false

# 기본수식
# print(2+3*4) #14
# print((2+3)*4) #20
# number=2+3*4 #14
# print(number)
# number=number+2 #16
# print(number)

# number+=2
# print(number) #18
# number*=2 #36
# print(number)
# number/=2 #18
# print(number)
# number-=2 #16
# print(number)

# number%=5 #1
# print(number)

#숫자처리함수
# print(abs(-5)) # 절대값 5 
# print(pow(4,2)) # 4^2=16
# print(max(5,12)) #큰값 12
# print(min(5,12)) #작은값 5
# print(round(3.14)) #반올림 3
# print(round(4.9)) #5

# from math import *
# print(floor(4.99)) #내림.4
# print(ceil(3.14)) #올림.4
# print(sqrt(16)) #제곱근.4

#랜덤함수
#from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10)+1)# 0~10이하의 임의의 값 생성

#로또번호 생성/ 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

#print(randrange(1,46)) #1~46미만의 임의의 값 생성 / 뒷숫자 포함하지 않음(뒷숫자-1)

#print(randint(1,45)) #1~45이하의 임의의 값을 생성 / 뒷숫자를 포함함
'''
# Q)당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 1번 오프라인의 날짜를 랜덤으로 정하여라

# 조건 : 랜덤으로 날짜를 뽑아야함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건3: 매우러 1~3일은 스터티 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디모임 날짜는 매월 X일로 선정되었습니다.

from random import *
d=randint(4,28)
print("오프라인 스터디모임 날짜는 매월 "+str(d)+"일로 선정되었습니다.")
'''
#문자열
# sentence='나는 소녀입니다'
# print(sentence)
# sentence2="파이썬은쉬워요"
# print(sentence2)
# sentence3="""
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# #슬라이싱
# jumin="990120-1234567"

# print("성별 : "+jumin[7])
# print("연 : "+jumin[0:2]) #0~2번째 자리 직전까지(0,1번째)
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])

# print("생년월일 : "+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : "+jumin[7:]) #7번째자리부터 끝까지
# print("뒤 7자리 (뒤에부터) : "+jumin[-7:])
# #맨뒤에서 7번째 끝까지 // 뒤 첫번째자리 -1

#문자열 처리 함수
# python="Python is Amazing"
# print(python.lower()) #전부다 소문자로
# print(python.upper()) #전부다 대문자로
# print(python[0].isupper()) #첫번째자리가 대문자인지 True
# print(python[0].islower()) #첫번째자리가 소문자인지 False
# print(len(python)) #문자길이 //17
# print(python.replace("Python", "Java ")) #문자를 바꿈, Python->Java

# index=python.index("n") # n이 몇번째 문자위치에 있는지
# print(index) #5번째에 있다

# index=python.index("n", index+1) #두번째 n이 몇번째위치에 있는지
# print(index)

# print(python.find("n")) # n이 몇번째 문자위치에 있는지
# print(python.find("Java")) #찾는 문자가 없으면 -1
# # print(python.index("Java")) #error

# print(python.count("n")) # n이 몇개 있는지

#문자열 포맷
#방법1
# print("나는 %d살 입니다." %20) # %d 정수
# print("나는 %s을 좋아해" % "파이썬") # %s 문자열
# print("Apple은 %c로 시작해요" % "A") # %c 문자

# print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간")) # 중괄호에 순서대로 입력
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간")) # 중괄호 안 번호대로 입력
# print("나는 {1}색과 {1}색을 좋아해요".format("파란","빨간"))

#방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=29, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=29, color="빨간"))

#방법4
# age=20
# color="빨간"

# print("나는 "+str(age)+"살이며, "+color+"색을 좋아해요.")

# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#문자열 앞에 f를 붙이면 {}로 변수를 불러낼수 있다.

# #탈출문자
# # \n : 줄바꿈
# print("백문이 불여일견 \n 백견이 불여일타")

# # \" : 문장 내 "
# print("저는 \"나도코딩\"입니다.")

# # \\ : 문장내에서 \
# print("d:\\PythonWorkspace\\practice.py")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # 커서 맨 앞으로 이동해서 Red 대신 Pinedl 옴 // PineApple 

# # \b : 백스페이스(한 글자 삭제)
# print("Red\bApple") # ReApple

# # \t : 탭
# print("Red\tApple") # Red     Apple

'''
Q) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙 1: http:// 부분은 제외 => naver.com
규칙 2: 처음만나는 점(.) 이후 부분은 제외 => naver
규칙 3: 남은 글자중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"(!)로 구성

예) 생성된 비밀번호 : nav51!
'''

# url="http://naver.com"
# r1=url[7:] # naver.com
# index=r1.index(".")
# r2=r1[:index] # naver
# r3=r2[:3]+str(len(r2))+str(r2.count("e"))+"!"
# print(r3)

url="http://daum.net"
r1=url.replace("http://","")
r1=r1[:r1.index(".")]
password=r1[:3]+str(len(r1))+str(r1.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))


