# creds for emailling
sender_address = "vvkovyazin@miem.hse.ru"
sender_password = "vladislav.2001"
smtp_host = "smtp.gmail.com"
smtp_port = 465

## Headers for proper requests (do not touch)

header = {
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept":
    "application/json",
    "Accept-Language":
    "en-US,en;q=0.9,ru;q=0.8",
    "Content-Type":
    "application/json;charset=UTF-8",
    "Host":
    "www.adidas.ru",
    "Connection":
    "keep-alive",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Origin":
    "https://www.adidas.ru",
    "Referer":
    "https://www.adidas.ru/adidasrunners/?cm_mmc=AdieSEM_Google-_-DSA-_-Test-_--_-dv%3AeCom-_-cn%3ADSA-_-pc%3AGoogle&cm_mmc1=&cm_mmc2=PPC-B-Multiple-Multiple-RU-CIS-eCom-Paid_Search&gclid=CjwKCAiA-_L9BRBQEiwA-bm5fmyAAAOwY7J-9RrnQFDVs03sTcLMePLo7ees9zm1ncmhlFAe-OHNnhoCvWoQAvD_BwE"
}

header_event_api = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "en-US,en;q=0.9,ru;q=0.8",
    "Connection":
    "keep-alive",
    "Host":
    "www.adidas.ru",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

me_header = {
    ":authority": "www.adidas.ru",
    ":method": "GET",
    ":path": "/adidasrunners/api/users/me",
    ":scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    #"referer": "",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    #"x-access-token": "",
}