# import numpy as np
import time
from time import sleep
import requests
from bs4 import BeautifulSoup

from medium.models import Article


def find_article():
    url='https://medium.com/blockchain'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    stories = soup.find_all('div', {'class':['col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size6of12','col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12']})
    # print(stories)
    # sleep(np.random.randint(1, 15))
    for story in stories:
        title=story.find('h3').text if story.find('h3') else '-'
        # print(title)
        description=story.find('div',{'class':'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}).text if story.find('div',{'class':'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}) else '-'
        # print(describtion)
        # sleep(np.random.randint(1, 15))
        slug=story.find('a')['href'].split('/')[-1]
        created_at = story.find('time')['datetime']
        # print(slug)
        # author=story.find('a',{'class':'ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken'})['href'].split('@')[-1]
        # print(author)
        story_url=story.find('a')['href']
        # print(story_url)
        story_page = requests.get(story_url)
        story_soup = BeautifulSoup(story_page.text, 'html.parser')
        sections = story_soup.find_all('section')
        for section in sections:
            # print(section)
            if section.find('p'):
                paragraphs=section.find_all('p')
                # print(paragraphs)
                body=''
                for paragraph in paragraphs:
                    body+=paragraph.get_text()
                    # print(body)
        # tags = story_soup.find_all('li',{'class':'gd by gs me'})
        # images_url=story_soup.find_all('div',{'class':'di dj s'})
        # sleep(np.random.randint(1, 15))
        Article.objects.create(
            slug=slug,
            title=title,
            description=description,
            body=body,
            created_at=created_at,
        )
        # for tag in tags:
        #     story_tag=tag.find('a').text if tag.find('a') else '-'
        #     # print(story_tag)
        #     # sleep(np.random.randint(1, 15))
        # for image_url in images_url:
        #     image=image_url.find('img',{'class':'t u v dc aj'})['src'] if image_url.find('img',{'class':'t u v dc aj'}) else '-'
        #     # print(image)
        #     data = requests.get(image)  # read image
        #     photo = data.content
        #     # print(photo)
        #     # print('ok')
if __name__ == '__main__':
    while True:
        find_article()
        time_wait = 3600
        time.sleep(time_wait * 24)