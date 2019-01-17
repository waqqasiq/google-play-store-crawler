import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import time

appNameSpanClassName = "AHFaub"
appReviewDateSpanClassName = "bAhLNe kx8XBd"
numberOfRatingsCountSpanClassName = "AYi5wd TBRnV"
ratingsCountSpanClassName = "BHMmbe"
installsSpanClassName = "htlgb"
appNameSpanClassName = "AHFaub"
categorySpanClassName = "T32cc UAO9ie"


import pandas as pd

df = pd.read_csv("SampleAppNameURL.csv") #reading the csv file
url = df['URL'].tolist()
appNameList = df['App'].tolist()
#url = ["https://play.google.com/store/apps/details?id=com.lemongame.klondike.solitaire","https://play.google.com/store/apps/details?id=com.dimcher.entertainment.revolver","https://play.google.com/store/apps/details?id=com.orangenose.tablefull"]

def getAppName(soup):
    for span_tag in soup.find_all('h1', {'class':appNameSpanClassName}):
        appName = span_tag.find('span').text
        return appName
    
def getNumberOfRatings(soup):
    NoOfRating = soup.findAll("span", {"class": numberOfRatingsCountSpanClassName})[0].text
    return NoOfRating
 
def getRating(soup):
    rating = soup.findAll("div", {"class": ratingsCountSpanClassName})[0].text
    return rating

def getInstalls(soup):
    installs_size = soup.findAll("span", {"class": installsSpanClassName})[4].text
    if "M" in installs_size[-1] or "k" in installs_size[-1] or "Varies with device" in installs_size:
        installs_paid = soup.findAll("span", {"class": installsSpanClassName})[7].text
        size_installs_list = [installs_size,installs_paid]
        return size_installs_list
    lists = [installs_size]
    return lists

def getUpdateDate(soup,index):
    update = soup.findAll("span", {"class": installsSpanClassName})[index].text
    return update

def getSize(soup):
    size = soup.findAll("span", {"class": installsSpanClassName})[3].text
    return size

    
def getCategory(soup):
    count=0
    for span_tag in soup.find_all('span', {'class':categorySpanClassName}):
        count = count +1
        appCategory = span_tag.find('a').text
        if count==2:
            return appCategory
    

def getReview(soup):
    review = soup.find("span", {"jsname": 'fbQN7e'})
    #Rating.append(rating)
    return review

def getContentRating(soup,index):
    content = soup.findAll("span", {"class": installsSpanClassName})[index].text
    if "L" in content:
        content = content.split("L")
        return content[0]
  
def getRatingDist(soup):

   rating_dist = soup.find('span',{'class': "L2o20d P41RMc"})
   title5 = rating_dist['title']
   
   rating_dist = soup.find('span',{'class': "L2o20d tpbQF"})
   title4 = rating_dist['title']
   
   rating_dist = soup.find('span',{'class': "L2o20d Sthl9e"})
   title3 = rating_dist['title']
   
   rating_dist = soup.find('span',{'class': "L2o20d rhCabb"})
   title2 = rating_dist['title']
   
   rating_dist = soup.find('span',{'class': "L2o20d A3ihhc"})
   title1 = rating_dist['title']
   
   return title5,title4,title3,title2,title1
 
        
    
#The for loop below runs for each link in the URL list
totalNumberOfURLs = len(url)
startingPoint = 0
totalURLs = totalNumberOfURLs-startingPoint
print("Total number of URLs: %d \nStarting from index: %d | App: %s\n" %(totalURLs,startingPoint,appNameList[startingPoint]))

index = startingPoint - 1 
while index < totalNumberOfURLs-1:
    index += 1
    startTime = time.time()
    html_doc = requests.get(url[index])
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    #print(soup.prettify())
    x = soup.get_text()
    x= x.split('"')
    k=index+1
    #print("Now Running: App Number - ",k)
    App = []
    Reviews = []
    Ratings = []
    Category = []
    Content_Rating = []
    Installs = []
    Last_updated = []
    No_of_Rating = []
    Rating = []
    Size = []
    Url = []
    Type = []
    Content_Rating = []
    Url.append(url[index])
    
    for i in range(len(x)):
        if x[i]=="]\n]\n]\n,1,null," or x[i]=="]\n]\n]\n,2,null," or x[i]=="]\n]\n]\n,3,null," or x[i]=="]\n]\n]\n,4,null," or x[i]=="]\n]\n]\n,5,null,":
            if x[i]=="]\n]\n]\n,1,null,":
                i = i+1
                Ratings.append(str(1))
                Reviews.append(str(x[i]))
                
            elif x[i]=="]\n]\n]\n,2,null,":
                i = i +1
                Ratings.append(str(2))
                Reviews.append(str(x[i]))
            elif x[i]=="]\n]\n]\n,3,null,":
                i = i +1
                Ratings.append(str(3))
                Reviews.append(str(x[i]))
            elif x[i]=="]\n]\n]\n,4,null,":
                i = i +1
                Ratings.append(str(4))
                Reviews.append(str(x[i]))
            elif x[i]=="]\n]\n]\n,5,null,":
                i = i +1
                Ratings.append(str(5))
                Reviews.append(str(x[i]))
        
    if(len(Reviews)>0):
        app = getAppName(soup)
        print("App:\t\t\t", app)
        App.append(app)

        numberOfRatings  = getNumberOfRatings(soup)
        print("Number of ratings:\t" , numberOfRatings)
        No_of_Rating.append(numberOfRatings)

        ratingVal = getRating(soup)
        print("Rating:\t\t\t" , ratingVal)
        Rating.append(ratingVal)

        getInstallsList = getInstalls(soup)
        print("Installs list: ",getInstallsList)

        appCategory = getCategory(soup)
        print("Category:\t\t" , appCategory)
        Category.append(appCategory)
        
        title5, title4, title3, title2,title1 = getRatingDist(soup)
        if (len(getInstallsList)==2):
            print("Size: ",getInstallsList[0])
            print("Installs: ",getInstallsList[1])
            print("Installs:\t\t" , getInstallsList[1])
            Installs.append(getInstallsList[1])
            print("Size:\t\t\t" , getInstallsList[0])
            Size.append(getInstallsList[0])

            dateUpdate = getUpdateDate(soup,2)
            #print("Date:\t\t" , dateUpdate)
            Last_updated.append(dateUpdate)
            Type.append("Paid")
            Content_Rating.append(getContentRating(soup,12))
        else:
            installs_value = getInstalls(soup)
            print("Installs:\t\t" , installs_value[0])
            Installs.append(installs_value[0])
            print("Size:\t\t\t" , getSize(soup))
            Size.append(getSize(soup))
            #print("Date:\t\t" , getUpdateDate(soup,0))
            Last_updated.append(getUpdateDate(soup,0))
            Type.append("Free")
            Content_Rating.append(getContentRating(soup,10))

        for j in range(len(Reviews)):
            test_df = pd.DataFrame({'App': App,
                                    'No_of_Rating': No_of_Rating,
                                    'Rating': Rating,
                                    'Installs': Installs,
                                    'Last Updated': Last_updated,
                                    'Size': Size,
                                    'Category': Category,
                                    'URL': Url,
                                    'Reviews': Reviews[j],
                                    'Ratings': Ratings[j],
                                    'Rating_5': title5,
                                    'Rating_4': title4,
                                    'Rating_3': title3,
                                    'Rating_2': title2,
                                    'Rating_1': title1,
                                    'Content_Rating': Content_Rating,
                                    'Type': Type})
            test_df.to_csv('SampleAppDetailsOutput.csv', header=False, mode = 'a') #run this to append the data into csv
        print (test_df)
    timeTaken = time.time() - startTime
    remainingTime = (timeTaken * (totalNumberOfURLs - index))/60
    numberOfAppsProcessed = index - startingPoint + 1
    print("Time Taken: %0.1fs | Remaining time: %0.1fm | Number of apps processed: %d\n"%(timeTaken,remainingTime,numberOfAppsProcessed))
