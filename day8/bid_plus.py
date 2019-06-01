# -*- coding: utf-8 -*-
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
     
     

pip install selenium
import pandas as pd
from selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:\Users\Kapil Patidar\Desktop\Application/chromedriver_win32/chromedriver.exe")
