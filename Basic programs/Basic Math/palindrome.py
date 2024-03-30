def pal(n):
  if n=='':
    return True
  elif n[0]==n[-1]:
    return pal(n[1:len(n)-1])
  else:
    return False
print(pal(input()))
