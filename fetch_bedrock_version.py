import requests
from bs4 import BeautifulSoup

url = "https://minecraft.wiki/w/Bedrock_Dedicated_Server"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

release_ver = None
preview_ver = None

# Locate the 'Latest version' table header
th = soup.find('th', string=lambda s: s and 'Latest version' in s)
if th:
    td = th.find_next_sibling('td')
    if td:
        for li in td.find_all('li'):
            bold = li.find('b')
            if bold and bold.text.strip() == "Release:":
                link = li.find('a')
                if link:
                    release_ver = link.text.strip()
            elif bold and bold.text.strip() == "Preview:":
                link = li.find('a')
                if link:
                    preview_ver = link.text.strip()

# Write to files and print results
if release_ver:
    with open("bedrock_server_version_release.txt", "w") as f:
        f.write(release_ver)
    print(f"Release Version: {release_ver}")
else:
    print("Release version not found.")

if preview_ver:
    with open("bedrock_server_version_preview.txt", "w") as f:
        f.write(preview_ver)
    print(f"Preview Version: {preview_ver}")
else:
    print("Preview version not found.")
