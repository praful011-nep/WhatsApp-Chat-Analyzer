def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # Number of Messages
    num_message = df.shape[0]
   
    # Number of Words

    words = []
    for message in df['message']:
        words.extend(message.split())

    return num_message, len(words)
        

