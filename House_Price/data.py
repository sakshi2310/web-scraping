import requests
import bs4

url = 'https://housing.com/buy-house-in-surat-for-sale-srpid-M2P20drlq24mltepds2?gad_source=1&gclid=CjwKCAiAxaCvBhBaEiwAvsLmWPCD2so6oOS0PxcfDIlUom4HUvTkKRcYVi6WIeyazsSq8FYkjaD9ghoCvS8QAvD_BwE'


print("hello")
r = requests.get(url)
print(r.status_code)

resp = requests.get(url)
scraptdata = bs4.BeautifulSoup(resp.text,'html.parser')
# print(scraptdata.prettify()) 
print(scraptdata)