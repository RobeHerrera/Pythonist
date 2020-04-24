#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_list = [10,20,30,40,50]


# In[2]:


def main():
    count = 0
    total = 0
    for i in num_list:
        count = count + 1
        total = total + i
        
        print("element is: ",i)
        print("")
        print("sum: ", total)
        print("")
    print("total sum:", total)


# In[4]:


if __name__=="__main__":
    main()


# In[ ]:




