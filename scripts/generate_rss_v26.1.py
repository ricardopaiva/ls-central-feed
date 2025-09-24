import requests
from bs4 import BeautifulSoup
# from feedgen.feed import FeedGenerator
import hashlib
from datetime import datetime, timezone

import os
from slugify import slugify  # pip install python-slugify

URL = "https://help.lscentral.lsretail.com/Content/Hotfixes/Hotfixes-26-1.htm"


def parse_items(item_details_tags):
    items = []

    current_item = None

    for item_details_tag in item_details_tags:
        if item_details_tag.name == 'h4':
            current_item_title = item_details_tag.get_text(strip=True)
            current_item_details = []

            current_item = (current_item_title, current_item_details)
            items.append(current_item)

        elif item_details_tag.name == 'ul':
            details = item_details_tag.select("li")
            for detail in details:
                current_item_details.append(detail)

    return items


def scrape_release_notes(content_div):
    if content_div:
        # Parses the main content container and extracts the products (LS Central, Hotels, Localization, etc)
        products = {}
        current_product = None

        versions = {}
        current_version = None

        items  = {}
        for content_tag in content_div.find_all(['h3', 'div'], recursive=False):
            if content_tag.name == 'h3':
                current_product = clean_text(content_tag.get_text(strip=False))
                products[current_product] = {}
                versions = products[current_product]
                current_version = None

            elif content_tag.name == 'div' and current_product:
                for products_subtag in content_tag.find_all(['a', 'div'], recursive=True):
                    if products_subtag.name == 'a':
                        # current_version = extract_version(products_subtag.get_text(strip=True))
                        current_version = products_subtag.get_text(strip=True)
                        versions[current_version] = []
                    elif products_subtag.name == 'div' and current_product and current_version:
                        item_details_tags = products_subtag.find_all(['h4', 'ul'], recursive=False)
                        items = parse_items(item_details_tags)
                        versions[current_version].append(items)

        return products
    else:
        print("No article content found.")


def extract_release_date(version_str):
    """
    Extracts the release date from a version string like:
    '26.1.0, Release date July 8, 2025'
    Returns a timezone-aware datetime object. If not found, returns current UTC time.
    """
    import re
    from datetime import datetime, timezone
    match = re.search(r"Release date ([A-Za-z]+ \d{1,2}, \d{4})", version_str)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, "%B %d, %Y").replace(tzinfo=timezone.utc)
        except Exception:
            pass
    return datetime.now(timezone.utc)


def extract_version(version_str: str) -> str:
    """
    Extracts the version number from a version string like:
    '26.1.0, Release date July 8, 2025'
    Returns the version as a string (e.g., '26.1.0').
    If not found, returns an empty string.
    """
    import re
    match = re.match(r"^([\d\.]+)", version_str.strip())
    if match:
        return match.group(1)
    return ""


def extract_sub_product_from_version(version_str: str) -> str:
    """
    Extracts the sub product from a version string like:
    '26.1.0 Local Functionality Germany, Release date July 8, 2025'
    Returns the sub product as a string (e.g., 'Local Functionality Germany').
    If not found, returns an empty string.
    """
    import re
    match = re.match(r"^[\d\.]+\s+(.*?)\s*,\s*Release date", version_str.strip())
    if match:
        return match.group(1).strip()
    return ""


def clean_text(text):
    """Clean text by replacing encoded characters with their readable equivalents"""
    replacements = {
        '\xa0': ' ',  # non-breaking space
        '\u200b': '',  # zero-width space
        '\u2019': "'", # smart quote
        '\u2018': "'", # smart quote
        '\u201c': '"', # smart quote
        '\u201d': '"', # smart quote
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def generate_hotfixes_dict(content):
    # Example hotfix dict from your scraper:
    # hotfix = {
    #     "title": "LS Central Hotfix 26.1",
    #     "product": "ls-central",
    #     "version": "26.1",
    #     "date": "2023-12-15",
    #     "content": "Details about this hotfix..."
    # }

    hotfixes = []
    sort_id = 0
    for product, versions in content.items():
        for version, items_list in versions.items():
            title = f"{product} - {version} - Hotfixes"
            pub_date = extract_release_date(version)

            content_items = []
            for items in items_list:
                for item_title, details in items:
                    item_text = f"<strong>{item_title}</strong>"
                    content_items.append(f"{item_text}")
                    items_array = [f"{detail}" for detail in details]
                    content_items.append(f"<ul>" + "\n".join(items_array) + "</ul>")
            content = "\n".join(content_items)

            sort_id += 1
            hotfixes.append({
                "sort_id": sort_id,
                "title": title,
                "product": product.replace(" hotfixes", ""),
                # "version": version.split(",")[0].strip(),
                "version": extract_version(version),
                "subproduct": extract_sub_product_from_version(version),
                "date": pub_date,
                "content": content
            })
    return hotfixes


# def generate_rss_feed(content, output_file="hotfixes.xml"):
#     fg = FeedGenerator()
#     fg.id("https://example.com/hotfixes/rss")
#     fg.title("Product Hotfixes")
#     fg.link(href="https://example.com/hotfixes", rel="alternate")
#     fg.link(href="https://example.com/hotfixes/rss", rel="self")
#     fg.description("RSS feed of the latest product hotfixes.")


#     # 4. Loop through hotfix items and add them to feed
#     for product, versions in content.items():
#         for version, items_list in versions.items():

#             title = f"{product} - {version} - Hotfixes"
#             guid = hashlib.sha1(title.encode("utf-8")).hexdigest()
#             pub_date = extract_release_date(version)

#             fe = fg.add_entry()
#             fe.id(guid)
#             fe.title(title)
#             fe.link(href=URL)
#             fe.pubDate(pub_date)

#             for items in items_list:
#                 desc_items = []
#                 for items in items_list:
#                     items_array = []

#                     for item_title, details in items:
#                         item_text = f"<strong>{item_title}</strong>"
#                         desc_items.append(f"{item_text}")
#                         for detail in details:
#                             items_array.append(f"{detail}")
#                         desc_items.append(f"<ul>" + "\n".join(items_array) + "</ul>")
#                 description = "\n".join(desc_items)

#             fe.description(description)

#     # 5. Save the feed to an XML file
#     rss_feed = fg.rss_str(pretty=True)
#     with open(output_file, "wb") as f:
#         f.write(rss_feed)

#     print(f"RSS feed generated: {output_file}")


def generate_rss_feed_for_jekyll(hotfix):  #save_hotfix_md
    """Save a hotfix entry as a Jekyll markdown file."""
    # filename = f"_hotfixes/{slugify(hotfix['product'])}-{hotfix['version']}.md"
    filename = f"_hotfixes/{slugify(hotfix['product'])}-" \
           f"{slugify(hotfix['subproduct']) + '-' if hotfix.get('subproduct') else ''}" \
           f"{hotfix['version']}.md"
    os.makedirs("_hotfixes", exist_ok=True)

    front_matter = f"""---
title: "{hotfix['title']}"
product: {hotfix['product']}
version: "{hotfix['version']}"
subproduct: {hotfix['subproduct']}
minor_version: "{hotfix['version'].split('.')[0] + '.' + hotfix['version'].split('.')[1] if '.' in hotfix['version'] else '0'}"
date: {hotfix['date']}
order: {hotfix['sort_id']}
---

{hotfix['content']}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter)


def save_feed_template(product=None, version=None):
    os.makedirs("feeds", exist_ok=True)

    # Construct feed name and filter
    if product and version:
        name = f"{product}-v{version}"
        filter_clause = f'| where: "product", "{product}" | where: "version", "{version}"'
    elif product:
        name = product
        filter_clause = f'| where: "product", "{product}"'
    elif version:
        name = f"v{version}"
        filter_clause = f'| where: "version", "{version}"'
    else:
        name = "all"
        filter_clause = ""

    template = f"""---
layout: none
permalink: /feed/{name}.xml
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Hotfixes - {name}</title>
  <link>{{{{ site.url }}}}/hotfixes/</link>
  <description>RSS feed for {name} hotfixes</description>
  {{% assign fixes = site.hotfixes {filter_clause} %}}
  {{% for fix in fixes %}}
  <item>
    <title>{{{{ fix.title }}}}</title>
    <link>{{{{ site.url }}}}{{{{ fix.url }}}}</link>
    <pubDate>{{{{ fix.date | date_to_rfc822 }}}}</pubDate>
    <description><![CDATA[{{{{ fix.content | strip_html }}}}]]></description>
  </item>
  {{% endfor %}}
</channel>
</rss>
"""
    with open(f"feeds/feed-{name}.xml", "w", encoding="utf-8") as f:
        f.write(template)


# Step 1: Fetch the HTML (like wget)
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# Step 2: Find the main content container and fetch the release notes
content_div = soup.find('div', role='main', id='mc-main-content')
content = scrape_release_notes(content_div)

# 3. Initialize RSS feed
# generate_rss_feed(content, output_file="hotfixes.xml")  # Uses FeedGenerator

hotfixes_dict = generate_hotfixes_dict(content)
for hotfix in hotfixes_dict:
    generate_rss_feed_for_jekyll(hotfix)  # Uses jekyll-feed

save_feed_template()

print('The end')