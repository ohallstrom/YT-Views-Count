'''
File name: generat_csv.py
Author: Oskar Hallström
Date created: 11/10/2021
Date last modified: 11/10/2021
Python Version: 3.8
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

# path to file
PATH = '../raw/original_video_data.csv'
# list of the urls of all videos
URLS = ['https://www.youtube.com/watch?v=y7jMc0eYjf4', 
'https://www.youtube.com/watch?v=PHi-95P_YAk',
'https://www.youtube.com/watch?v=BbFhxh2eJn4',
'https://www.youtube.com/watch?v=spmyWJ_mWMg',
'https://www.youtube.com/watch?v=UKwwYtknZiE',
'https://www.youtube.com/watch?v=qZ12eHriNCY&t=1s',
'https://www.youtube.com/watch?v=V8SZGXPN-YU',
'https://www.youtube.com/watch?v=AQv_760hnvM',
'https://www.youtube.com/watch?v=60Vmx6Usi8M'
]

def get_video_data(urls):
    '''
    Collect title, channel, views affiliated to each url
    using requests and BeautifulSoup
    :param urls: list of urls to videos
    :return data_list: list of dictionaries with data for each url
    '''
    data_list = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        meta_data = soup.body.find('div', class_='watch-main-col')
        names = meta_data.find_all(itemprop = 'name')
        title = names[0].get('content')
        channel = names[1].get('content')
        views = int(meta_data.find(itemprop='interactionCount').get('content'))
        data_list.append({'Title': title,
        'Channel': channel,
        'Views': views, 
        'URL': url})
    return data_list

if __name__ == '__main__':
    # get video data and create a dataframe of it
    video_data = get_video_data(URLS)
    video_df = videos_df = pd.DataFrame(data = video_data, columns = ['Title', 'Channel', 'Views', 'URL'])

    # save dataframe as a csv
    video_df.to_csv(PATH)

