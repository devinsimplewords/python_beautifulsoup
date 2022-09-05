from bs4 import BeautifulSoup

with open(r"html_file/simple_file.html") as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

print("The soup: \n{}".format(soup))
print("\nThe <p> element with its attributes: \n{}\n{}".format(soup.p, soup.p.attrs))
print("\nThe <h1> element with its attributes: \n{}\n{}".format(soup.h1, soup.h1.attrs))
