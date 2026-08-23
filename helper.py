def fetch_stats(selected_user, df):

    if selected_user == "Overall":
        #Number of messages
        num_message  = df.shape[0]

        #Number of words
        words = []
        for message in df['message']:
            words.extend(message.split())
        return num_message, len(words)
    else:
        #Number of message
        new_df = df[df['user'] == selected_user]
        num_message = new_df.shape[0]
        #Number of words
        words = []
        for message in new_df['message']:
            words.extend(message.split())
        return num_message, len(words)