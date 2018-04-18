#! /usr/bin/env python3
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium import common
import datetime
import sys
import csv
import json

def main():
  if len(sys.argv) > 1 and sys.argv[1] == "json":
    scrap('json')
  else:
    scrap('csv')

def scrap(output_format):
  date_string = '{}-{}-{}'.format(date.day,date.month-1,date.year)
  xPath_Price = '//td[@id="c-'+date_string+'"]//span[contains(text(),"$")]'
  date = datetime.datetime.today()
  delta_1_day = datetime.timedelta(days=1)
  current_month = date.month
  current_year = date.year
  price_list = []
  with Display():
    while not(date.month == current_month and date.year >
    current_year):
      try:
        driver = webdriver.Firefox()
        driver.get('https://www.signaturemgmgrand.com/en/booking/room-booking.html#/step1&arrive=2018-04-11&depart=2018-04-12&numGuests=2')
        price = driver.find_element_by_xpath(xPath_Price).text
      except common.exceptions.NoSuchElementException:
        price = "unavailable"
      finally:
        driver.quit()
    price_list.append([date.strftime('%Y-%m-%d'),price])
    date = date + delta_1_day
  if output_format == 'json':
    write_json(price_list)
  elif output_format == 'csv':
    write_csv(price_list)
  else:
    return json.JSONEncoder().encode(price_list)

def write_csv(data):
  with open(datetime.datetime.today().strftime('%Y-%m-%d')+'.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

def write_json(data):
  json_encoded = json.JSONEncoder().encode(data)
  with open(datetime.datetime.today().strftime('%Y-%m-%d')+'.json','w') as \
  jsonfile:
    for line in json_encoded:
      jsonfile.write(line)

if __name__ == "__main__":
  main()
