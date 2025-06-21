import requests
from bs4 import BeautifulSoup

url = "https://minecraft.wiki/w/Bedrock_Dedicated_Server"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

release_ver = None
preview_ver = None

for link in soup.find_all('a'):
    if 'Bedrock Dedicated Server' in link.text:
        if 'Preview' in link.text:
            preview_ver = link.text.split()[-1]
        elif 'Release' in link.text:
            release_ver = link.text.split()[-1]

if release_ver:
    with open("bedrock_server_version_release.txt", "w") as f:
        f.write(release_ver + "\n")

if preview_ver:
    with open("bedrock_server_version_preview.txt", "w") as f:
        f.write(preview_ver + "\n")
