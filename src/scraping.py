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
    head = ['country', 'year', 'population', 'yearly change (%)', 'yearly change', 'migrants (net)', 'median age', 'fertility rate', 'density (p/km2)', 'urban population (%)', 'urban population', "country's shared of world population", 'world population', 'rank']

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
    csv_file = open('./data/population/' + country + '-population.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    for data_list in data:
        writer.writerow(data_list)
    csv_file.close()

    ## Getting the forecast data
    tbody = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[8]/table/tbody')

    data = []
    head = ['country', 'year', 'population', 'yearly change (%)', 'yearly change', 'migrants (net)', 'median age', 'fertility rate', 'density (p/km2)', 'urban population (%)', 'urban population', "country's shared of world population", 'world population', 'rank']
    data.append(head)

    for r in tbody.find_elements(By.XPATH,'./tr'):
        row = []
        row.append(re.sub('-', ' ', country.title()))
        for c in r.find_elements(By.XPATH,'./td'):
            no_commas_string = re.sub(',', '', c.text)
            row.append(no_commas_string)
            
        data.append(row)

    ## Pass data into a csv file
    csv_file = open('./data/forecast/' + country + '-forecast.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    for data_list in data:
        writer.writerow(data_list)
    csv_file.close()