for i in range(1,int(input())+1):
    (letters, questions) = tuple(map(int, input().split()))
    s = input()
    d = {}
    all_letters = set(s)
    total = 0
    for letter in all_letters:
        d[letter] = [0]
        for l in s:
            if l == letter:
                d[letter].append(d[letter][-1]+1)
            else:
                d[letter].append(d[letter][-1])
    for question in range(questions):
        count = 0
        (L,R) = tuple(map(int, input().split()))
        
        for letter in all_letters:
            count += (d[letter][R]-d[letter][L-1]) % 2
            if count>1: break
        else:
            if count < 2: total+=1
        
    print("Case #"+str(i)+": "+str(total))
