# Web-Scraper
## Simple web scraping python script using BeautifulSoup

Python-based Web Scraper script

Python script that scrapes https://www.futurelearn.com/ website. It scrapes information such as University name, Course Title, Course Description, Duration, Effort, Cost of 476 total courses.

Language: Python
Libraries: Beautiful Soup.

Input: Website url
Output: Json Data

record={
         'University':university,
         'Title':title,
         'Description':desc,
         'Duration':dur,
         'Effort':eff,
         'Cost':price
         }  

Sample output:
[{"University": "University of Basel", "Title": "Allergies: When the Immune System Backfires", "Description": "What do allergies reveal about our immune system's capabilities? Learn more about allergy symptoms and treatments on this course.", "Duration": "3 weeks", "Effort": "4 hrs per week", "Cost": "Included in Unlimited"},

