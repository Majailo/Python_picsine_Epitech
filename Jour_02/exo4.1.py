def p(n):
     
     p=0

     for i in range(0,n):
          a=(-1)**i
          b=(2*i)+1
          #k=(-1)**n/(2*n+1)
          k=a/b
          p+=4*k

     return p

#pi= p(5)

#print(format(pi,'.6f'))


def picalcul ():
       
       p=0
       n1=1
       n2=2
       i=0



       while True:
            
            a=(-1)**i
            b=(2*i)+1
            k=a/b
            p+=4*k 
            n1=n2
            n2=p
            i+=1

            if format(n1, "7f") == format(n2, "7f"):
                   return print(format(n2, "6f"))

picalcul()
            
                   
               
             

