num1 = 42 #variable declaration and primative number
num2 = 2.3 #variable declaration and number
boolean = True #variable declaration and boolean
string = 'Hello World' #variable declaration and initializing string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration and list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable dec and a dictionary with key and values
fruit = ('blueberry', 'strawberry', 'banana') # Tuple, allows to store multiple values in one variable
print(type(fruit)) # log statment nd checking the data type of the fruit variable
print(pizza_toppings[1]) #log statment, logging the second element in the list
pizza_toppings.append('Mushrooms') #adding an element with .append to the end of the list
print(person['name']) # Accessing a value in the person dictionary 
person['name'] = 'George' #updating the name value to 'George'
person['eye_color'] = 'blue'# adding new key value to the dictionary
print(fruit[2])#printing value at index 2 of the fruit tuple

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")# this is a conditional if else statment with print being run in the code blocks

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")#this is an elseif conditional

for x in range(5):# setting a range of 5 incraments by 1 by default this will be 0 -4
    print(x)
for x in range(2,5): #instead of starting at 0 it's starting at 2 going until 4 (5 is exclusive)
    print(x)
for x in range(2,10,3): # starting at to, going to 9 incramenting by 3 instead of default 1
    print(x)
x = 0
while(x < 5):#while loop
    print(x)
    x += 1

pizza_toppings.pop() # by default this will remove the last element in a list
pizza_toppings.pop(1) # will remove index 1 of the list

print(person)
person.pop('eye_color')
print(person) # will print person, then will print person without the eye_color key value

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # this will reach pepperoni in the pizza_toppings list the print statment then continue with loop
    #then once you get olives it will break out of the loop

def print_hello_ten_times():#function declaration
    for num in range(10):#loop with a range of 10 so it will print hello 10 times
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x):# function declaration and name with one parameter
    for num in range(x):#loop that loops within range passed into function
        print('Hello')#will print hello x bumber of times

print_hello_x_times(4) #function call 

def print_hello_x_or_ten_times(x = 10): #if nothing is passed into the function as an argument this will use the number 10
    for num in range(x):
        print('Hello')#loop will print hello x number of times or 10 if no argument given

print_hello_x_or_ten_times()#will print hello 10 times
print_hello_x_or_ten_times(4)#will print Hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)