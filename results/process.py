content = []
newContent = []
with open("map_3items.txt","r") as f:
  content = f.readlines()
  
for line in content:
  if "x" in line or len(line) < 50:
    continue
  else:
    newContent.append(line)
    
with open("out.txt","w") as f:
  for line in newContent:
    f.write(line)