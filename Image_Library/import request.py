import tor 
import requests as req


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}




def import_request(url):
    """
    This function imports an image from a url.
    """
    try:
        page = req.get( url, proxies=proxies )
    except Exception as e:
        print("Error: The url is not valid.")
        print(e)
        return e
    else:
    
        return page.content

print(import_request("https://ipapi.co/"))
 