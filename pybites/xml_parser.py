import xml.etree.ElementTree as ElementTree
import requests

rss_feed = "https://alexos.dev/index.xml"
response = requests.get(rss_feed)

tree = ElementTree.fromstring(response.content)

titles = (e.text for e in tree.findall("./channel/item/title"))

first_five = list(titles)[:5]
print(*first_five, sep='\n')
