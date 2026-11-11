from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


driver = webdriver.Safari()

def get_product_list ():
  driver.get ("https://www.amazon.com.mx/s?k=musica&__mk_es_MX=ÅMÅŽÕÑ&crid=M96PDMFN94ZO&sprefix=musica%2Caps%2C235&ref=nb_sb_noss_1")

  soup = BeautifulSoup(driver.page_source, "html.parser")
  a_class = "a-link-normal s-line-clamp-3 s-link-style a-text-normal"
  a_tags = soup.find_all("a", class_= a_class)

  for a in a_tags :
    title = a.text.replace("\n", "")
    link = a.get("href")
    print("titulo: ", title)
    print("link: ", link)
    print("\n")

    detail_link = "https://amazon.com.mx" + link if "https" not in link else link
    get_details(detail_link)

  


def get_details(url):
  driver.get(url)
  time.sleep(3)

  soup = BeautifulSoup(driver.page_source, "html.parser")

  price_tag = soup.find("span", class_="a-offscreen")

  if price_tag:
    price_text = price_tag.get_text(" ", strip=True)
    print("Texto recibido:", repr(price_text))

    match = re.search(r"[\d,]+(?:\.\d+)?", price_text)

    if match:
      price = float(match.group().replace(",", ""))
      print("Precio:", price)
      print("\n")
    else:
      print("Precio no válido:", price_text)
      print("\n")
  else:
    print("Precio no disponible:", url)
    print("\n")
  


get_product_list()

driver.quit()
