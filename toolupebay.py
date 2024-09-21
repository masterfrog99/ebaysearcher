import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?_nkw=playstation+5'
useragent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
}
response = requests.get(url, headers=useragent)

if response.status_code == 200:
    parse = BeautifulSoup(response.content, 'html.parser')
    
    with open("playstation5_listings.html", "w") as file:
        # styling the output
        file.write("""
        <html>
        <head>
            <style>
                @font-face {
                    font-family: 'Ubuntu';
                    src: url('fonts/Ubuntu-Regular.ttf') format('truetype');
                    font-weight: normal;
                }
                @font-face {
                    font-family: 'Ubuntu';
                    src: url('fonts/Ubuntu-Bold.ttf') format('truetype');
                    font-weight: bold;
                }
                body { font-family: 'Ubuntu', sans-serif; }
                .title { color: red; font-weight: bold; font-size: 24px; }
                .price { color: green; font-weight: bold; font-size: 20px; }
                .listing { margin-bottom: 20px; }
                a { font-size: 18px; }
            </style>
        </head>
        <body>
        """)
        listings = parse.findAll('li', class_='s-item')
        
        # organizing wanted data and filtering output       
        for listing in listings:
            title_tag = listing.find('div', class_='s-item__title')
            price_tag = listing.find('span', class_='s-item__price')
            link_tag = listing.find('a', class_='s-item__link')
    
            title = title_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            link = link_tag['href']
            
            price_bold = f"<strong>{price}</strong>"
            output = output = f"""
            <div class="listing">
                {title} - <span class='price'>{price}</span> - <a href="{link}">eBay Link</a>
            </div>
            """

            print(output.strip()) # optional
            
            # updating file
            file.write(output)
        file.write("<html><body>\n")
else:
    print("Failed to retrieve the page")
