for i in range(int(input())):
   bags, kids = input().split()
   total = sum(int(x) for x in input().split())
   print("Case #"+str(i+1)+": " + str(total%int(kids)))
