'''
takes in CSV of column of wiki urls

outputs csv with the following columns

URL | Title | |Views

'''
# import libraries
#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import math
import datetime
import time
import requests
import json
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from collections import defaultdict
import statsmodels.api as sm
from bs4 import BeautifulSoup

# Import list of URLs
input_path = 'input/urls.csv'

urls = pd.read_csv(input_path)
rows = []
url_list = urls.values

for url in url_list:
	print('scraping ', url[0])
	#
	info_dict = {}
	req = requests.get(url[0])
	soup = BeautifulSoup(req.text, "html.parser")

	#
	attributes = soup.find_all('div', {'class':'sp_text'})
	title = soup.find('h1', {'class':'title_md','id':'section_0'}).get_text()
	info_dict['Title'] = title
	info_dict['Url'] = url

	for i in attributes:
		info = i.get_text()
		info = info.split(':')
		info[0] = info[0].strip()
		info[1] = info[1].strip()
		if info[0] == 'Views':
			info_dict[info[0]] = float(info[1].replace(',',''))

	rows.append(info_dict)


results_db = pd.DataFrame.from_dict(rows, orient='columns')
print(results_db)
results_db.to_csv('output/return_table.csv')