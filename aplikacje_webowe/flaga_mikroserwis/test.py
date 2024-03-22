import requests

cookies = {
    'csrftoken': 'VvHIxNiXKKv4VvPkOOlGe9520CjArlEa',
    'sessionid': 'rxm9cn9l4l63dhhj70ar4zooyte51shf',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'pl-PL,pl;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'csrftoken=VvHIxNiXKKv4VvPkOOlGe9520CjArlEa; sessionid=rxm9cn9l4l63dhhj70ar4zooyte51shf',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://web.kazet.cc:42448/download-png/7c10ed658c7b032d38bac5fd7fc29e8ad2df13a02aed1ca9ec4d185661ae4690',
    cookies=cookies,
    headers=headers,
)
# print(response.content)
with open("/home/mpkitlo/src/BSK/flag.png", "wb") as f:
        f.write(response.content)

