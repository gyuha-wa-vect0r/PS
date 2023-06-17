a = int(input()); b = int(input()); c = int(input());
gop = list(str(a*b*c))
for i in range(10):
  print(gop.count(str(i)))