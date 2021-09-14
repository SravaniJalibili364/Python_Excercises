import datetime
base=datetime.datetime.today()
lst=["Maths","Physics","Chemistry"]
#for ele in range(lst)
for x in range(0,len(lst)):
        print(x+str(base+datetime.timedelta(days=x)))
    