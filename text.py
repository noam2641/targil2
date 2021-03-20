def revword(word:str):
  return(word[::-1].lower())
      
def countword():
    counter=1
    text=open('text.txt').read()
    text=text.replace('\n',' ')
    text=(text.lower())
    matword=text.split(' ')
    x = len(matword)
    i=0
    while i<=x:
       if revword(matword[0])==matword[i-1]:
           counter=counter+1
       i=i+1
    return(float(counter))


