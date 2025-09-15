import requests
from torpy.http.requests import TorRequests, tor_requests_session, do_request as requests_request
from termcolor import colored
import multiprocessing, ctypes
from bs4 import BeautifulSoup
\

def getCookies(cookie_jar, domain):
    cookie_dict = cookie_jar.get_dict(domain=domain)
    found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
    return ';'.join(found)


headers = {
  'authority': 'www.google.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
  # 'cookie': 'CONSENT=YES+shp.gws-20211115-0-RC3.de+FX+113; OTZ=6728428_42_42_114990_38_379890; 1P_JAR=2022-11-16-08; AEC=AakniGN8RcZY12tMP3MfhMYBHCXhMGHPEYVDSkFF8gKcgDpRzF5MVccWh-E; OGPC=19026797-4:; NID=511=Wyfz8yapZPJgf0B_3Gk5T98azNCjJVUpIJMhgYFy_M-IikNTNxurJ6IKKD7cT57gmHy-JLnyfmhh7Ka7o_Atkf1pb3TE8EbsUcq5jYknbst6lBHP_vdkTmxudoy30XSclZGJXzbJqkK9vDp9gJZSTLWBwxeAaR7SfwmHhMryVj9pjDy_YJOjZeXrhOBceS8BFNW9Oo20ajwj; OGP=-19026797:; DV=A4_NqugM3AUrgJ14QZ6ztebO2Uj6RxhonmSkrvHUVwEAAAA; 1P_JAR=2022-11-18-10; AEC=AakniGNyce6HYoOyayP0sNALqAXgo7hUjG_on9M8NbJxkZzVymCEkL9KuK8',
  'referer': 'https://www.google.com/',
  'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"107.0.1418.42"',
  'sec-ch-ua-full-version-list': '"Microsoft Edge";v="107.0.1418.42", "Chromium";v="107.0.5304.110", "Not=A?Brand";v="24.0.0.0"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
  'Content-Type': 'application/json'
}

headers1 = {
  'authority': 'www.google.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
  # 'cookie': 'CONSENT=YES+shp.gws-20211115-0-RC3.de+FX+113; OTZ=6728428_42_42_114990_38_379890; 1P_JAR=2022-11-16-08; AEC=AakniGN8RcZY12tMP3MfhMYBHCXhMGHPEYVDSkFF8gKcgDpRzF5MVccWh-E; OGPC=19026797-4:; NID=511=Wyfz8yapZPJgf0B_3Gk5T98azNCjJVUpIJMhgYFy_M-IikNTNxurJ6IKKD7cT57gmHy-JLnyfmhh7Ka7o_Atkf1pb3TE8EbsUcq5jYknbst6lBHP_vdkTmxudoy30XSclZGJXzbJqkK9vDp9gJZSTLWBwxeAaR7SfwmHhMryVj9pjDy_YJOjZeXrhOBceS8BFNW9Oo20ajwj; OGP=-19026797:; DV=A4_NqugM3AUrgJ14QZ6ztebO2Uj6RxhonmSkrvHUVwEAAAA; 1P_JAR=2022-11-18-10; AEC=AakniGNyce6HYoOyayP0sNALqAXgo7hUjG_on9M8NbJxkZzVymCEkL9KuK8',
  'referer': 'https://www.google.com/',
  'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"107.0.1418.42"',
  'sec-ch-ua-full-version-list': '"Microsoft Edge";v="107.0.1418.42", "Chromium";v="107.0.5304.110", "Not=A?Brand";v="24.0.0.0"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
  'Content-Type': 'application/json'
}

def get_google_results(i, headers, headers1):
    cnt = 0
    cookie_previous = False
    keyword='stripe'
    page=1
    number_query=10
    while True:
        try:
            with tor_requests_session() as sess:
                while True:
                    url = f"https://www.google.com/search?q={keyword}&hl=en&device=Desktop"

                    payload = {}

                    if(cookie_previous):
                        sess.headers.update(headers1)
                        r = sess.get(url, headers=headers1, data=payload)
                    else:
                        r = sess.get(url, headers=headers, data=payload)

                    if r.status_code==200:
                        mangaerlist.append('ok')
                        print(colored(f'Process {i}: {len(mangaerlist)}' , 'green'))
                        cookie_ = getCookies(r.cookies, '.google.com')
                        headers1['cookie'] = cookie_
                        sess.headers.update(headers1)
                        cookie_previous = True

                    else:
                        print(colored(f'Process {i}: {r.status_code}', 'red'))
                        cookie_previous = False
                        break
                    # print(cnt)
        except Exception as e:
            print(e)
mangaerlist = multiprocessing.Manager().list()

number_processes = 10

processes = []

for i in range(number_processes):
    processes.append(multiprocessing.Process(target=get_google_results, args=[i, headers, headers1]))

for p in processes:
    p.start()

for p in processes:
    p.join()