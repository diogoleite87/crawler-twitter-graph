import time
import pandas as pd
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import json

load_dotenv()
browser = webdriver.Chrome()
browser.get("https://twitter.com")
time.sleep(3)

username = browser.find_element(
    By.CLASS_NAME, "r-30o5oe")
username.send_keys(os.getenv("USERNAME"))
time.sleep(3)
username.send_keys(Keys.RETURN)
time.sleep(6)
password = browser.find_element(By.NAME, "password")
password.send_keys(os.getenv("PASSWORD"))
time.sleep(3)
password.send_keys(Keys.RETURN)
time.sleep(3)


def get_followers_you_follow(username):
    browser.get(f'https://twitter.com/{username}/followers_you_follow')

    time.sleep(5)

    span_starting_with_at = []

    for i in range(250):
        browser.execute_script(
            "window.scrollBy(0, 100);")

        html = browser.page_source

        soup = BeautifulSoup(html, "html5lib")

        span_elements = soup.find_all("span")

        for span in span_elements:
            if span.text.startswith("@") and span.text not in span_starting_with_at:
                span_starting_with_at.append(str(span.text))
                print(str(span.text))

        print(len(span_starting_with_at))

    print(span_starting_with_at)

    return span_starting_with_at


def get_following(username):
    browser.get(f'https://twitter.com/{username}/following')

    time.sleep(5)

    span_starting_with_at = []

    for i in range(500):
        browser.execute_script(
            "window.scrollBy(0, 100);")

        html = browser.page_source

        soup = BeautifulSoup(html, "html5lib")

        span_elements = soup.find_all("span")

        for span in span_elements:
            if span.text.startswith("@") and span.text not in span_starting_with_at:
                span_starting_with_at.append(str(span.text))
                print(str(span.text))

        print(len(span_starting_with_at))

    print(span_starting_with_at)

    return span_starting_with_at


def follow_user(username):
    browser.get(f'https://twitter.com/{username}')

    time.sleep(3)

    return


def extract_users():
    result = get_following("userX")

    result_formated = []

    for user in result:
        result_formated.append(user.replace("@", ""))

    print(result_formated)

    list_ids = []

    df = pd.read_csv('./dataID.csv', encoding='utf-8', delimiter=';')

    list_ids = df['ID'].tolist()

    file_router = "ids_list.json"

    final_list = []

    for user in list_ids:
        if user in result_formated:
            final_list.append(user)

    ids_list_json = {
        'ids': final_list
    }

    with open(file_router, "w") as arquivo:
        json.dump(ids_list_json, arquivo, indent=4)


if __name__ == "__main__":

    with open('dataset/ids_list.json', 'r') as arquivo:
        json_ids = json.load(arquivo)

        list_ids = json_ids['ids']

    for user in list_ids:
        followers = get_followers_you_follow(user)

        followers_formated = []

        for aux in followers:
            followers_formated.append(aux.replace("@", ""))

        followers_final = []

        for aux2 in followers_formated:
            if aux2 in list_ids:
                followers_final.append(aux2)

        user_json = {
            'username': user,
            'position': 'teste',
            'color': 'teste',
            'following': [],
            'followers': followers_final
        }

        with open(f'dataset/{user}.json', "w") as arquivo:
            json.dump(user_json, arquivo, indent=4)

    print(list_ids)
    time.sleep(10)
