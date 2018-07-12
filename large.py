def l(n):
  map(int,n)
  n.sort()
  n.reverse()
  return ''.join(map(str,n))

s = int(input())
num = input().split()
res = l(num)
print (res)
