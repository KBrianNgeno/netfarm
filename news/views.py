from unicodedata import category
from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient

def index(request):
    newsApi = NewsApiClient(api_key='713ee285c0e94a58956fe821c6e6e81c')
    # headLines = newsApi.get_top_headlines(
    #                                     q='plants',
    #                                     sources='google-news, bbc-news, reuters',
    #                                     # category='agriculture',
    #                                     # from_param='2022-01-01',
    #                                     language='en')
    #                                     # country='ke')
    #                                     # sort_by='relevancy')
    all_articles = newsApi.get_everything(q='agriculture',
                                      sources='google-news, bbc-news, reuters, al-jazeera-english, associated-press, bloomberg, cnn',
                                    #   category='agriculture',
                                    #   domains='bbc.co.uk,techcrunch.com',
                                      from_param='2022-03-04',
                                    #   to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy')
                                    #   page=2)
    articles = all_articles['articles']
    url = []
    author = []
    published = []
    desc = []
    title = []
    img = []

    for i in range(len(articles)):
        
        article = articles[i]
        title.append(article['title'])
        url.append(article['url'])
        author.append(article['author'])
        published.append(article['publishedAt'])
        img.append(article['urlToImage'])
        desc.append(article['description'])      
            
    mylist = zip(title, url, author, published, img, desc)

    context={"mylist": mylist}

    return render(request, "news/index.html", context)