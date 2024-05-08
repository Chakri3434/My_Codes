def pal(n):
  p=n.lower()
  if p=='':
    return True
  elif p[0]==p[-1]:
    return pal(p[1:len(p)-1])
  else:
    return False
print(pal(input()))
