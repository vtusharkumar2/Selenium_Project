# #To create a table of any number

# for i in range(1,11):
#     print("5 X",i,"=",5*i)


# #for checking if a number is palindrome

# def palindrome():
#     num=input("enter number:")
#     if num==num[::-1]:
#         print("palindrome")
#     else:
#         print("is not a palindrome")

# palindrome()

#DSA1: Reverse a string

# str=input("enter txt to reverse:")

# rev_str=str[::-1]
# print("the reversed string is:",rev_str)



#DSA2 find duplicate elements in a list

# list1=[1,2,3,4,1,2,5,6]
# seen=set()
# duplicates=set()

# for num in list1:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
# print("duplicates:",list(duplicates))


#DSA3 To remove duplicate elements from list

# list1=[1,2,3,4,2,3,4,5]
# seen=set()
# uni_list=[]

# for num in list1:
#     if num not in seen:
#         uni_list.append(num)
#         seen.add(num)


# print("unique_list:",uni_list)


# To see if two strings are anagrams


# def anagrams(str1,str2):
#     return sorted(str1)==sorted(str2)
        
    
# str1=input("enter string1:")
# str2=input("enter string2")

# if anagrams(str1,str2):
#     print("are anagrams")
# else:
#     print("are not anagrams")


#To reverse a sentence

sentence= "QA could be good"

reverse_sentence="".join(sentence.split()[::-1])

print(reverse_sentence)
    