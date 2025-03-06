sTr = input()
Left = 0
right = 0
newStr=[]
sT=""
for i in sTr:
  if i =="L":
    sT+=i
    Left+=1
  elif i =="R":
    sT+=i
    right+=1
  if Left != 0 and right != 0:
    if Left == right:
      newStr.append(sT)
      sT=""
      Left = 0
      right = 0
print(len(newStr))
for i in newStr:
  print(i)