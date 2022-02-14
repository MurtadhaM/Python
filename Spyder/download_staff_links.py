from html.parser import HTMLParser
from urllib import parse



rl= "view-source:https://pages.charlotte.edu/connections/links/capabilities-agility/"
staff_links = []



def handle_starttag():
    tag = 'a'
    attrs = 'href'
    if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(base_url, value)
                    staff_links.add(url)

    
    return links