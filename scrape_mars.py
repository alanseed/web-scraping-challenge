# Script for the mars scraping functions 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Return a news item from the NASA site 
def get_nasa_news():
    url_base = "https://redplanetscience.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_base)
 
    html = browser.html
    soup = bs(html, "html.parser")
    news = soup.find('div',id='news')
    last = news.find("div", class_ = 'list_text')
    title = last.find("div", class_ = 'content_title').text 
    para = last.find("div", class_ = 'article_teaser_body').text 
    list_date = last.find("div", class_ = 'list_date').text 
    browser.quit() 
    return list_date, title, para

# Return the url to the current image featured on the JPL site  
def get_jpl_image():
    url_base = "https://spaceimages-mars.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_base)
    
    html = browser.html
    soup = bs(html, "html.parser")
    header=soup.find('img', class_="headerimage")
    url = url_base + header['src']
    browser.quit()
    return url

# Return a string with the HTML for the table on mars  
def get_mars_table():     
    url = "https://galaxyfacts-mars.com/"
    match = "Equatorial Diameter"
    df_list = pd.read_html(url,match=match)
    mars_table = df_list[0].to_html(index=False,header=False,classes=["table", "table-striped"])
    return mars_table

# Return the images of the four hemispheres from Astropedia 
def get_hemispheres():
    url_base = "https://marshemispheres.com/index.html"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # open the landing page and parse it with BS 
    browser.visit(url_base)
    html = browser.html
    soup = bs(html, "html.parser")

    # get the list of links to visit and the hemisphere names
    link_list = []
    title_list = []
    for desc in soup.find_all('div',class_="description"):
        for link in desc.find_all('a'):
            if link.has_attr('href'):
                link_list.append(link['href'])
                long_title = link.find('h3').contents[0]
                title = long_title[0:long_title.find(" Enhanced")]
                title_list.append(title)

    # loop over the list of links to get the url for each of the images 
    image_list = []
    for link in link_list:
        url = "https://marshemispheres.com/" + link 
        browser.visit(url)
        html_2 = browser.html
        soup_2 = bs(html_2, "html.parser")
        img = soup_2.find('img', class_="wide-image")
        image_list.append("https://marshemispheres.com/" + img['src'] )

    # combine the lists into a list of dictionaries and return 
    ret_list = []
    for ia in range(len(title_list)):
        hemisphere = {"title":title_list[ia], "img_url":image_list[ia]}
        ret_list.append(hemisphere)
    
    browser.quit()         
    return  ret_list          

# here is the scrape function 
def scrape():
    # get all the info that we need 
    nasa_date, nasa_title, nasa_news = get_nasa_news()
    jpl_image = get_jpl_image()
    mars_table = get_mars_table()
    hemi = get_hemispheres()

    # now package it up in a dictionary 
    mars_info = {} 
    mars_info["nasa_date"] = nasa_date
    mars_info["nasa_title"] = nasa_title
    mars_info["nasa_news"] = nasa_news
    mars_info["jpl_image"] = jpl_image
    mars_info["mars_table"] = mars_table
    mars_info["hemispheres"] = hemi
    return mars_info 

# test the function out 
#mars_info = scrape()
#keys = mars_info.keys()
#for key in keys:
#    print(f"Key = {key}")
#    print(mars_info[key])
#    print()