
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
   executable_path = {'executable_path': 'chromedriver.exe'}
   return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    # all the scraping code here
    browser = init_browser()
    # **Get First Headline and Teaser**

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    import time
    time.sleep(2)
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all headlines
    headlines = soup.find_all("div", class_="list_text")

    titles =[]

    for headline in headlines:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        a = headline.find('a').text
        titles.append(a)
    #         print('-----------')
    #         print(a)

    news_title = titles[0]
    news_title

    blurb =[]

    for headline in headlines:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        b = headline.find('div', class_ = "article_teaser_body").text
        blurb.append(b)
    #         print('-----------')
    #         print(blurb)

    news_p =blurb[0]
    news_p


    # **Get Featured Image**

    # URL of starting page
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #Click through pages to get to page to be scraped
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    browser.click_link_by_partial_text('jpg')

    #Extract link from page
    full_res_html = browser.html
    soup_full_res = BeautifulSoup(full_res_html, 'html.parser')
    featured_image_url =soup_full_res.find('img')['src']
    featured_image_url

    # **Extract Weather Data**

    # URL of page to be scraped
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)

    time.sleep(2)
    html_weather = browser.html
    # Parse HTML with Beautiful Soup
    soup_weather = BeautifulSoup(html_weather, 'html.parser')


    # #Data to be extracted
    mars_weather=soup_weather.find('div', class_ ='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text
    mars_weather

   # **Space Facts Table**


    mars_df = pd.read_html('https://space-facts.com/mars/')[0]
    mars_df.columns=["Description", "Value"]
    mars_df.set_index("Description", inplace = True)
    mars_facts =mars_df.to_html(classes="table")
    mars_facts = mars_facts.replace("'","")


    # **Mars Hemispheres**
    # 

    # Cerberus Hemisphere Enhanced

    # Starting URL
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    first_hemi_html = browser.html
    soup_first_hemi = BeautifulSoup(first_hemi_html, 'html.parser')

    #Pull specific data from webpage
    hemi_title1_url = soup_first_hemi.find('h2', class_ ='title').text
    hemi_img1_url =soup_first_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    first ={'title':hemi_title1_url, "img_url":hemi_img1_url}
    first


    # Schiaparelli Hemisphere Enhanced


    # Starting URL
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    second_hemi_html = browser.html
    soup_second_hemi = BeautifulSoup(second_hemi_html, 'html.parser')

    #Pull specific data from webpage
    hemi_title2_url = soup_second_hemi.find('h2', class_ ='title').text
    hemi_img2_url =soup_second_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    second ={'title':hemi_title2_url, "img_url":hemi_img2_url}
    second


    # Syrtis Major Hemisphere Enhanced

    # Starting URL
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    third_hemi_html = browser.html
    soup_third_hemi = BeautifulSoup(third_hemi_html, 'html.parser')

    #Pull specific data from webpage
    hemi_title3_url = soup_third_hemi.find('h2', class_ ='title').text
    hemi_img3_url =soup_third_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    third ={'title':hemi_title3_url, "img_url":hemi_img3_url}
    third


    # Valles Marineris Hemisphere Enhanced

    # Starting URL
    url_mars_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_hemi)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    forth_hemi_html = browser.html
    soup_forth_hemi = BeautifulSoup(forth_hemi_html, 'html.parser')

    #Pull specific data from webpage
    hemi_title4_url = soup_forth_hemi.find('h2', class_ ='title').text
    hemi_img4_url =soup_forth_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    forth ={'title':hemi_title4_url, "img_url":hemi_img4_url}
    forth


    # Dictionary - Titles and Image Files

    hemisphere_images_urls = [first, second, third, forth]
    hemisphere_images_urls


    # Store data in a dictionary
    mars_data = {

        "News_Title" : news_title,
        "News_Blurb" : news_p,
        "Featured_Image" : featured_image_url,
        "Mars_Weather" : mars_weather,
        "Mars_Facts" : mars_facts,
        "Hemisphere_Images" : hemisphere_images_urls

    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

pass

 