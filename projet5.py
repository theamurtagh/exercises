#poblem 5 Thea Murtagh, the solution made sense to me, but i did not come up with it- https://www.youtube.com/watch?v=EMTcsNMFS_g

def prob5():
    i=20
    while 1:
        i+=20
        if  i%11==0 and i%12==0 and i%13==0 and \
            i%14==0 and i%15==0 and i%16==0 and \
            i%17==0 and i%18==0 and i%19==0: 
             print(i)
             break
