#  prblem 1:Reverse a String

# word = 'hello'
# reverse = word[::-1]
# print(reverse)

# Problem 2: Count Vowels in a String
# word = 'Apple'
# def vowels(word):
#     str = word.lower()
#     vowels = ['a','e','i','o','u']
#     count = 0
#     for i in str:
#          if(i in vowels):
#           count +=1
          
#     print(count)     
   
  
     
# vowels(word)    



# -------------   Problem 3: Sum of Digits

num =1234
def get_sum_string(num):
    strNum = str(num)
    
    addNum = 0
    for i in strNum:
        addNum += int(i)
    print(addNum)    
    
get_sum_string(num)    