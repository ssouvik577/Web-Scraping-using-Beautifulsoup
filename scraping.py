# =======================Importing required libraries====================
import requests
from bs4 import BeautifulSoup
import pprint
# ========================================================================

# ========================Making HTTP requests============================
page = requests.get("https://news.ycombinator.com/")
page2 = requests.get("https://news.ycombinator.com/?p=2")
# ========================================================================

# =====================Parsing HTML with BeautifulSoup====================
soup = BeautifulSoup(page.text, "html.parser")
soup2 = BeautifulSoup(page2.text, "html.parser")
# ========================================================================

# ===================Selecting elements from the page=====================
links = soup.select('.titleline')
links2 = soup2.select('.titleline')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
# ========================================================================

# ====================Merging the data from both pages====================
mega_links = links + links2
mega_subtext = subtext + subtext2
# ========================================================================

# ======================Defining helper functions=========================
#filtering the HTML into text only
def sort_stories_by_votes(hackernews_list):
    return sorted(hackernews_list, key=lambda key:key['vote'], reverse=True)
# ====================Processing and filtering the data===================
def create_custom_hackernews(links, subtext):
    hackernews = []
    for index, i in enumerate(links):  #To get both the index and the value of each element
        title = links[index].getText()
        href = links[index].find('a')['href']
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hackernews.append({'title' : title, 'link' : href, 'vote' : points})
    return sort_stories_by_votes(hackernews)
# ========================================================================

# ====================Printing the results================================
pprint.pprint(create_custom_hackernews(mega_links, mega_subtext))


