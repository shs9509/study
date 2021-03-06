#https://www.acmicpc.net/problem/10026

def cons(li, scale, char):  # li = 색깔배치, scale = 배치 크기, char = 해당하는 색깔
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]
    count = 0   # 구역 숫자
    visited = [['o' for j in range(size)] for k in range(size)] # 확인한 색깔 체크용리스트
    for x in range(size):
        for y in range(size):
            if (li[x][y] in char) and (visited[x][y] != 'V'):   # 원하는색깔이며 방문하지 않았다!
                start_x = x
                start_y = y # x,y 그대로쓰면 밑에서 위의 for문의 xy가 바뀜
                count += 1  # 구역 추가 
                S = list()
                S.append([start_x,start_y])
                while len(S) != 0:
                    start_x, start_y = S.pop()
                    visited[start_x][start_y] = 'V' # 방문 체크해주기
                    for i in range(4):
                        X = start_x + dr[i]
                        Y = start_y + dc[i]
                        if 0 <= X < size and 0 <= Y < size:
                            if li[X][Y] in char and visited[X][Y] != 'V':
                                S.append([X,Y])
    return count

size = int(input())
section = list()
for i in range(size):
    section.append(list(input()))

person =cons(section,size,['B'])+cons(section,size,['R'])+cons(section,size,['G'])
color_blindness= cons(section,size,['B'])+cons(section,size,['G','R'])
print(person,color_blindness)

'''
5
RBBBG
RBBBB
RBBBB
RBBBB
RBBBB
이거일때 G 가생이의 G가 인식안함 왜?
'''