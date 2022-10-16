list=[1,2,3,4,5,6,7,8,10,11,12,15]
for index,item in enumerate(list):
    if index==2 or index ==5 or index ==11 or index== 15:
        print(f"The {index+1} element is {item} ")