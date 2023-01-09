from flask import Flask,render_template,redirect,request
from datetime import datetime
from newsapi import NewsApiClient
import requests

app=Flask(__name__)

Api_key='Your api key'

#using newsclient package

@app.route('/')
def home():
    newsapi=NewsApiClient(api_key=Api_key)
    topheadlines=newsapi.get_top_headlines(sources='abc-news')
    articles=topheadlines['articles']
    news=[]
    img=[]
    desc=[]
    url=[]

    for i in range(0,len(articles)):
        myarticles=articles[i]

        news.append(myarticles['title'])
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    my_list=zip(news,img,desc,url)
    
    return render_template('base.html',context=my_list)
    

#getting different categories
@app.route('/feed',methods=['GET','POST'])
def search_feed():

    search=request.args['searches']

    today=datetime.now()

    today_date=today.strftime("%x")

    url=f'https://newsapi.org/v2/everything?q={search}&from={today_date}&sortBy=popularity&apiKey={Api_key}'

    response=requests.get(url)

    responses=response.json()

    articles=responses['articles']
    news=[]
    img=[]
    desc=[]
    url=[]

    for i in range(0,len(articles)):
        myarticles=articles[i]

        news.append(myarticles['title'])
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])

    my_list=zip(news,img,desc,url)
    
    return render_template('feed.html',context=my_list)



if __name__=='__main__':
    app.run(debug=True,port=7000)