import re
import pandas as pd

def preprocess(data):

    #Timestamp format
    date_pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s(?:am|pm|AM|PM))?"    #Full Chat entry timestamp -sender: message
    entry_pattern = (
        r"(?s)^" +
        r"(" + date_pattern + r")" +
        r"\s-\s([^:]+):\s(.*?)" +
        r"(?=\n" + date_pattern + r"\s-\s[^:]+:\s|\Z)"
    )

    entries = re.findall(entry_pattern, data, flags=re.M)
    messages = [f"{name}: {msg}" for _, name, msg in entries]
    dates = [
        re.sub(r"\s(?:am|pm|AM|PM)$", "", d.replace("\u202f", " ")) + " - "
        for d, _, _ in entries
    ]
    #Dataframe of all chat data
    df = pd.DataFrame({"user_message": messages, "message_date": dates})
    clean_dates = df["message_date"].str.replace(r"\s-\s$", "", regex=True)
    #Converts column data into actual datetime object
    df["message_date"] = pd.to_datetime(clean_dates, format="mixed", dayfirst=True)
    df.rename(columns={"message_date": "date"}, inplace=True)

    #Seperate user and message
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)   

    #Column for each in data and time
    df['year']= df['date'].dt.year
    df['month'] =df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df