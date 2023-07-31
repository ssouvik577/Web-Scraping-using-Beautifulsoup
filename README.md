# Web-Scraping-using-Beautifulsoup
This code is a Python script that fetches data from the "Hacker News" website (https://news.ycombinator.com/) and extracts information about the top news articles based on their votes (points). It uses the requests library to make HTTP requests and the BeautifulSoup library to parse and extract data from the HTML pages.

Let's go through the code step by step:

Importing required libraries:

requests: Used for making HTTP requests to the web pages.
BeautifulSoup: Used to parse the HTML content and extract information from it.
pprint: Used for pretty-printing the output.
Making HTTP requests:

The script uses the requests.get() method to fetch the content of two pages: the main page and page 2 of "Hacker News."
The page variable holds the response for the main page, and the page2 variable holds the response for page 2.
Parsing HTML with BeautifulSoup:

The BeautifulSoup class is used to parse the HTML content of the pages fetched in the previous step.
The soup variable holds the parsed content of the main page, and the soup2 variable holds the parsed content of page 2.
Selecting elements from the page:

The script uses CSS selectors to extract specific elements from the HTML pages.
The soup.select() method is used to select all elements with the class "titleline" (which are the news article titles) and store them in the links and links2 variables for both pages.
Similarly, the soup.select() method is used to select all elements with the class "subtext" (which contain the article metadata, including votes/points) and store them in the subtext and subtext2 variables for both pages.
Merging the data from both pages:

The script combines the links and subtext from both pages into two new lists: mega_links and mega_subtext.
Defining helper functions:

The script defines two functions: sort_stories_by_votes() and create_custom_hackernews().
The sort_stories_by_votes() function takes a list of Hacker News articles and sorts them based on their vote/points in descending order.
The create_custom_hackernews() function processes the list of article links and metadata (subtext) and returns a list of dictionaries containing information about the articles that have more than 99 points.
Processing and filtering the data:

The create_custom_hackernews() function is called with the mega_links and mega_subtext lists as arguments to process and filter the data.
For each news article, the function extracts its title and URL from the links list and calculates the number of points from the subtext list.
If an article has more than 99 points, it is added to the hackernews list as a dictionary with keys: 'title', 'link', and 'vote'.
Finally, the sort_stories_by_votes() function is called to sort the filtered articles by their vote/points in descending order.
Printing the results:

The pprint.pprint() function is used to pretty-print the resulting list of articles with their titles, links, and votes/points.
