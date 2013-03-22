import commands

def encode(x):
  return commands.getoutput("ppt %d" % int((bin(int(x))[2:])))

while True:
  next = raw_input("> ")
  if next.isdigit() == True:  
    print encode(next)
  else:
    pass