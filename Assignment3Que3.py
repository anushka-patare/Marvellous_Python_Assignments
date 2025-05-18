def Display():
    print("Enter size of list:")
    size=int(input())


    Data2=list()
    print("Enter elements in list:")
    for i in range(size):
       no=int(input())
       Data2.append(no)

    min_element=Data2[0]
    for i in Data2:
        if i < min_element:
            min_element=i
            
    print("The minimum element is:",min_element)


if __name__=="__main__":
    Display()