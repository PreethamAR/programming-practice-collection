
#1 Function getSum to get Sum of numbers

def getSum(number1, number2):
    return number1+number2

def invoke_getSum():
    sum = getSum(10,20)
    print("Sum of two number is ", sum)

    sum2 = getSum(1.2,1.2)
    print("Sum of two number is ", sum2)

    sum3 = getSum("Hello "," World")
    print("Sum of two number is ", sum3)


def getIntegerSum(number1: int, number2: int) ->int:
    ans = number1 + number2
    return ans

def invoke_getIntegerSum():
    sum1 = getIntegerSum(1.2, 1.5)
    print("Sum of two number is ", sum1)

    sum2 = getIntegerSum(100, 1.5)
    print("Sum of two number is ", sum2)


#2 Function swapNumbers to Swap two variable values

def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp
    return item1, item2

def swapSimple(item1, item2):    
    return item2, item1


def invoke_swap():
    number1 = 10
    number2 = 20

    print(f"Before swapping: Value of number1 = {number1} and number2 = {number2}")
    # number1, number2 = swap(number1, number2)

    number1, number2 = swapSimple(number1, number2)
    print(f"After swaping: Value of number1 = {number1} and number2 = {number2}")

#3 Function isEven to return true if number is even otherwise false

#def isEven(number: int)-> bool: 
def isEven(number):
    if (number%2 == 0):
        return True
    else:
        return False
 
def invoke_isEven():    
    input = 100
    result = isEven(input)

    if result:
        print(f"{input} is even")
    else:
        print(f"{input} is odd")


#4Function isNumber to return true if it is an getIntegerSum

def isNumbers(number):
    isInteger = True    

    for eachCharacter in number:
        if (eachCharacter >= '0' and eachCharacter <= '9'):
            continue
        else:
            isInteger = False
            break
    
    return isInteger
        
def isNumbers_V2(number):
    # Check if any of the character falls outside the range 0 to 9, if yes return false
    for eachCharacter in number:
        if (eachCharacter < '0' or eachCharacter > '9'):
            return False
    
    # All the characters are between 0 to 9 hence return True
    return True


def invoke_IsNumbers():
    #result = isNumbers("1234")
    #result = isNumbers("a12a34")

    result = isNumbers_V2("a12a34")

    if result:
        print("Yes it is an integer")
    else:
        print("No it is not an an integer")
    
#5 -> Function  simpleGreetings to accept name as input and print simple greetings Namaskara name
def simpleGreetings():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Namaskara {name}")
    print(f"You are  {age} years old now")

#6-> Function to Print ASCII  values of string input

def printASCIIOfString(string):
    for character in string:
        ascii_value = ord(character)
        print(f"{character} -> {ascii_value}")


def invoke_printASCIIOfString():    
    printASCIIOfString("abc")
    printASCIIOfString("123")
    printASCIIOfString("ABC")


# 7-> Function to getStrlength to get string length

def getStrLength(string)->int:
    counter = 0
    
    if string != None:
     for character in string:
        counter = counter + 1

    return counter

def invoke_getStrLength():
    input1 = None # NULL 
    length = getStrLength(input1)
    print(f"String length of {input1} is {length}")

    input2 = "" # Empty string
    print(f"String length of {input2} is {getStrLength(input2)}")

    input3 = "m" # only one item is present
    print(f"String length of {input3} is {getStrLength(input3)}")

    input4 = "mahesh" # many items are present
    print(f"String length of {input4} is {getStrLength(input4)}")   

#8-> Function to Count vowels  getCountOfOvewel for a given string

def count_vowels(string)-> int:
    counter = 0

    #This was to show another not so good way to write if statement
    # if (character == 'a' or character == 'e' or  character == 'i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):

    if string is not None:  # if (string != NULL) this is how we write this in C
        for character in string:
            if (character == 'a' or
                character == 'e' or 
                character == 'i' or 
                character == 'o' or 
                character == 'u' or 
                character == 'A' or 
                character == 'E' or 
                character == 'I' or 
                character == 'O' or 
                character == 'U'):
                counter +=1  # counter = counter + 1
    
    return counter

def invoke_count_vowels():
    input = "mahesh"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = None
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = ""
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = "a"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = "123"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")



#9 - Function to Reverse string reverseString 

def reverseString(string)->str:

    length = len(string)
    
    #for start, end in zip(range(0,length, 1), range(length-1, -1, -1)):
        #print(f"Start = {start} end = {end}")
        #string[start], string[end] = string[end], string[start]

    reversedString = ""
    for end in range(length-1, -1, -1):
        reversedString += string[end]
    
    return reversedString

def invoke_stringReverse():
    name = "abcde"
    name = reverseString(name)
    print(name)

# 10 - Function to get sum of all elements in the integer array getSum

def getSum(numbers)->int:

    sumOfElements = 0
    for number in numbers:
        sumOfElements = sumOfElements + number
    
    return sumOfElements

def getSumV2(numbers: list):

    sumOfElements = 0
    length = len(numbers)
    
    for index in range(0, length, 1):
        sumOfElements = sumOfElements + numbers[index]
    
    return sumOfElements


def invoke_getSum():
    numbers = [1,2,3]

    #numbers = [1.1,2.1,3.1]
    #sumOfNumbers = getSum(numbers)

    sumOfNumbers = getSumV2(numbers)
    print(f"Sum of numbers = {sumOfNumbers}")

# 11 -> Function to find given string is Palindrome, function isPalidrome returns true if string is palindrome

def isPalindrome(string: str)->bool:
    leftIndex = 0
    rightIndex = len(string) - 1
    result = True

    while (leftIndex < rightIndex):
        if string[leftIndex] != string[rightIndex]:
            result = False
            break

        leftIndex+=1
        rightIndex-=1
    
    return result

def invoke_isPalindrome():   
    input1 = "mam"
    input2 = "malayalam"
    input3 = "hello"
    input4 = "abba"
    input5 = "abcedcba"

    result = isPalindrome(input5)

    if result:
        print("String is palindrome")
    else:
        print("String is not Palindrome")


# 12 -> Function to print max and min value from an integer array ,  printMaxMin

#def getMaxMin(numbers: list)-> tuple[int,int]:

def getMaxMin(numbers:list):
    max = numbers[0]
    min = numbers[0]
    
    for index in range(1, len(numbers), 1):
        if numbers[index] > max:
            max = numbers[index]
        
        if numbers[index] < min:
            min = numbers[index]

    return max,min

def invoke_maxmin():
    input1 = [1,2,100,4,5,-1]
    resultMax, resultMin = getMaxMin(input1)
    print(f"Maximum value is {resultMax} and minium value is {resultMin}")


#13 -> Function to search in an sorted integer array
# aka binary search 

def search(numbers, key)->bool:
    leftIndex = 0
    rightIndex = len(numbers) -1    
    found = False

    while(leftIndex <= rightIndex):
        middleIndex = int(leftIndex + (rightIndex-leftIndex)/2) # Typecasting

        if(numbers[middleIndex] == key):
            found = True
            break

        if (numbers[middleIndex] > key):
            # you must search on the left side of the array
            rightIndex = middleIndex - 1
        else:
            # you must search onthe right side of the array
            leftIndex = middleIndex + 1
        
    return found

def invoke_search():
    input1 = [1,2,3,4,5,6]
    key = 6

    result = search(input1, key)

    if result:
        print("Number is found")
    else:
        print("Number is not found")

# 14 - Function to merge two arrays and return combined output in first array

def mergeList(list1: list, list2:list):
    for item in list2:
        list1.append(item)
    
def invoke_mergeList():
    list1 = [1,2,3]
    list2 = [4,5]
    mergeList(list1, list2)
    print(list1)

#15 - Function get second largest element in an integer array  getSecondLargest

def getSecondLargestNumber(numbers)->int:
    largestMax = numbers[0]
    secondLargest = numbers[0]

    for index in range(1, len(numbers), 1):
        # If new number we scanned is greater than current largest
        # you have to update both variables

        if numbers[index] > largestMax:
            secondLargest = largestMax
            largestMax = numbers[index]
        elif numbers[index] > secondLargest and numbers[index] != secondLargest:
            secondLargest = numbers[index]    
        elif largestMax == secondLargest and numbers[index] < largestMax:
            secondLargest = numbers[index]    
    
    return secondLargest

def getSecondLargestNumber_v2(numbers)->int:
    largestMax = float('-inf')
    secondLargest = float('-inf')

    for index in range(0, len(numbers), 1):
        # If new number we scanned is greater than current largest
        # you have to update both variables

        if numbers[index] > largestMax:
            secondLargest = largestMax
            largestMax = numbers[index]
        elif numbers[index] > secondLargest:
            secondLargest = numbers[index]    
        
    return secondLargest

def invoke_getSecondLargestNumber():
    input1 = [-1,-2,-4,-5]
    #input1 = [5,4,3,2,1]
    #input1 = [8,1,2,6,10]
    result = getSecondLargestNumber_v2(input1)
    print(f"Second largest number is {result}")

# 16 - Function to print unique elements in an integer array   printUniqueElements
# Ignore those numbers completely which have duplicates 
def printUniqueElements(numbers):

    for read_index in range(0, len(numbers), 1):
        isDuplicate = False

        for compare_index in range(0, len(numbers),1):
            if read_index == compare_index:
                continue

            if numbers[read_index] == numbers[compare_index]:
                isDuplicate = True
                break
        
        if(isDuplicate == False):
            # This is unique element, hence print it
            print(numbers[read_index])

def invoke_printUniqueElements():
    input1 = [1,2,3,2,4,1]
    #input1 = [1,2,3,4,5]
    printUniqueElements(input1)


# 17 - Function to print intersection or common elements of two integer arrays  getCommonElements

def printCommonElements(input1, input2):

    for input1_index in range(0, len(input1), 1):
        isFound = False
        for input2_index in range(0, len(input2), 1):
            if input1[input1_index] == input2[input2_index]:
                isFound = True
                break
        
        if isFound:
            print(input1[input1_index])


def invoke_printCommonElements():
    input1 = [1,2,3,4,7,9,8]
    input2 = [9,6,7,8]

    printCommonElements(input1, input2)

# 18 - Function to get count of words in the string  getCountOfWords
# There will be no word or atleast one word in the input
def getWordCount(string):
    counter = 1

    if (len(string) == 0):
        return 0
    
    for char in string:
        if char == ' ' or char == '\t' or char == '\n':
            counter+=1
  
    return counter


def invoke_getWordCount():
    input = ""
    count = getWordCount(input)
    print(f"Count of words = {count}")
    
# 19 - Function to print binary values of various input like integer, char , also perform shift operations on integers

def printBinaryForm(number: int):
    no_of_bits = number.bit_length()
    print(f"Number of bits = {no_of_bits}")

    mask = 1
    mask = mask << no_of_bits-1

    for _ in range(no_of_bits):
        if (number & mask):
            print("1", end=" ")
        else:
            print("0", end=" ")
        
        mask = mask >> 1


def invoke_printBinaryForm():
    printBinaryForm(1)
    printBinaryForm(1024)

#20 - Function to remove spaces from the string  removeSpaces

def removeSpaceFromString(string):
    output = ""

    for character in string:
        if character != ' ' and character != '\t' and character != '\n':
            output = output + character
    
    print(output)

def invoke_removeSpaceFromString():
    input = "  a"
    removeSpaceFromString(input)

## Invocation
invoke_removeSpaceFromString()















