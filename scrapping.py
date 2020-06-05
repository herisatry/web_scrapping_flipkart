from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&sid=tyy&as=on&as-show=on&otracker=off'

uClient = uReq(my_url) #load the url
page_html = uClient.read() #this will parse the page
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"_3liAhj"})

#print(len(containers))

filename = "products.csv"
f = open(filename,"w")
headers = "Product_Name,Pricing,Ratings\n"
f.write(headers)

print("Article found: " ,len(containers),"\n")
for container in containers:
    product = container.find("a",{"class":"_2cLu-l"})
    product_name = product.text.strip()
    
    price = container.find("div",{"class":"_1vC4OE"})
    trimmed_price = price.text.replace("₹","")
    final_price = trimmed_price.replace(",","")
    
    #rating = container.find("div",{"class":"hGSR34"})
    
    print(final_price, "\n",product_name, "\n")
    f.write(final_price+ ","+product_name+"\n")
f.close()