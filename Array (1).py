print("********** Programmed by: **********")
print("********** Lyza Jorella R. Del Rosario **********")


list1 = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
print(list1)


def menu() :
    print("Add an element (1)")
    print("Insert an element (2)")
    print("Modify an element (3)")
    print("Delete an element (4)")
    print("Arrange in ascending order (5)")
    print("Arrange in descending order (6)")
    print("Exit (7)")
  
          
menu()
option = int(input("Enter your option:"))

while option:
    
    if option == 1:
        #add an element
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.append
            edited_list = int(input("Add an element:"))
            add_element = list.append(edited_list)
            print(list)
            
    elif option == 2:
        #insert an element
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.append
            edited_list = int(input("Insert an element:"))
            add_element = list.append(edited_list)
            print(list)

        
    elif option == 3:
        #insert an element
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.append
            edited_list = int(input("Modify an element:"))
            add_element = list.append(edited_list)
            print(list)

        
    elif option == 4:
        #insert an element
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.append
            edited_list = int(input("Enter the index you want to delete:"))
            del list[edited_list]
            print("The element has been deleted. This is the new array:", list)


    elif option == 5:
        #arrange in ascending order
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.sort()
            print(list1)
        
    elif option == 6:
        #arrange in descending order
            list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
            list1.reverse()
            print(list1)
            
    elif option == 7:
        print("THANK YOUUUU!!!!")
        break          
 
        
    print()
    menu()
    option = int(input("Enter your option: "))
