#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


election_file = "/Users/kerimason/Desktop/pythonchallenge/PyPoll/election_data.csv"


# In[3]:


election_file_pd = pd.read_csv(election_file)
election_file_pd.head()


# In[4]:


#The total number of votes cast
unique = election_file_pd["Voter ID"].unique()
unique


# In[5]:


voter_count = election_file_pd["Voter ID"].value_counts()
voter_count


# In[6]:


#A complete list of candidates who received votes
candidate_votes_df = election_file_pd
candidate_votes_df.head()


# In[7]:


#A complete list of candidates who received votes
candidate_votes_df = candidate_votes_df.dropna(how = "any")
candidate_votes_df.head()


# In[8]:


#check work that zero were removed
candidate_votes_df["Voter ID"].values.min()


# In[9]:


#List of candidates who received votes
candidate_votes_df["Candidate"].unique()


# In[ ]:


#The percentage of votes each candidate won
#candidate_count = len(candidate_votes_df["Candidate"].value_counts())
#candidate_count


# In[24]:


candidate_count=candidate_votes_df["Candidate"].value_counts()
candidate_count


# In[27]:


#Total vote casts
candidate_percentages= (candidate_count.values / len(voter_count))
candidate_percentages


# In[33]:


summary_table = [(candidate_count, candidate_percentages)]
summary_table


# In[39]:


summary_table = [(candidate_count , candidate_percentages)]
summary_table


# In[41]:


df = pd.DataFrame(candidate_count)
df


# In[42]:


df["Percents"] = candidate_percentages


# In[43]:


df


# In[48]:


winner = df[df["Percents"] > .50]
winner


# In[ ]:




