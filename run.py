import requests
from bs4 import BeautifulSoup

url = "https://www.facebook.com/100002698669337"


def extract_facebook_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    script_tags = soup.find_all("script")
    for script_tag in script_tags:
        if "userVanity" in script_tag.text and "userID" in script_tag.text:
            script_content = script_tag.text
            break
    else:
        return None, None

    # Extract userVanity
    user_vanity = script_content.split("userVanity:")[0]
    # Extract userID
    user_id = script_content.split("userID:")[0]
    print(user_vanity, "\n", user_id, "\n", title)
    return user_vanity, user_id, title


# extract_facebook_info(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# with open("result.html", "w", encoding="UTF-8") as f:
#     f.write(soup.prettify())
# ios_url = soup.find("meta", property="al:ios:url")
# text = ios_url["content"]
# print(text.split("/")[-1])
r = soup.prettify()
arr = r.splitlines()
username = ""
for item in arr: 
    if "userVanity" in item:
        for i in item.split(","):
            if "userVanity" in i:
                k = i.split(":")[1]
                if k == "":
                    pass
                else:
                    username = k
print(username)                