#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Addition

a=int(input("enter the value for a :"));
b=int(input("enter the value for b :"));
sum = a+b;
print("sum : ", sum)


# In[2]:


#Subtraction

a=int(input("enter the value for a :"));
b=int(input("enter the value for b :"));
sub=a-b;
print("sub : ",sub)


# In[3]:


#Multiplication

a=int(input("enter the value for a :"));
b=int(input("enter the value for b :"));
multi=a*b;
print("multi : ",multi)


# In[4]:


#Division

a=float(input("enter the value for a :"));
b=float(input("enter the value for b :"));
div=float(a/b);
print("div : ",div)


# In[5]:


#Module

a=int(input("enter the value for a :"));
b=int(input("enter the value for b :"));
mod=float(a%b);
print("mod : ",mod)


# In[6]:


#Exponent

a=int(input("enter the value for a :"));
b=int(input("enter the value for b :"));
exp=a**b;
print("exp : ",exp)


# In[7]:


#Floor division

a=float(input("enter the value for a :"));
b=float(input("enter the value for b :"));
c=(a//b);
print("the value of c is :",c)


# In[8]:


#Simple Interest

principal=float(input("enter the principal value :"))
time_period=float(input("enter the timeperiod value :"))
rate=float(input("enter the rate value :"))
interest=(principal*time_period*rate)/100
print("interest :",interest)


# In[9]:


#Area of circle

PI=3.14
r=float(input("enter the radius of the circle :"))
area= PI*r*r;
print("Area of the circle is :",area)


# In[10]:


#Area of triangle

b=float(input("enter the base value :"))
h=float(input("enter the height value :"))
area=1/2*b*h;
print("Area of the triangle is :",area)


# In[11]:


#Celsius to Faherenheit

c=float(input("enter the celsius value :"))
output=(c*1.8)+32;
print("The converted value in fahrenheit is :",output)


# In[12]:


#Area of Rectangle

w=float(input("enter the width value :"))
h=float(input("enter the height value :"))
area=w*h;
print("Area of the rectangle is :",area)


# In[13]:


#Perimeter of a square

a=float(input("enter the length of the side value:"))
p=4*a;
print("Perimeter of the square is :",p)


# In[14]:


#Circumference of circle

PI=3.14
r=float(input("enter the radius of the circle :"))
c= 2*PI*r;
print("Circumference of the circle is :",c)


# In[18]:


#Swap two numbers

a=int(input("enter the value for a :"))
b=int(input("enter the value for b :"))
temp=0;
temp=a;
a=b;
b=temp;
print("the value of a after swapping :",a)
print("the value of b after swapping :",b)

