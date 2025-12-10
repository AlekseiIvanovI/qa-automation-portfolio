from bs4 import BeautifulSoup
import requests

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
# print(type(questions[0]))
# print(questions[0])
print(questions[0].attrs)
# print(questions[0].select(".s-link"))
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(
        ".s-post-summary--stats-item__emphasized span").getText())
# print(questions[0].select_one(".s-link").getText())
