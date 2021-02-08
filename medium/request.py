# import numpy as np
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User

from medium.models import Article


def find_article():
    url = 'https://medium.com/blockchain'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    stories = soup.find_all('div', {'class': [
        'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size6of12',
        'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12']})
    # sleep(np.random.randint(1, 15))
    for story in stories:
        title = story.find('h3').text if story.find('h3') else '-'
        description = story.find('div', {
            'class': 'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}).text if story.find(
            'div', {
                'class': 'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}) else '-'
        # sleep(np.random.randint(1, 15))
        slug = story.find('a')['href'].split('/')[-1]
        created_at = story.find('time')['datetime']
        # print(slug)
        author=story.find('a',{'class':'ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken'}).text
        # print(author)
        story_url = story.find('a')['href']
        # print(story_url)
        story_page = requests.get(story_url)
        story_soup = BeautifulSoup(story_page.text, 'html.parser')
        sections = story_soup.find_all('section')
        # tag_item = story_soup.find_all('ul',{'class':'bg bh'})
        # print(tag_item)
        # for tag in tag_item:
        #     tagg=tag.find_all('li')
        #     tagss=''
        #     for i in tagg:
        #         tagss=tagss+i.text+','
        #         tags=tagss[:-1]
        # print(tags)
        images_url = story_soup.find_all('div', {'class': 'di dj s'})
        for image_url in images_url:
            image = image_url.find('img', {'class': 't u v dc aj'})['src'] if image_url.find('img', {
                'class': 't u v dc aj'}) else '-'
            # print(image)
        for section in sections:
            # print(section)
            if section.find('p'):
                paragraphs = section.find_all('p')
                # print(paragraphs)
                body = ''
                for paragraph in paragraphs:
                    body += paragraph.get_text()
                    # print(body)
        # tags = story_soup.find_all('li',{'class':'gd by gs me'})
        # images_url=story_soup.find_all('div',{'class':'di dj s'})
        # sleep(np.random.randint(1, 15))
        # obj = Article.objects.get()
        # user=obj.author
        user=User(username=author)
        user.save()
        Article.objects.create(
            title=title,
            description=description,
            slug=slug,
            created_at=created_at,
            author=author,
            image=image,
            body=body,
            # tags=tags,
        )

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
