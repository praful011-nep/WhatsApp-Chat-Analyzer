import re
import pandas as pd

def preprocess(data):

    # Timestamp format
    date_pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s*[\u202f ]?(?:am|pm|AM|PM))?"

    # Match every WhatsApp entry, including group notifications
    entry_pattern = (
        r"(?s)^("
        + date_pattern +
        r")\s-\s(.*?)"
        r"(?=\n" + date_pattern + r"\s-\s|\Z)"
    )

    entries = re.findall(entry_pattern, data, flags=re.M)

    # Create dataframe
    messages = [msg for _, msg in entries]

    dates = [
        re.sub(r"\s*(?:am|pm|AM|PM)$", "", d.replace("\u202f", " "))
        for d, _ in entries
    ]

    df = pd.DataFrame({
        "message": messages,
        "date": dates
    })

    # Convert date to datetime
    df["date"] = pd.to_datetime(
        df["date"],
        format="mixed",
        dayfirst=True
    )

    # Separate user and message
    users = []
    messages = []

    for message in df["message"]:

        # Normal message:- sender: message
        match = re.match(r"^([^:]+):\s(.*)$", message, flags=re.S)

        if match:
            users.append(match.group(1))
            messages.append(match.group(2))

        # Group notification
        else:
            users.append("group_notification")
            messages.append(message)

    df["user"] = users
    df["message"] = messages

    # Column for each date/time component
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    return df