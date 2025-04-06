import requests
from bs4 import BeautifulSoup
import random

class ContentSpark:
    def __init__(self):
        self.trending_topics = []
        self.user_niches = []

    def scrape_google_trends(self):
        url = "https://trends.google.com/trends/trendingsearches/daily?geo=US"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        topics = soup.find_all('div', class_='details-top')
        self.trending_topics = [topic.find('a').text for topic in topics]

    def scrape_twitter_trends(self):
        url = "https://twitter.com/explore/tabs/trending"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        trends = soup.find_all('span', class_='TrendName')
        self.trending_topics = [trend.text for trend in trends]

    def set_user_niches(self, niches):
        self.user_niches = niches

    def generate_content_ideas(self):
        if not self.trending_topics or not self.user_niches:
            return []

        content_ideas = []
        for topic in self.trending_topics:
            for niche in self.user_niches:
                idea = f"Explore the impact of {topic} on {niche}"
                content_ideas.append(idea)

        return content_ideas

    def run(self, niches, source='google'):
        self.set_user_niches(niches)
        if source == 'google':
            self.scrape_google_trends()
        elif source == 'twitter':
            self.scrape_twitter_trends()
        
        content_ideas = self.generate_content_ideas()
        return content_ideas

if __name__ == "__main__":
    spark = ContentSpark()
    niches = ["technology", "health", "finance"]
    ideas = spark.run(niches, source='google')
    for idea in ideas:
        print(idea)