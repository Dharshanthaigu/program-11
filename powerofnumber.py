def power(b,e):
  if(e==1):
    return(b)
  if(e!=1):
    return(b*power(b,e-1))
b,e=input.split()
b=int(b)
e=int(e)
print(power(b,e))
  
