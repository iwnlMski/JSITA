import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from db_utils import offer_not_id_db, add_to_db


def initialize_chrome_driver():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    return webdriver.Chrome(options=op)


def get_response_from_url(url):
    return requests.get(url)


def generate_offers_from_response(response):
    for offer in response.text.split('</entry>')[0:-1]:
        yield offer + '</entry>'


def get_skill_and_exp_from_url(url, driver):
    driver.get(url)
    skill_set_soup = BeautifulSoup(driver.page_source, 'html.parser')
    skills_list = [x['title'] for x in skill_set_soup.find_all(attrs={'class': 'css-1xm32e0'})]
    experience = skill_set_soup.find_all(attrs={'class': 'css-1ji7bvd'})[1].text
    return {'skills': skills_list, 'exp': experience}


def limit_update_check():
    for limit in range(101):
        yield limit


def update_database_with_offers(splitted_response, driver):
    limit = limit_update_check()
    for offer in splitted_response:
        soup = BeautifulSoup(offer, 'html.parser')
        if offer_not_id_db(soup.entry.id.text.strip()):
            summary_soup = BeautifulSoup(soup.summary.text, 'html.parser')
            skills_exp_dict = get_skill_and_exp_from_url(soup.entry.id.text.strip(), driver)
            skills = ', '.join(skills_exp_dict['skills'])
            exp = skills_exp_dict['exp']
            data = {
                'url': soup.entry.id.text.strip(),
                'name': soup.entry.title.text.strip(),
                'location': summary_soup.p.text.strip().splitlines()[1],
                'company': soup.entry.author.text.strip(),
                'salary': summary_soup.p.text.strip().splitlines()[0],
                'skills': skills,
                'date': soup.entry.updated.text,
                'exp': exp,
            }
            add_to_db(data)
        else:
            try:
                next(limit)
            except StopIteration:
                break
    return print('Done updating')


