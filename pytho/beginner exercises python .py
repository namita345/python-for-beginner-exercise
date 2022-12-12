#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Use python to know your age
birth_year = input("what is your birth year: ")
age = 2022 - int(birth_year)
print (age)


# In[4]:


# check in a paitient name 1. Raheela khan 2. new paitient 3. 20 years old
Patient_name = "Raheela Khan"
age = 20
new_patient = True


# In[1]:


# input name and print hi name 
name = input("what is you name: ")
print('Hi' " "+ name)


# In[5]:


First_name = input("What is your name: ")
Favourite_color = input("Please input your Favourite color: ")
print (First_name +"Likes The color " +Favourite_color )


# In[1]:


#ask a user their weight(in pounds) and convert it to kilograms
enter_weight_lbs = input("enter your weight in lbs: ")
print(int(enter_weight_lbs) * 0.4)


# In[3]:


# string rules
# number 1 use double quote when adding apostrophies
print ("python's course in Pakistan")
#and if we want to add double quotes like "Pakistan" use single quote like this:
print('python coure in "pakistan"')


# In[5]:


# write and string as email
email = '''
Hello Sam,
Please remind me on saturday to prepare for the presentation.
Thank you 
Kindest Regards
'''
print (email)


# In[9]:


# print python using index
exercises = ("Python beginner courses")
print(exercises[3])
# print negative index
print(exercises[-4])


# In[14]:


# more examples on python exercises 
exercises = ("Python beginner courses")
print(exercises[0:9])
# print negative index
print(exercises[1: -6])
print(exercises[1:])
print(exercises[:6])


# In[15]:


exercises = ("Python beginner courses")
print(exercises[1:-4])


# In[2]:


# Formatted Strings Formatted string literals (also called f-strings for short) 
#let you include the value of Python expressions inside a string by prefixing the string with f or 
#F and writing expressions as {expression} .
a = "Namita"
b= "Nabiha"
c = "Rishi"
d = f" {a} {b} {c} are sisters"
print(d)


# In[2]:


#formatted string more examples 
import math
g = "this is the cos of 65 "
e = f"{g} {math.cos(65)}"
print(e)


# In[1]:


user_name = input("please enter your username: ")
email_user = input ("please enter your email: ")
user_info = f"{user_name} Your email is {email_user} and your password is 'PYTONuser702*'"
print(user_info)


# In[2]:


first_user = input ("please enter your first name: ")
last_user = input ("please enter your last name: ")
msg = f"{first_user} [{last_user}]" 
print(msg)


# In[7]:


l = "how r u"
m = "i am fine"
k= l + m
print(k)


# In[1]:


# string method
# length of string 
example1 = "These are very helpful exercises"
print(len(example1))


# In[6]:


#String Mehtods 
Your_full_name ="Namita Fawad"
print (Your_full_name.upper())
print (Your_full_name.lower())
print (Your_full_name.capitalize())


# In[8]:


Your_full_name ="Namita Fawad"
print (Your_full_name.find("a"))


# In[9]:


Your_full_name ="Namita Fawad"
print (Your_full_name.replace("Fawad" , "Fawad Khan"))


# In[11]:


Your_full_name ="Namita Fawad"
print ("Fawad" in Your_full_name)


# In[16]:


Your_full_name ="Namita Fawad"
print (Your_full_name.title())


# In[ ]:





# In[ ]:




