def Hanoi(n,source ,auxillary,destination):

    if n==1:
     print("Move disk 1 from",source ,"to" ,destination)
     return
    Hanoi(n-1, source , destination ,auxillary)
    print("Move disk",n, "from",source ,"to" ,destination)
    Hanoi(n-1 , auxillary , source ,destination)

n=3
Hanoi(n,'A','B','C')