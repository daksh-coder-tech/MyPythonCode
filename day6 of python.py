def print_list(list , index =0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list ,index + 1 )

fruits = ["mango", "litchi" , "apple" , "banana" ]

print_list(fruits , )