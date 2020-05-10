
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
   executable_path = {'executable_path': 'chromedriver.exe'}
   return Browser('chrome', **executable_path, headless=False)

def scrape():
    # all the scraping code here
    browser = init_browser()
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(10)
    html = browser.html
# Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')




# Retrieve all elements that contain book information
    articles = soup.find_all("div", class_="list_text")



    titles =[]

    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        a = article.find('a').text
        titles.append(a)
        print('-----------')
        print(a)


    #     # Click the 'Next' button on each page
    #     try:
    #         browser.click_link_by_partial_text('next')
        
    #     except:
    #         print("Scraping Complete")



    titles[0]




    blurb =[]

    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        b = article.find('div', class_ = "article_teaser_body").text
        blurb.append(b)
        print('-----------')
        print(blurb)


    #     # Click the 'Next' button on each page
    #     try:
    #         browser.click_link_by_partial_text('next')
        
    #     except:
    #         print("Scraping Complete")



    blurb[0]



    news_title = titles[0]

    news_title




    news_p = blurb[0]
    news_p




    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(10)
    html2 = browser.html
    # Parse HTML with Beautiful Soup
    soup2 = BeautifulSoup(html2, 'html.parser')




    # Retrieve image file
    image_file = soup2.find_all("div", class_="carousel_items")
    image_file



    browser.click_link_by_partial_text('FULL IMAGE')



    browser.click_link_by_partial_text('more info')



    browser.click_link_by_partial_text('jpg')



    full_res_html = browser.html
    soup_full_res = BeautifulSoup(full_res_html, 'html.parser')



    featured_image_url =soup_full_res.find('img')['src']
    featured_image_url



    # URL of page to be scraped
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)

    time.sleep(10)
    html_weather = browser.html
    # Parse HTML with Beautiful Soup
    soup_weather = BeautifulSoup(html_weather, 'html.parser')




    mars_weather=soup_weather.find('div', class_ ='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text
    mars_weather



    # URL of page to be scraped
    url_mars_facts = 'https://space-facts.com/mars/'
    browser.visit(url_mars_facts)

    time.sleep(10)
    html_mars_facts = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars_facts = BeautifulSoup(html_mars_facts, 'html.parser')



    mars_facts=soup_mars_facts.find('table', class_ ='tablepress tablepress-id-p-mars')
    mars_facts


    # **Mars Hemispheres**
    # 

    # Cerberus Hemisphere Enhanced


    # URL of page to be scraped
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    time.sleep(10)
    html_mars_hemi = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')



    mars_hemi=soup_mars_hemi.find('div', class_ ='collapsible results')
    mars_hemi




    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    first_hemi_html = browser.html
    soup_first_hemi = BeautifulSoup(first_hemi_html, 'html.parser')
    featured_img1_url =soup_first_hemi.find('div', class_ ='content')

    featured_img1_url



    summary_featured_title1 =featured_img1_url.find('h2', class_ = 'title').text
    summary_featured_img1 =featured_img1_url.find('a')['href']
    first ={'title':summary_featured_title1, "img_url":summary_featured_img1}
    first


    # Schiaparelli Hemisphere Enhanced



    # URL of page to be scraped
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    time.sleep(10)
    html_mars_hemi = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')







    # # soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')
    # mars_hemi=soup_mars_hemi.find('div', class_ ='collapsible results')





    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    second_hemi_html = browser.html
    soup_second_hemi = BeautifulSoup(second_hemi_html, 'html.parser')
    featured_img2_url =soup_second_hemi.find('div', class_ ='content')

    featured_img2_url



    summary_featured_title2 =featured_img2_url.find('h2', class_ = 'title').text
    summary_featured_img2 =featured_img2_url.find('a')['href']
    second ={'title':summary_featured_title2, "img_url":summary_featured_img2}
    second


    # Syrtis Major Hemisphere Enhanced


    # URL of page to be scraped
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    time.sleep(10)
    html_mars_hemi = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')



    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    third_hemi_html = browser.html
    soup_third_hemi = BeautifulSoup(third_hemi_html, 'html.parser')
    featured_img3_url =soup_third_hemi.find('div', class_ ='content')

    featured_img3_url



    summary_featured_title3 =featured_img3_url.find('h2', class_ = 'title').text
    summary_featured_img3 =featured_img3_url.find('a')['href']
    third ={'title':summary_featured_title3, "img_url":summary_featured_img3}
    third






    # Valles Marineris Hemisphere Enhanced


    # URL of page to be scraped
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    time.sleep(10)
    html_mars_hemi = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')



    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    fourth_hemi_html = browser.html
    soup_fourth_hemi = BeautifulSoup(fourth_hemi_html, 'html.parser')
    featured_img4_url =soup_fourth_hemi.find('div', class_ ='content')

    featured_img4_url




    summary_featured_title4 =featured_img4_url.find('h2', class_ = 'title').text
    summary_featured_img4 =featured_img4_url.find('a')['href']
    fourth ={'title':summary_featured_title4, "img_url":summary_featured_img4}
    fourth


    # Dictionary - Titles and Image Files



    hemisphere_images_urls = [first, second, third, fourth]
    hemisphere_images_urls


pass

 