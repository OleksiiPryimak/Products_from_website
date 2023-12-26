# python (lokation)/Products_from_website.py "website" "xpath"
# for example:
# python (lokation)/Products_from_website.py "https://www.castorama.pl/produkty/urzadzanie/wyposazenie-kuchenne/zlewozmywaki.html" "//*[@id='categoryMainContent']/div/section/div/div/section/section/h3"

import click
from lxml import html
import requests

# division into two functions - main and extract. To make testing easier - extract.

def extract(page_content, xpath):
    """Accepts page_content and xpath as a string and returns matching elements as a list of strings"""

    tree = html.fromstring(page_content)
    elements = tree.xpath(xpath)
    elements = [e.text_content() for e in elements]
    stripped = [e.strip().replace('\n', ' ') for e in elements]
    return stripped


@click.command()
@click.argument('url')
@click.argument('xpath')
def main(url, xpath):

    page = requests.get(url)
    content = page.text
    elements = extract(content, xpath)
    for element in elements:
        print(element)


if __name__ == "__main__":
    main()