from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import mail
from tkinter import messagebox, IntVar
import pymysql
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta

import os
while True:
    try:
        con = pymysql.connect(host='localhost', user='root', password='Minnu%1122')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error', 'Connection error')
    query = 'use userdata'
    mycursor.execute(query)
    query = 'select max(id) from data ;'
    a = mycursor.execute(query)
    row = mycursor.fetchone()
    for n in row:
        n1 = n
        break


    while(n1>=1):
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from details where id=%s;'
        a = mycursor.execute(query,(n1))
        row = mycursor.fetchone()

        while row==None:
            n1=n1-1
            query = 'use userdata'
            mycursor.execute(query)
            query = 'select * from details where id=%s;'
            a = mycursor.execute(query, (n1))
            row = mycursor.fetchone()

        jt=row[1]
        l=row[2]

        Job_data = []
        df = pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Rating':[''] , 'Location':[''] , 'Salary':[''], 'Date':['']})


        driver = webdriver.Chrome()
        options = Options()
        options.add_argument("--headless=new")
        driver=webdriver.Chrome(options=options)
        driver.get('https://in.indeed.com/')
        time.sleep(2)


        what = driver.find_element("xpath", '//*[@id="text-input-what"]')
        what.send_keys(f'{jt}')


        where = driver.find_element("xpath", '//*[@id="text-input-where"]')
        where.send_keys(f'{l}')


        driver.find_element("xpath", '//*[@id="jobsearch"]/button').click()
        time.sleep(2)

        driver.find_element("xpath", '//*[@id="filter-dateposted"]').click();
        driver.find_element("xpath", '//*[@id="filter-dateposted-menu"]/li[3]/a').click()

        while True:

            soup = BeautifulSoup(driver.page_source, 'lxml')


            postings = soup.find_all('div', class_='job_seen_beacon')
            for post in postings:

                link = post.find('a', class_='jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
                link_full = 'https://in.indeed.com' + link

                try:
                    name = post.find('h2', class_='jobTitle css-1h4a4n5 eu4oa1w0').text.strip()
                except:
                    name = post.find('h2', class_='jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0').text.strip()

                company = post.find('span', class_='companyName').text.strip()

                try:
                    salary = post.find('div', class_='metadata salary-snippet-container').text
                except:
                    salary = 'N/A'

                try:
                    location = post.find('div', class_='companyLocation').text
                except:
                    location = "N/A"

                try:
                    rating = post.find('span', class_='ratingNumber').text
                except:
                    rating = "N/A"

                date = post.find('span', class_='date').text


                data = {'Link': link_full, 'Job Title': name, 'Company': company, 'Rating': rating, 'Location': location,
                     'Salary': salary, 'Date': date}
                Job_data.append(data)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            try:
                button = soup.find('a', attrs={'aria-label': 'Next Page'}).get('href')
                driver.get('https://in.indeed.com' + button)
            except:
                break
        df = pd.DataFrame(Job_data)

        NaukriJob_data = []
        df1 = pd.DataFrame(
            {'Link': [''], 'Job Title': [''], 'Company': [''], 'Rating': [''], 'Location': [''], 'Salary': [''],
             'Date': ['']})

        driver = webdriver.Chrome()
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.naukri.com/')
        time.sleep(2)


        inputs = driver.find_elements(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
        for input in inputs:
            input.send_keys(f'{jt}')


        locations = driver.find_elements(By.XPATH, '//*[@id="root"]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
        for location in locations:
            location.send_keys(f'{l}')


        driver.find_element(By.CLASS_NAME, 'qsbSubmit').click()
        time.sleep(2)


        while True:

            soup = BeautifulSoup(driver.page_source, 'lxml')


            postings = soup.find_all('article', class_='jobTuple')
            for post in postings:


                link = post.find('a', class_='title ellipsis').get('href')
                link_full = 'https://www.naukri.com/' + link


                try:
                    name = post.find('div', class_='jobTupleHeader').text.strip()
                except:
                    name = post.find('div', class_='info fleft').text.strip()

                company = post.find('div', class_='companyInfo subheading').text.strip()

                try:
                    salary = post.find('span', class_='ellipsis fleft').text
                except:
                    salary = 'N/A'

                try:
                    location = post.find('span', class_='ellipsis fleft locWdth').text
                except:
                    location = "N/A"

                try:
                    rating = post.find('a', class_='reviewsCount fleft').text
                except:
                    rating = "N/A"


                def parse_job_date(date_string):
                    date_string = date_string.strip().lower()
                    now = datetime.now()
                    if date_string == 'just now':
                        return now
                    elif date_string == 'today':
                        return now - timedelta(days=0)
                    elif date_string == '1 day ago':
                        return now - timedelta(days=1)
                    elif 'days ago' in date_string:
                        days_str = date_string.split()[0]
                        if days_str.endswith('+'):
                            days = int(days_str[:-1])
                        else:
                            days = int(days_str)
                        if days <= 7:
                            return now - timedelta(days=days)
                    elif 'few hours ago' in date_string:
                        return now - timedelta(hours=1)
                    else:
                        return None



                date = post.find('span', class_='fleft postedDate').text
                job_date = parse_job_date(date)


                if job_date is not None:
                    days_diff = (datetime.now() - job_date).days
                    data = {'Link': link_full, 'Job Title': name, 'Company': company, 'Rating': rating,
                            'Location': location,
                            'Salary': salary, 'Date': days_diff}
                    NaukriJob_data.append(data)



            try:

                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.fright.fs14.btn-secondary.br2')))


                next_button.click()


                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.row')))


            except:

                break
        df1 = pd.DataFrame(NaukriJob_data)

        frame=[df,df1]
        df2=pd.concat(frame)
        df2.to_excel('Vacancies.xlsx',encoding='utf-8')
        mail.send(n1)
        os.remove(r'C:\Users\minnu\PycharmProjects\MiniPro\Vacancies.xlsx')
        n1=n1-1
    time.sleep(7 * 24 * 60 * 60)

