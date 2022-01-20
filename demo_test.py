# create a collection  of news/articles having the keys as
# id,title,date,description,time
# apply operations to search based id or category of type

# news_articles = list()
# print(len(news_articles))

news_articles = [{'id':123 , 'title':'happy new year', 'date':'01-05-2022', 'description':'2022 for klu','type':'general'},
                 {'id':125 , 'title':'happy birthday', 'date':'07-08-2022', 'description':' klu','type':'sports'},
                 {'id':128 , 'title':'happy ', 'date':'01-10-2022', 'description':'rrr','type':'movies'},
                 {'id':129 , 'title':'india ', 'date':'01-12-2022', 'description':'radhe shyam','type':'software'}]
# print(type(news_articles) )
# print(len(news_articles))

# print(na)
# print(type(na))

# news_articles ={'id' :[123,125,128,129] ,'title':{} , 'date':[],}
print(type(news_articles))

for na in news_articles:
    if na.get('id') ==123:
        print(na['type'])
        print(na.get('date'))
        print(na.get('title'))
