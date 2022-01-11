#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install selenium')


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver


# In[4]:


driver = webdriver.Chrome(r"C:/Users/sony/Downloads/chromedriver_win32/chromedriver.exe")


# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data

# In[4]:


driver.get('https://www.naukri.com/')


# In[5]:


search_job = driver.find_element_by_id('qsb-keyword-sugg')
search_job.send_keys("Data Analyst")
search_loc = driver.find_element_by_xpath("//input[@id='qsb-location-sugg']")
search_loc.send_keys("Bangalore")


# In[6]:


search_btn = driver.find_element_by_xpath("//div[@class='search-btn']/button")
search_btn.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[9]:


titles=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")


# In[11]:


titles


# In[12]:


for i in titles:
    if i.text is None :
        job_title.append("--") 
    else:
        job_title.append(i.text)


# In[16]:


job_title[0:10]


# In[17]:


locations=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
for i in locations:
    if i.text is None :
        job_location.append("--") 
    else:
        job_location.append(i.text)
job_location[0:10]        


# In[25]:


companies=driver.find_elements_by_xpath("//div[@class='subTitle ellipsis fleft']")
for i in companies:
    if i.text is None :
        company_name.append("--") 
    else:
        company_name.append(i.text)
company_name[0:10]


# In[26]:


experience=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")
for i in experience:
    if i.text is None :
            experience_required.append("--") 
    else:
            experience_required.append(i.text)
experience_required[0:10]            


# In[27]:


df=pd.DataFrame({"experience_required":experience_required[0:10],"company_name":company_name[0:10],"job_location":job_location[0:10],
                "job_title":job_title[0:10]})
df


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[28]:


url = "https://www.naukri.com/"
driver.get(url)


# In[29]:


search_field_designation=driver.find_element_by_id("qsb-keyword-sugg")
search_field_designation.send_keys("Data Scientist")
search_field_location=driver.find_element_by_id('qsb-location-sugg')  
search_field_location.send_keys("Bangalore")


# In[35]:


search_button=driver.find_element_by_xpath("//div[@class='search-btn']/button")
search_button.click()


# In[30]:


job_title=[]
job_location=[]
company_name=[]


# In[36]:


titles=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in titles:
    if i.text is None :
        job_title.append("--") 
    else:
        job_title.append(i.text)
job_title


# In[37]:


locations=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
for i in locations:
    if i.text is None :
        job_location.append("--") 
    else:
        job_location.append(i.text)
job_location        


# In[38]:


companies=driver.find_elements_by_xpath("//div[@class='mt-7 companyInfo subheading lh16']/a")
for i in companies:
    if i.text is None :
        company_name.append("--") 
    else:
        company_name.append(i.text)
company_name        


# In[39]:


df=pd.DataFrame({"job_title":job_title[0:10],"company_name":company_name[0:10],"job_location":job_location[0:10]})
df


# Q3: In this question you have to scrape data using the filters available on the webpage as shown below: You have to use the location and salary filter. You have to scrape data for “Data Scientist” designation for first 10 job results. You have to scrape the job-title, job-location, company_name, experience_required. The location filter to be used is “Delhi/NCR” The salary filter to be used is “3-6” lakhs 

# In[40]:


url = "https://www.naukri.com/"
driver.get(url)


# In[41]:


search_field_designation=driver.find_element_by_id("qsb-keyword-sugg")   #job  search bar
search_field_designation.send_keys("Data Scientist")

search_button=driver.find_element_by_xpath("//div[@class='search-btn']/button")
search_button.click()


# In[45]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[46]:


loc=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[2]/div[2]/div[2]/label/p")
loc.click()

slry_box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[3]/div[2]/div[2]/label/p")
slry_box.click()


# In[47]:


titles=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in titles:
    if i.text is None :
        job_title.append("--") 
    else:
        job_title.append(i.text)
job_title        


# In[48]:


locations=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
for i in locations:
    if i.text is None :
        job_location.append("--") 
    else:
        job_location.append(i.text)
job_location        


# In[49]:


companies=driver.find_elements_by_xpath("//div[@class='mt-7 companyInfo subheading lh16']/a")
for i in companies:
    if i.text is None :
        company_name.append("--") 
    else:
        company_name.append(i.text)
company_name        


# In[50]:


experience=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")
for i in experience:
    if i.text is None :
            experience_required.append("--") 
    else:
            experience_required.append(i.text)
experience_required            


# In[51]:


df=pd.DataFrame({"job_title":job_title[0:10],"experience_required":experience_required[0:10],"company_name":company_name[0:10],
                 "job_location":job_location[0:10]})
df


# Q4 : Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 
# Brand
# Product Description
# Price

# In[53]:


driver = webdriver.Chrome(r"C:/Users/sony/Downloads/chromedriver_win32/chromedriver.exe")


# In[93]:


url = "https://www.flipkart.com/"
driver.get(url)


# In[94]:


search_bar=driver.find_element_by_class_name("_3704LK")
search_bar.send_keys('sunglasses')
button=driver.find_element_by_class_name('L0Z3Pu')
button.click()


# In[61]:


brand=[]
description=[]
price=[]


# In[96]:


brands=driver.find_elements_by_class_name('_2WkVRV')


# In[97]:


for i in brands:
        brand.append(i.text)
brand        


# In[98]:


desc=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')


# In[67]:


for i in desc:
        description.append(i.text)
description        


# In[99]:


prices=driver.find_elements_by_xpath("//div[@class='_30jeq3']")


# In[100]:


for i in prices:
        price.append(i.text)
price        


# In[101]:


nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")


# In[102]:


try:
    driver.get(nxt_button[1].get_attribute('href'))
except:
    driver.get(nxt_button[0].get_attribute('href'))
    


# In[91]:


df=pd.DataFrame({'Brand':brand,'Description':description,'Price':price})
df


# In[95]:


nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")


# quest-5  Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb-includesearpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace. you have to scrape the below mention attributes. These are
# 
# Rating
# Review_summary
# Full review

# In[106]:


url = "https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART"
driver.get(url)


# In[107]:


urls=[]
short_review=[]
complete_review=[]
stars=[]


# In[108]:


url_1 = driver.find_elements_by_xpath("//a[@class='ge-49M _2Kfbh8']")
for i in url_1:
    urls.append(i.get_attribute('href'))
url_2 = driver.find_elements_by_xpath("//a[@class='ge-49M']")
for i in url_2:
    urls.append(i.get_attribute('href'))


# In[109]:


for i in urls:
    driver.get(i)
    #for scrapping the number of stars
    for j in driver.find_elements_by_xpath("//div[@class='col _2wzgFH K0kLPL']/div[1]/div[1]"):
        stars.append(j.text)
    #for scrapping the short review
    for k in driver.find_elements_by_xpath("//p[@class='_2-N8zT']"):
        short_review.append(k.text)
    #for scrapping the complete review
    for l in driver.find_elements_by_xpath("//div[@class='t-ZTKy']/div/div"):
        complete_review.append(l.text)


# In[110]:


df=pd.DataFrame({'Number of Stars': stars,
                'Short Review': short_review,
               'Full Review': complete_review})
df


# In[111]:


url = "https://www.flipkart.com/"
driver.get(url)


# In[112]:


log_in_pop_up = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
log_in_pop_up.click()


# In[113]:


search_bar=driver.find_element_by_class_name("_3704LK")
search_bar.send_keys('sneakers')


# In[114]:


button=driver.find_element_by_class_name('L0Z3Pu')
button.click()


# In[115]:


brand=[]
description=[]
price=[]

start=0
end=4
for page in range(start,end):#for loop for scrapping 4 page
    
    brands=driver.find_elements_by_class_name('_2WkVRV')#scraping brands name by class name='_2WkVRV'
    for i in brands:
        brand.append(i.text)#appending the text in Brand list
        
    prices=driver.find_elements_by_xpath("//div[@class='_30jeq3']")# scraping the price from the xpath
    for i in prices:
        price.append(i.text)
        
    desc=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')#scraping description from the xpath
    for i in desc:
        description.append(i.text)
        
    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page
    try:
        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page
    except:
        driver.get(nxt_button[0].get_attribute('href'))    


# In[116]:


df=pd.DataFrame({'Brand':brand[:100],
                'Description':description[:100],
                'Price':price[:100]})
#printing dataframe
df


# Q7."https://www.myntra.com/shoes". Set price filter "Rs 6649 to Rs 13099" and color filter to "Black" and then scrap 100 shoes data. The data should include "Brand" of shoes, shoe short-description and price. Please not: Everything should done through code even the filtering for sneakers as well.

# In[117]:


url = "https://www.myntra.com/shoes%22"
driver.get(url)


# In[119]:


price_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div")
price_button.click()



black_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div")
black_button.click()


# In[120]:


shoe_names=[]
s_desc=[]
short_desc=[]
price=[]
page_urls = []


# In[124]:


nxt_page = driver.find_elements_by_xpath("//ul[@class='pagination-container']/li/a")
for i in nxt_page:
    page_urls.append(i.get_attribute('href'))
    

for url in page_urls[:3]:
    driver.get(url)
    Names=driver.find_elements_by_xpath("//div[@class='product-productMetaInfo']/h3")  #for scrapping shoe brand names
    for i in Names:
        shoe_names.append(i.text)
    
    desc=driver.find_elements_by_xpath("//div[@class='product-productMetaInfo']/h4") #for scrapping shoe short-description
    for i in desc:
        s_desc.append(i.text)
        #As, the s_desc list contain blank description in every alternate index, so removing the blank or null description
    for j in range(0,len(s_desc),2):
        short_desc.append(s_desc[j])
        
    rs=driver.find_elements_by_xpath("//div[@class='product-price']")  #for scrapping shoe prices
    for i in rs:
        price.append(i.text)    
                    


# In[125]:


df=pd.DataFrame({'Brand': shoe_names[:100],'Short-description': short_desc[:100],'Price': price[:100]})
df


# Q8:  Go to webpage https://www.amazon.in/Enter “Laptop” in the search field and then click the search icon.Then set CPU Type filter to “Intel Core i7” and “Intel Core i9”
# After setting the filters scrape first 10 laptops data.You have to scrape 3 attributes for each laptop:
# 1. title
# 2. Ratings
# 3. Price

# In[5]:


url = "https://www.amazon.in"
driver.get(url)


# In[27]:


Title=[]
Ratings=[]
price=[]

search_bar = driver.find_element_by_id("twotabsearchtextbox")    
search_bar.clear()                                               
search_bar.send_keys("laptops")                                   
search_button = driver.find_element_by_xpath('//span[@id="nav-search-submit-text"]') 
search_button.click()

filter_button=driver.find_elements_by_xpath("//a[@class='a-link-normal s-navigation-item']/span")
for i in filter_button:
    if i.text=='Intel Core i7':
        i.click()
        break
        
        
#Scrapping Titles
titles=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for i in titles[:10]:
    Title.append(i.text)
    
    
#scrapping Price
prices=driver.find_elements_by_xpath("//span[@class='a-price-whole']")
for i in prices[:10]:
    price.append(i.text)

#locating Ratings
urls=driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")#collecting urls of all the laptop
UR=[]
for i in urls[:10]:
    UR.append(i.get_attribute('href'))#getting the url of first 10 laptops
for url in UR:#loop for every laptop in the list
    driver.get(url)
    try:                  #exception handling for nosuchelementexception                                                    #click the rating link found
        rating=driver.find_element_by_xpath("//span[@class='a-size-base a-nowrap']//span")#locating the rating
        Ratings.append(rating.text)#appending the ratings in Ratings list
        
    except NoSuchElementException:
        Ratings.append("NO rating")#appending the No rating if no rating is there
        
#creating a dataframe
df=pd.DataFrame({'Title':Title,
                'Price':price,
                'Ratings':Ratings})
#printing dataframe
df


# Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida 
# location. You have to scrape company name, No. of days ago when job was posted, Rating of the company.
# This task will be done in following steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the Job option as shown in the image
# 3. After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter “Data Scientist” and click on search button.
# 4. You will reach to the following web page click on location and in place of “Search location” enter “Noida” and select location “Noida”.
# 5. Then scrape the data for the first 10 jobs results you get on the above shown page.
# 6. Finally create a dataframe of the scraped data.

# In[5]:


driver.get('https://www.ambitionbox.com/')


# In[6]:


job_option = driver.find_element_by_xpath("//a[@class='link jobs']")
job_option.click()

search_job = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div/div/span/input')
search_job.send_keys('Data Scientist')

search_btn = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div/button/span")
search_btn.click()

select_location = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/p")
select_location.click()

location = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input')
location.send_keys('Noida')

select_Noida = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/label")
select_Noida.click()


# In[ ]:


companies=[]
no_of_days_ago=[]
company_rating=[]


# In[8]:


company_name = driver.find_elements_by_xpath("//p[@class='company body-medium']")

for i in company_name:
    companies.append(i.text)
companies    


# In[13]:


no_of_days = driver.find_elements_by_xpath("//div[@class='other-info']/span[1]")

for i in no_of_days:
    no_of_days_ago.append(i.text)
no_of_days_ago    


# In[12]:


ratings = driver.find_elements_by_xpath("//div[@class='info']/div/div/a/span")

for i in ratings:
    company_rating.append(i.text)
company_rating    


# In[14]:


data = list(zip(companies,no_of_days_ago,company_rating))

import pandas as pd
df = pd.DataFrame(data,columns=['companies','no_of_days_ago','company_rating'])

df.head(10)


# Q10: Write a python program to scrape the salary data for Data Scientist designation.
# You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary.
# The above task will be, done as shown in the below steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the salaries option as shown in the image.
# 3. After reaching to the following webpage, In place of “Search Job Profile” enters “Data Scientist” and then click on “Data Scientist”.
# 4. Scrape the data for the first 10 companies. Scrape the company name, total salary record, average salary, minimum salary, maximum salary, experience required.
# 5. Store the data in a dataframe.

# In[15]:


driver.get('https://www.ambitionbox.com/')


# In[16]:


salary_option = driver.find_element_by_xpath("//a[@class='link salaries']")
salary_option.click()

job_profile = driver.find_element_by_xpath('/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input')
job_profile.send_keys('Data Scientist')

select_DS = driver.find_element_by_xpath("/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/div/div/div[1]/div/div/p")
select_DS.click()


# In[17]:


companies=[]
salary_record=[]
avg_salary=[]
min_salary_range=[]
max_salary_range=[]
experience_required=[]


# In[18]:


company_name = driver.find_elements_by_xpath("//div[@class='name']/a")
for i in company_name:
    companies.append(i.text) 
    
salary = driver.find_elements_by_xpath("//div[@class='name']/span")
for i in salary:
    salary_record.append(i.text)
    
Average = driver.find_elements_by_xpath("//p[@class='averageCtc']")
for i in Average:
    avg_salary.append(i.text)
    
#minimum salary
min_salary = driver.find_elements_by_xpath("//div[@class='salary-values']/div[1]")
for i in min_salary:
    min_salary_range.append(i.text)
    
#maximum salary
max_salary = driver.find_elements_by_xpath("//div[@class='salary-values']/div[2]")
for i in max_salary:
    max_salary_range.append(i.text)
    
#experience required
experience = driver.find_elements_by_xpath("//div[@class='salaries sbold-list-header']")
for i in experience:
    experience_required.append(i.text.split('\n')[2])    


# In[20]:


data = list(zip(companies,salary_record,avg_salary,min_salary_range,max_salary_range,experience_required))
import pandas as pd

df = pd.DataFrame(data,columns=['companies','salary_record','avg_salary','min_salary_range','max_salary_range','experience_required'])
df


# In[ ]:




