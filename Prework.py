

#Question 1
print("Question 1: \n")

def hello_name(user_name):
    print("hello " + user_name)

hello_name('Eddie')
#----------------------------------

#Question 2
print("Question 2: \n")

def first_odds():
    for num in range(100):
        if num % 2 != 0:
            print(num)

first_odds()
#---------------------------------

#Question 3
print("Question 3: \n")

def max_num_in_list(a_list):
    max = 0
    for i in range(len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
    return max

#Tests

my_list = [1,4,6,7,23,45357]
other_list = [4,35,46353,2356753645]
print(max_num_in_list(my_list))  #45357
print(max_num_in_list(other_list))  #2356753645
#---------------------------------

#Question 4
print("Question 4: \n")

def is_leap_year(a_year):
    if a_year % 4 != 0:
        return False
    elif a_year % 100 == 0:
            return False
    elif a_year % 400 == 0:
        return True
    else:
        return True 
    
#Tests

print(is_leap_year(1994)) #False
print(is_leap_year(2020)) #True 
print(is_leap_year(1800)) #False
print(is_leap_year(1996)) #True
#---------------------------------

#Question 5
print("Question 5: \n")

def is_consecutive(a_list):
    list_copy = []
    for num in a_list:
       list_copy.append(num)
    a_list.pop(0)       #Remove first index
    list_copy.pop()     #Remove last index
    for i in range(len(a_list)):
        if a_list[i] - list_copy[i] != 1:   #Compare new first index (AKA second index of original list) to original first index
            return False
    return True
   
       
#Tests

my_list = [1,2,3,4,6]
other_list = [3,4,5,6,7,8,9,10]
third_list = [4,6,3,6,3,]
fourth_list = [11,12,13,14,15,16,17,18,19,20]
print(is_consecutive(my_list)) #False
print(is_consecutive(other_list)) #True
print(is_consecutive(third_list)) #False
print(is_consecutive(fourth_list)) #True

