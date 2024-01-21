from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
import pandas as pd
import pickle

def fetch_reviews_for_platform(url, platform, driver):
    link = url + f"/{platform}"
    print(link)
    driver.get(link)

    time.sleep(3)
    previous_height = driver.execute_script('return document.body.scrollHeight')

    for i in range(2):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height

    return driver.page_source

def extract_reviews(page):
    parsed_page = soup(page, 'html.parser')
    reviews = []

    games = parsed_page.find_all('div', attrs={'class':'content-item jsx-1409608325 row divider'})
    print(str(len(games)) + ' review links have been added to the main review list')
    for game in games:
        title = game.find("span", attrs={"class":"interface jsx-777404155 item-title bold"}).get_text().strip()
        link = "https://www.ign.com" + game.find("a", attrs={"class":"item-body"}).get('href')
        date = game.find('div', attrs={'class':'interface jsx-153568585 jsx-957202555 item-subtitle small'}).get_text().strip().split("-")[0]
        rating = game.find('span', attrs={'class':'hexagon-content-wrapper'}).get_text().strip()
        author = game.find('object', attrs={'class':'caption jsx-1541923331 data small', 'title': 'Author Link'}).get_text().strip()
        reviews.append((title, link, date, rating, author))
    print('Main review list has been updated with key information appended')
    return reviews


def create_dataframes_for_platforms(link, platforms):
    driver = webdriver.Chrome()
    dataframes = {}

    for platform in platforms:
        time.sleep(5)
        page_content = fetch_reviews_for_platform(link, platform, driver)
        reviews = extract_reviews(page_content)
        reviews = [(title, link, date, rating, author, platform) for title, link, date, rating, author in reviews]
        # Create a dataframe for each platform's reviews
        df = pd.DataFrame(reviews, columns=['Title', 'Link', 'Date', 'Rating', 'Author', 'Platform'])
        dataframes[platform] = df

    driver.quit()
    return dataframes


if __name__ == "__main__":

    platforms_list = ["ps3", "ps4", "ps5", "xbox-360", "xbox-one", "xbox-4", "nintendo-switch", "wii", "pc"]

    ign_games_link = "https://www.ign.com/reviews/games"

    result_dataframes = create_dataframes_for_platforms(ign_games_link, platforms_list)

    for platform, dataframe in result_dataframes.items():
        print(f"Reviews for {platform}:")
        print(dataframe)

    with open('result_dataframes.pkl', 'wb') as file:
        pickle.dump(result_dataframes, file)