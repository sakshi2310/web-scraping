from django.shortcuts import render
import requests
import bs4
import pandas as pd

# Create your views here.
def home(request):
     values = []
     data = {'title':[],'price':[]}
     if request.method == "POST":
          web_url = request.POST['url']
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
          
          resp = requests.get(web_url,headers=headers)
          scraptdata = bs4.BeautifulSoup(resp.text,'html.parser')

# how to print all the data ------------------------------------------
          # print(scraptdata.prettify())


# print the title of page --------------------------------------------
          # print(scraptdata.title , type(scraptdata.title))
          # print(scraptdata.title.string , type(scraptdata.title))


# using css selecter how select class and id -------------------------
          # print(scraptdata.select("div.topsocial"))
          # print(scraptdata.select("a#IE_TOP_VERNACULAR_ENGLISH"))

# using find select the id and class --------------------------------
          # print(scraptdata.find(id="IE_TOP_VERNACULAR_ENGLISH"))
          # print(scraptdata.find(class_="topsocial"))


# parent chlid of class ---------------------------------------------
     # for chile in scraptdata.find(class_="topsocial").children:
     #      print(chile)
          
     # for parent in scraptdata.find(class_="topsocial").parent:
     #      print(parent)

# how to modify the tag----------------------------------------------
          # m = scraptdata.find(class_="topsocial")
          # m.name = "span"
          # print(m)

# how to modify the class name -------------------------------------
          # m = scraptdata.find(class_="topsocial")
          # m["class"] = "myclass"
          # print(m)

# how to modify the text inside the class -----------------------
          # m = scraptdata.find(class_="topsocial")
          # m.string = "I AM SAKSHI"
          # print(m)

# how to insert a tag in file -------------------------------------
          # ultag = scraptdata.new_tag("ul")

          # litag = scraptdata.new_tag("li")
          # litag.string = "this is li tag"
          # ultag.append(litag)

          # Insert = scraptdata.html.body.insert(0,ultag)
          # print(Insert)


# know the attribute is avaible in tag or not----------------------
          # cont = scraptdata.find(class_="topsocial")
          # print(cont.has_attr("id"))

          # id = scraptdata.find(id ="IE_TOP_VERNACULAR_ENGLISH")
          # print(id.has_attr("class"))

#create the function of diffternt types-----------------------------
          # def has_class_but_not_id(tag):
          #      return not tag.has_attr("class") and not tag.has_attr("id")
          
          # def has_content(tag):
          #      return tag.has_attr("content")

          # # result = scraptdata.find_all(has_class_but_not_id)
          # result = scraptdata.find_all(has_content)
          # for results in result:
          #      print(results)
         
# class practice -------------------------------------------------
          
          # for data in scraptdata.find_all('h3'):
          #      # img_url = data.get('src')
          #      # print(img_url)
          #      values.append(data.text)

#amzon data project ---------------------------------------------BB
          spans = scraptdata.select("span.a-size-medium.a-color-base.a-text-normal")
          for span in spans:
               print(span.string)
               data['title'].append(span.string)

          prices = scraptdata.select("span.a-price-whole")
          for price in prices:
               print(price.string)
               data['price'].append(price.string)
               if len(data['price']) == len(data['title']):
                    break;
     df = pd.DataFrame.from_dict(data)
     df.to_csv("data.csv")

     return render(request,'home.html',{'data':values})