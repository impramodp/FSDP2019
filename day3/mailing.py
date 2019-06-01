"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
l  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      
"""
# -*- coding: utf-8 -*-

