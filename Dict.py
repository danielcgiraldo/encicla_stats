Suramericana = {}
Colombia = {}
Campus_Nacional = {}
Carlos_E = {}
arc = open("data.txt").readlines()
key = ["Suramericana","Colombia","Carlos E. Restrepo","Campus Nacional"]
fechas = set()
for element in arc:
  new = element.split(",")
  fechas.add(new[2])
date = sorted(fechas)
for number in arc:
  new = number.split(",")
  if new[0] == "Suramericana":
    for i in date:
      Suramericana[i] = []
  elif new[0] == "Colombia":
    for i in date:
      Colombia[i] = []
  elif new[0] == "Campus Nacional":
    for i in date:
      Campus_Nacional[i] = []
  elif new[0] == "Carlos E. Restrepo":
    for i in date:
      Carlos_E[i] = []
for number in arc:
  n = number.rstrip()  
  new = n.split(",")
  if new[0] == "Suramericana":
    for i in date:
      Suramericana[i].append([new[1],new[3]])
  elif new[0] == "Colombia":
    for i in date:
      Colombia[i].append([new[1],new[3]])
  elif new[0] == "Campus Nacional":
    for i in date:
      Campus_Nacional[i].append([new[1],new[3]])
  elif new[0] == "Carlos E. Restrepo":
    for i in date:
      Carlos_E[i].append([new[1],new[3]])
print(Colombia)
print(Suramericana)
print(Campus_Nacional)
print(Carlos_E)
