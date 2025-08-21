# 1. reverse string without using slicing or reverse()
def reverse_str(data):
    result = ""
    for char in data:
        result = char + result
    # return result
    # print(result)

#2. Delete all consonants from string
def del_cons(data):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in data if not char.isalpha() or char in vowels])
    # return result
    # print (result)
    

#3. find sum of all prime numbers between 1 and N and print the numbers
def is_prime(number):
    total = 0
    for z in range(2,number):
        if (number%z == 0):
            return False
    return True

def add(number):
    total = 0
    for z in range(2,number+1):
        if(is_prime(z)):
            # print(z)
            total = total+z
    # return total
    # print(total)


'''4. you are given a string s of length n and an array of strings t containing m strings each of length n-1.
you need to remove one character from s such that s become equals to any of the m string.

find the total number of strings from the m given strings which can be obtained by removing one character from s.'''

def equiliser(s,n,t,m):
    count = 0
    slist = list(s)
    for i in range(n):
       char = slist.pop(i)
       for word in t:
           if "".join(slist)==word:
                count+=1
       slist.insert(i,char)
    return count

# print(equiliser('abcde',5,['abcd','abce','acde','bcde'],4))

'''5. Given an array of integers 'nums' and an integer 'target' return indices of two numbers such that they add up to target.

you may assume that each input would have exactly one solution, and you may not use the same element twice.'''


def find_target(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] ==target and len(output)==0:
                output.append(i)
                output.append(j)
    return output

print(find_target([3,5,7,8,6,4],10))





# <a href="https://www.youtube.com/watch?v=h9Tdd9Ljotc">Coding Interview Questions 2</a>

# <a href="https://www.youtube.com/watch?v=IT9A6ZtR_9s">Interview Questions</a>

# <a href="https://www.youtube.com/watch?v=vEYXEXI06D0">Interview Questions 2</a>

# <a href="https://www.youtube.com/watch?v=k6am31_ajHo">Interview Questions 3</a>






'''
Dear Faraz Ahmed Raj,

Thank you for accepting our interview invitation with Infosys. Here are the details for your interview with us. 
Candidate Id: 1007231455
Date: 07-Dec-2024
Time: 3:15 PM
Interview Link: https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZWRiMjI2MDYtZmNjYy00MjA5LWIzMjMtZGEzNWMwNTA2MGQ4%40thread.v2/0?context=%7b%22Tid%22%3a%2263ce7d59-2f3e-42cd-a8cc-be764cff5eb6%22%2c%22Oid%22%3a%22fd066652-232c-4a41-8a5c-912c2ee4e874%22%7d

- Request you to enable your webcam and mic during the interview.
- Please keep a government issued Photo Identity proof handy with you during interview.
- Please note, we will take screenshots of the interview for record purpose.
- Please use Google Chrome for accessing the Interview link.

Regards,
Talent Acquisition






'''
