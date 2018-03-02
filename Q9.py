list1 = [1,2,4,5,4,5,1,2,1,3,8,96,7,4,7,8,9,6,96,4,2,3,8,5,7,1,4,9,6,1000]
def f(int):
    d1={}
    for no in int:
        if no in d1:
            d1[no] +=1
        else:
            d1[no] =1

    print(d1)
    return(d1)
f(list1)
