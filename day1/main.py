inp =  open('input.txt','r')
inp = inp.read()
inp = inp.split("\n")
m = 0
x = int(inp[0])
for i in inp:
  i = int(i)
  if i > x:
    m+=1
  x = i
print(m)
