for i in range(int(input())):
    (L, R) = tuple(map(int, input().split()))
    print("Case #" + str(i+1) + ": " + str(sum(_ for _ in range(min(L,R)+1))))
