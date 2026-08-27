import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #Fetching unique users
    user_list = df['user'].unique().tolist()

    #Remove group_notification and add overall in users
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
 
    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    if st.sidebar.button("Show Analysis"):
        st.title("Top Statistics")
        num_messages, words, media, link = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        with col1: 
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)      
        with col3:
                st.header("Number of Media Messages")
                st.title(media)   
        with col4:
                st.header("Number of Links Shared")
                st.title(link)    

        # Timeline of chat
        st.title("Chat Timeline")
        col1, col2 = st.columns(2)

        with col1: 
            st.title("Monthly Timeline ")
            monthly_timeline, daily_timeline = helper.timeline(selected_user, df)
            
            fig, ax = plt.subplots()
            ax.plot(monthly_timeline['time'], monthly_timeline['message'])
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)
        
        with col2: 
            st.title("Daily Timeline")
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['date_only'], daily_timeline['message'], color = 'black')
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)


        # Finding the most active user in the group
        if selected_user == 'Overall':
            st.title("Most Active Users")
            x, per = helper.most_active_user(df)
            fig, ax = plt.subplots()
            
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color = 'blue')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(per)

        # Word Cloud

        st.title("Word Cloud of Messages")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most Common Words
        st.title("Most Common Words")
        count = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()

        ax.barh(count['Word'], count['Frequency'])
        
        st.pyplot(fig)

        # Emoji Analysis

        st.title("Emoji Analysis")

        emoji_df = helper.emoji_analysis(selected_user, df)

        col1, col2 = st.columns(2)


        with col1:
            if not emoji_df.empty:
                fig, ax = plt.subplots()
                ax.pie(emoji_df['Frequency'].head(), labels = emoji_df['Emoji'].head(), autopct = '%.2f')   
                st.pyplot(fig)
            else:
                st.write("No Emoji Sent by User") 
        with col2:
            st.dataframe(emoji_df)
        

        