# some_str='40 50 100 20'
# some_list=[440021,23,3,4,5,1]

# print(some_list[0])
# print(some_str[0])

# some_str.split()
# # some_list.split()
# print(some_str[1].split(),some_str.split()[1],some_str)
# print(some_str.split())

# some_str.split().sort()

# print(some_str.split())
# print(some_str)

# if 13:
#     print('참인가')
# else: 
#     print('거짓인가.')
# if ('M 45')==('M 45'):
#     print('참인가')
# else: 
#     print('거짓인가.')n, m = map(int, input().split())

# while True:
#      answer = input('0을 입력하지 않으면 끝나지 않습니다.')
#      if answer == '0':
#           break

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     # 버스노선정보 저장
#     lines = []
#     for i in range(N):
#         lines.append(list(map(int, input().split())))

#     #버스 노선개수 카운트 (정류장번호 -1에 빈도수 저장)
#     count = [0]*5000
#     for line in lines:
#         for dis in range(line[0]-1, line[1]):
#             count[dis] += 1

#     #물어보는 정류장의 방문 횟수 출력
#     P = int(input())
#     print('#{}'.format(tc), end=' ')
#     for bus_stop in range(P):
#         C = int(input())
#         print('{}'.format(count[C-1]), end=' ')

# [27,35,12,3,4,56,42] > 27부터 시작해서 가장큰 56이 맨뒤에 안착
# a= [27,35,12,3,4,56,42] 
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j+1],a[j]= a[j], a[j+1]
# print(a)

a= [1,2,2,0,3,3,6,4,3,5]
b= [0,0,0,0,0,0,0]
e= [0,0,0,0,0,0,0,0,0,0]
for i in range(len(a)):
    b[a[i]] += 1	# 1의값이면 1의 자리 +1  [c를 만들어가는 과정]
for i in range(0,len(b)-1):
    b[i+1] += b[i]	# [d를 만들어가는 과정]
for i in range (len(a)-1,-1,-1):
    e[b[a[i]]-1] = a[i]
    b[a[i]] -= 1
print(e)

# [27,35,12,3,4,56,42] > 27부터 시작해서 가장큰 56이 맨뒤에 안착
a= [27,35,12,3,4,56,42] 

for i in range(len(a)-1):	#6번 대상을 선정
    for j in range(len(a)-i-1):	#뒤에가 점점 차서 비교횟수가 줄어든다. 처음에 6번비교! 그다음 5번!
        if a[j]>a[j+1]:
            a[j+1],a[j]= a[j], a[j+1]
print(a)

