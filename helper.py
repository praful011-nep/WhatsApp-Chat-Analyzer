from urlextract import URLExtract  # To find urls from messages
import matplotlib.pyplot as plt

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
