def Display():
    print("enter size of list:")
    size=int(input())

    Data1=list()
    print("Enter elements into list:")
    for i in range(size):
        no=int(input())
        Data1.append(no)
    
    max_element=Data1[0]
    for i in Data1:
        if i > max_element:
            max_element = i
    print("The maximum element is:",max_element)

if __name__=="__main__":
    Display()

