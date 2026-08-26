from urlextract import URLExtract  # To find urls from messages
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # Number of Messages
    num_message = df.shape[0]
   
    # Number of Words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Number of Media Message
    media = df[df['message'] == "<Media omitted>"].shape[0]

    # Number of links shared
    extractor = URLExtract()
    link = []
    for message in df['message']:
        link.extend(extractor.find_urls(message))
    

    return num_message, len(words), media, len(link)
        
def most_active_user(df):
    x = df['user'].value_counts()
    per = round((df['user'].value_counts()/df.shape[0])*100 , 2).reset_index().rename(columns = {'index': 'name', 'count': 'percent'})

    return x, per

def create_wordcloud(selected_user,df):
    # open the file containing possible stopwords
    f = open("stopwords.txt",'r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # remove group notification and media files
    temp = df[df['user']!= 'group_notification']
    temp = temp[temp['message'] != "<Media omitted>"]

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep = " "))
    return df_wc

def most_common_words(selected_user,df):
    # open the file containing possible stopwords
    f = open("stopwords.txt",'r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # remove group notification and media files
    temp = df[df['user']!= 'group_notification']
    temp = temp[temp['message'] != "<Media omitted>"]
    # will hold the words not in stopwords lsit
    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    
    count = pd.DataFrame(Counter(words).most_common(25))
    count.rename(columns={0: "Word", 1: "Frequency"}, inplace=True)

    return count