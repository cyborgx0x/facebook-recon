import requests
from bs4 import BeautifulSoup

url = "https://www.facebook.com/w4rf0t"
def process(data):
    link = "https://www.facebook.com/w4rf0t"
    return link
soup = BeautifulSoup(requests.get(url=url).text, features="html.parser")


title = soup.find("meta", property="og:title")
url = soup.find("meta", property="og:url")
image = soup.find("meta", property="og:image")

print(title["content"])
url["content"]
image["content"]


img_url = image["content"]
import cv2 as cv
from skimage import io

image = io.imread(img_url)
image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

import cv2

window_name = "image"

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image_2)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
