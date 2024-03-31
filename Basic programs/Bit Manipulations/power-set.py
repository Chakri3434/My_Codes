def powset(s):
  n=len(s)
  powsize=pow(2,n)
  for counter in range(powsize):
    for i in range(n):
      if (counter & (1<<i))!=0:
        print(s[i])
    print('\n')
for i in range(int(input())):
  s=input()
  powset(s)
