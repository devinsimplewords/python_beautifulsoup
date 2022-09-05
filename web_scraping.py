from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://en.wikipedia.org/wiki/%22Hello,_World!%22_program")
soup = BeautifulSoup(response.text, "html.parser")

# Finding the main title tag.
title = soup.find("h1", class_="firstHeading")
print("Title of the page: {}".format(title.get_text()))

print("\nList of chapters and links:")
chapters_list = soup.find_all("h2")
for chapter in chapters_list:
    chapter_text = chapter.get_text()
    chapter_link = chapter.a
    if chapter_link:
        chapter_href = chapter.a.get("href")
    else:
        chapter_href = ""
    print(chapter_text, chapter_href)

print("\nList of sections and links:")
sections_list = soup.find_all("h3")
for section in sections_list:
    section_text = section.get_text()
    section_link = section.a
    if section_link:
        section_href = section.a.get("href")
    else:
        section_href = ""
    print(section_text, section_href)
