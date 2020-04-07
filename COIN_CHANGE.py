li=[0.05,0.10,0.25,1,2,5,10,20]
li.sort()
def Change(change):
    result=[]
    while change!=0.0:
        print(li)
        denom=li.pop(len(li)-1)
        if change>denom:
            number=change//denom
            result.append(str(denom)+' X '+str(number))
            change = round(change - (denom*number),2)
            print('old',change)
    print(result)

Change(37.25)
