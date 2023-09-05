import requests
from bs4 import BeautifulSoup

# req = requests.get("https://medium.com/@hm6091999")
# soup = BeautifulSoup(req.content,"html.parser")
# print(soup.prettify())

def scrape_and_pretty_print(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        soup = BeautifulSoup(response.text, 'html.parser')
        pretty_html = soup.prettify
        
        return pretty_html
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    usernames = ["session.userinfo.nickname"]  # Replace with your usernames
    for username in usernames:
        medium_url = f"https://medium.com/@{username}"
        instagram_url = f"https://www.instagram.com/@{username}/"
        
        print("Medium Profile:")
        print(scrape_and_pretty_print(medium_url))
        
        print("Instagram Profile:")
        print(scrape_and_pretty_print(instagram_url))
        
        print("=" * 40)  # Add a separator between profiles
