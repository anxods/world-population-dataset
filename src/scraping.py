from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import re

def get_country_data(country, url):
    driver = webdriver.Chrome()
    driver.get(url)

    data = []

    ## Getting the headers
    thead = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[5]/table/thead')

    head = ['country']

    for r in thead.find_elements(By.XPATH, './tr'):
        row = []
        for c in r.find_elements(By.XPATH, './th'):
            inner_html = c.get_attribute('innerHTML')
            new_string = re.sub('<br>|<span.*?>|</span>', ' ', inner_html)
            head.append(new_string)

    head = [('Rank') if "Rank" in item or "rank" in item else item for item in head]

    data.append(head)

    ## Getting the historical data
    tbody = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[5]/table/tbody')

    for r in tbody.find_elements(By.XPATH,'./tr'):
        row = []
        row.append(re.sub('-', ' ', country.title()))
        for c in r.find_elements(By.XPATH,'./td'):
            no_commas_string = re.sub(',', '', c.text)
            row.append(no_commas_string)
            
        data.append(row)

    ## Pass data into a csv file
    csv_file = open('./data/population/countries/' + country + '-population.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    for data_list in data:
        writer.writerow(data_list)
    csv_file.close()

    ## Getting the forecast data
    tbody = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[8]/table/tbody')

    data = []

    ## Getting the headers
    thead = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[8]/table/thead')

    head = ['country']

    for r in thead.find_elements(By.XPATH, './tr'):
        row = []
        for c in r.find_elements(By.XPATH, './th'):
            inner_html = c.get_attribute('innerHTML')
            new_string = re.sub('<br>|<span.*?>|</span>', ' ', inner_html)
            head.append(new_string)

    head = [('Rank') if "Rank" in item or "rank" in item else item for item in head]

    data.append(head)

    for r in tbody.find_elements(By.XPATH,'./tr'):
        row = []
        row.append(re.sub('-', ' ', country.title()))
        for c in r.find_elements(By.XPATH,'./td'):
            no_commas_string = re.sub(',', '', c.text)
            row.append(no_commas_string)
            
        data.append(row)

    ## Pass data into a csv file
    csv_file = open('./data/forecast/countries/' + country + '-forecast.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    for data_list in data:
        writer.writerow(data_list)
    csv_file.close()