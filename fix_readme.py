import urllib.request
import re
import concurrent.futures
import sys
import os

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_content = f.read()

def check_url(url):
    if not url.startswith('http'):
        return True, url
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read(2048).decode('utf-8', errors='ignore').lower()
            if "domain is parked" in content or "buy this domain" in content:
                print(f"URL Failed (Parked): {url}")
                return False, url
            return True, url
    except urllib.error.HTTPError as e:
        if e.code in [404, 410]:
            print(f"URL Failed (HTTP {e.code}): {url}")
            return False, url
        if e.code == 403:
            # Lots of sites return 403 for bots, let's be lenient
            return True, url
        return True, url 
    except Exception as e:
        print(f"URL Failed (Exception {e}): {url}")
        return False, url

urls_to_check = set()
lines = readme_content.split('\n')
for line in lines:
    m = re.search(r'- \[(.*?)\]\((.*?)\)', line)
    if m:
        urls_to_check.add(m.group(2))

valid_urls = set()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(check_url, urls_to_check)
    for is_valid, url in results:
        if is_valid:
            valid_urls.add(url)

# Remove lines with invalid URLs
new_lines = []
for line in lines:
    m = re.search(r'- \[(.*?)\]\((.*?)\)', line)
    if m:
        if m.group(2) not in valid_urls:
            continue
    new_lines.append(line)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Done removing invalid links!")
