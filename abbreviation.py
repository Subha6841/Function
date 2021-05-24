# program for showing a abbreviation of a word
def abbreviation(name):
   m=name[0]
   for i in range(len(name)):
        if name[i]==' ':
           m=m+'.'+name[i+1]
           m=m.upper()
   return m
name=input('Enter a name : ')
print('The abbreviated form is :',abbreviation(name))

        
    
