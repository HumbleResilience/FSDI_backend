


def print_name ():
    print("Eric")



def list1(): 
    print("Working with lists (arrays)")

    names=['jon', 'blake']
    #add values to the list
    names.append("Eric")
    names.append("juan")


    #get the values

    print(names[0])
    print(names[3])

    print(names)

    #for loops
    for name in names:
        print(name)


def list2():
    print("-" * 30)

    nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]

    #1- print the sum of all numbers
    total = 0

    for number in nums:
       total += number
       
    print(total)


# 2 - print all numbers lower than 50
#2b-  0 count how many numbers are lower than 50

    count = 0
    for number in nums:

        if number < 50:
            print(number)
            count += 1

    print(f"there are: {count} nums lower than 50")


    #3 - find the smallest number in the list
    #variable that start with any num from the list (first)
    # for
    #compare if the num is lower than your smallest number

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    print(f"the smallest in the list is {smallest}")

def dict1():
    print("Dictionary tests 1 ----------------")

    me = {
            "name": "Eric",
            "last": "Moore",
            "age:": 35,
            "hobbies":[],
            "address":{
                "street": "Evergreen",
                "number": 42,
                "city": "SpringField"

                }
    }

    print( me["name"])

    print(me["name"] + " " + me["last"])


    me["age"] = 99

    me["email"] = "emoore.tech@gmail.com"

    print(me)

#print fujll address in single line

    address = me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")

   

list1()
list2()
dict1()