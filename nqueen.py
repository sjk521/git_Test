def nQueens(sol, n):
    global count #총 몇번째 답인지
    if len(sol) == n:
        count += 1
        print("%d 번째 해결 : "%count, sol)
        return 0
    candi = list(range(n)) # 0~n-1
    #print(sol)
    for i in range(len(sol)):
        if sol[i] in candi:
            candi.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candi:
            candi.remove(sol[i] + distance)
        if sol[i] - distance in candi:
            candi.remove(sol[i] - distance)

    if candi != []:
        for j in candi:
            sol.append(j)
            nQueens(sol,n)
            sol.pop()
    else:
        return 0


count = 0


num = int(input("N-Queens의 크기를 입력하세요 : "))
for k in range(num):
    nQueens([k], num)
if count == 0:
    print("해답없음")
