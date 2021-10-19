'''
File name: update_csv.py
Author: Oskar Hallström
Date created: 11/10/2021
Date last modified: 11/10/2021
Python Version: 3.8
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

# path to file
READ_PATH = '../raw/original_video_data.csv'
WRITE_PATH = '../generated/updated_video_data.csv'

def get_views(url):
    '''
    Gets the views of the url
    :param url: url to get views from
    :return views: number of views for url
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    meta_data = soup.body.find('div', class_='watch-main-col')
    views = int(meta_data.find(itemprop='interactionCount').get('content'))
    return views

def get_updated_views(df_col):
    '''
    Collect updated number of views affiliated to each url
    using requests and BeautifulSoup
    :param df_col: column of urls
    :return views_col: column of updated views
    '''
    views_col = df_col.apply(lambda url: get_views(url))
    return views_col

def main():
    '''
    Main function. Created so that visualise.ipynb
    can do the equivalent to run this file.
    '''
    # get original video data
    video_data = pd.read_csv(READ_PATH)

    # update number of views
    video_data['Views'] = get_updated_views(video_data['URL'])

    # save dataframe as a csv
    video_data.to_csv(WRITE_PATH, index = False)


if __name__ == '__main__':
    main()
