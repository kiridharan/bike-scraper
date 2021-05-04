from os import error
import json
import requests
from bs4 import BeautifulSoup


list_links = [
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/2/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/1/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/3/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/4/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/5/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/6/50/popularity/desc/",
            "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/1:9/1:10/1:11/1:12/1:13/1:14/1:15/1:16/1:17/1:18/1:19/1:20/1:21/1:26/1:34/page/7/50/popularity/desc/",
]
base_url = "https://autoportal.com/newbikes/bike-finder/1:1/1:2/1:3/1:4/1:5/1:6/1:7/1:8/page/1/50/popularity/desc/"
data = {}
lis = []
def get_data(url):
    base_link_address = "https://autoportal.com"
    r = requests.get(base_url)
    content = r.content
    soup = BeautifulSoup(content , features="html.parser")
    bikes = soup.find_all('div', class_='item')
    for bike in bikes:
        try:
            bike_name = bike.find('a',class_= 'model-title').text
            bike_detail_name = bike.find('a',class_='title').text 
            bike_price = bike.find('div',class_='price cell-md').text
            engine = bike.find('li',class_='engine').span.text
            mileage = bike.find('li',class_='mileage').span.text
            power = bike.find('li',class_='power').span.text
            img = bike.img['data-original']
            details_link = bike.img['data-link']
            bike_detail_link = base_link_address + details_link
            
            data = {
                
                    "bike_name": bike_name.strip(),
                    "bike_detail name": bike_detail_name,
                    "bike_price": bike_price,
                    "bike_engine": engine,
                    "bike_mileage": mileage,
                    "bike_power": power,
                    "bike_img_url": img,
                    "detail_page_url": bike_detail_link,
               
            }
            # bike_list=[]
            # bike_list.append(bike_name.strip())
            # bike_list.append(bike_detail_name.strip())
            # bike_list.append(bike_price.strip())
            # bike_list.append(engine.strip())
            # bike_list.append(mileage.strip())
            # bike_list.append(power.strip())
            # bike_list.append(img.strip())
            
            # lis.append(bike_list)
            


        except AttributeError:
            pass
    

def list_url(url_list):
    for url in url_list:
        print(url)


if __name__ == '__main__':
    get_data(base_url)
    list_url(list_links)