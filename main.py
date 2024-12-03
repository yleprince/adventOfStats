import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data(year: int):
    url = f"https://adventofcode.com/{year}/stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    pre = soup.find('pre', class_='stats')
    a_ = pre.extract().find_all('a')
    columns = ("day", "both", "first")
    texts = [{k:v for k, v in zip(columns, a.text.strip().split())} for a in a_]
    df = pd.DataFrame(texts)
    df["year"] = year
    return df


if __name__ == '__main__':
    df = pd.DataFrame()
    for year in range(2015, 2025):
        print("processing year: ", year, end="\r")
        data = get_data(year)
        df = pd.concat([df, data], ignore_index=True)
    df.to_csv("/tmp/advent_of_code.csv", index=False)
