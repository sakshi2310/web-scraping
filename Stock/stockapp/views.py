from django.shortcuts import render
import requests
import bs4
import pandas as pd


# Create your views here.
def home(request):

     dic = {'company name':[],'price':[],'stock':[],'percentage':[]}
     if request.method == "POST":
          url = request.POST['url']
          
          resp = requests.get(url)
          scraptdata = bs4.BeautifulSoup(resp.text,'html.parser')
          # print(scraptdata.prettify()) 
          companys = scraptdata.select("div.ZvmM7")
          for company in companys:
               print(company.string)
               dic['company name'].append(company.string)

          parent = scraptdata.find_all("div" , class_="SxcTic")
          for price in parent:
               prices = price.find('div', class_='YMlKec')
               # print(prices.string)
               dic['price'].append(prices.string)


          for stocks in parent:
               stock_ele = stocks.select("span.P2Luy.Ez2Ioe, span.P2Luy.Ebnabc , span.P2Luy.TrEAYc")
               for stock in stock_ele:
                    print(stock.text)
                    dic['stock'].append(stock.string)

          for per in parent:
               # print("hy")
               percentage = per.select("span.NydbP.VOXKNe , span.NydbP.nZQ6l , span.NydbP.oNKluc")
               for avg in percentage:
                    # print(avg.text)
                    dic['percentage'].append(avg.text)
                    print(dic['percentage'])

     df = pd.DataFrame.from_dict(dic)
     df.to_csv("stock.csv")

     return render(request,'home.html')