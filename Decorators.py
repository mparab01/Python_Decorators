
# coding: utf-8

# Decorators:
# Decorators can be thought of as functions which modify the functionality of another function. They help to make the code shorter and more pythonic.

# FUNCTIONS AS ARGUMENTS

# In[5]:

def hello():
    return 'Hello Milind'


# In[6]:

def other(func):
    print 'I am in the other function'
    print func()


# In[7]:

other(hello)


# FUNCTIONS WITHIN FUNCTIONS

# In[14]:

def hello (name='Milind'):
    print 'The hello() funcion has been executed'
    
    def greet():
        return '\t this is inside the greet function'
    
    def welcome():
        return '\t this is inside welcome function'
    
    print greet()
    print welcome()
    
    if name == 'Milind':
        return greet
    else:
        return welcome


# In[15]:

x = hello()


# In[16]:

x


# In[17]:

print x()


# In[ ]:



