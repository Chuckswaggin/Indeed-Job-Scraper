# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:15:11 2019

@author: Nicholas
"""

import requests
import bs4

html = requests.get('https://www.indeed.com/jobs?q=Computer+Science&l=Houston%2C+TX&explvl=entry_level&sort=date')
html.raise_for_status()

soup = bs4.BeautifulSoup(html.text, 'lxml')
jobs = soup.select('a[class=jobtitle\ turnstileLink\ ]')
companies = soup.select('span[class=company]')

for i in range(len(jobs)):
    print(jobs[i].get_text().strip())
    print(companies[i].get_text().strip())
    print()