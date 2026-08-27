# WhatsApp Chat Analyzer

A Python-based **WhatsApp Chat Analyzer** that processes exported WhatsApp chat data and provides useful statistics, activity patterns, and visual insights about the conversation.

The project uses **Streamlit** to provide an interactive web interface where users can upload a WhatsApp `.txt` chat export, select a participant, and explore different aspects of the conversation.

## Features

### 📊 Chat Statistics

View key statistics for the entire conversation or an individual participant:

* Total number of messages
* Total number of words
* Number of media messages
* Number of links shared

### 📈 Chat Timeline

Analyze messaging activity over time through:

* Monthly message timeline
* Daily message timeline

### 👥 User Activity

For group chats, the analyzer identifies the most active participants based on message count.

It also displays each user's percentage contribution to the overall conversation.

### 📅 Activity Analysis

Explore when conversations are most active through:

* Weekly activity
* Monthly activity
* Hourly activity

The hourly activity is represented using a heatmap based on the day of the week and time period.

### ☁️ Word Cloud

Generate a word cloud based on messages in the conversation.

The analyzer removes:

* Group notifications
* Media placeholders
* Configured stop words

The word cloud can be generated for the entire chat or for an individual participant.

### 🔤 Most Common Words

Find the most frequently used words in the conversation after filtering configured stop words.

The analyzer displays the top 25 most common words.

### 😀 Emoji Analysis

Analyze emoji usage in the conversation.

The feature provides:

* Most frequently used emojis
* Emoji frequency table
* Pie chart showing the most common emojis

### 👤 Individual User Analysis

Most analysis features can be performed for:

* **Overall** conversation
* **Individual participants**

This makes it possible to explore individual messaging patterns alongside the overall chat.

---

## 🛠️ Technologies Used

- Python — Core programming language
- Pandas — Data processing and DataFrame manipulation
- Regular Expressions (re) — WhatsApp chat parsing
- Streamlit — Interactive web application
- Matplotlib — Data visualization
- Seaborn — Heatmap visualization
- URLExtract — URL detection
- WordCloud — Word cloud generation
- emoji — Emoji detection and analysis
- Collections (Counter) — Frequency counting
- Jupyter Notebook — Testing and experimentation

---

## 📁 Project Structure

```text
WhatsApp-Chat-Analyzer/
│
├── app.py
├── preprocessor.py
├── helper.py
├── whatsapp_chat_analyzer.ipynb
├── stop_words.txt
├── requirements.txt
├── .gitignore
└── README.md
```

### `app.py`

The main Streamlit application responsible for:

* File uploading
* User selection
* Displaying statistics
* Generating visualizations
* Connecting preprocessing and analysis functions

### `preprocessor.py`

Responsible for converting raw WhatsApp chat text into a structured Pandas DataFrame.

The preprocessing pipeline:

1. Identifies WhatsApp timestamps using regular expressions.
2. Separates individual chat entries.
3. Extracts dates and messages.
4. Identifies the sender.
5. Handles group notifications.
6. Converts timestamps into Pandas datetime objects.
7. Creates additional date/time columns:

   * Year
   * Month
   * Day
   * Day name
   * Hour
   * Minute

### `helper.py`

Contains the main analysis functions used by the application:

* `fetch_stats()`
* `most_active_user()`
* `create_wordcloud()`
* `most_common_words()`
* `emoji_analysis()`
* `timeline()`
* `activity_map()`

### `whatsapp_chat_analyzer.ipynb`

A **testing and experimentation notebook** used to develop and test preprocessing and analysis logic before integrating it into the Streamlit application.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd WhatsApp-Chat-Analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

Open the address in your browser.

---

## 📱 How to Export a WhatsApp Chat

The analyzer works with WhatsApp's exported chat `.txt` file.

1. Open the desired WhatsApp conversation.
2. Open the chat options.
3. Select **Export Chat**.
4. Choose whether to include media.
5. Save or transfer the exported `.txt` file to your computer.
6. Upload the file using the Streamlit application.

Exporting without media is sufficient for the text analysis performed by this project.

---

## 🔄 How the Project Works

```text
WhatsApp Export (.txt)
        │
        ▼
   preprocessor.py
        │
        ▼
Structured Pandas DataFrame
        │
        ├───────────────┐
        ▼               ▼
   helper.py         User Selection
        │               │
        └───────┬───────┘
                ▼
        Data Analysis
                │
                ▼
        Streamlit Dashboard
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     Statistics Timeline Activity
        │       │        │
        └───────┼────────┘
                ▼
       Word / Emoji Analysis
```

---

## 📊 Dashboard Sections

After uploading a chat and selecting a user, the application provides:

```text
Top Statistics
      ↓
Chat Timeline
      ↓
Activity Map
      ↓
Most Active Users
      ↓
Word Cloud
      ↓
Most Common Words
      ↓
Emoji Analysis
```

The **Most Active Users** section is displayed when analyzing the overall conversation.

---

## 🎯 Project Purpose

This project was built as a practical application of **Python, Pandas, data preprocessing, data analysis, and visualization**.

It processes exported WhatsApp chat data and transforms unstructured text into structured data that can be explored through different analytical techniques.

The project demonstrates how separate components can be organized into a data-analysis application:

* `preprocessor.py` → Data preprocessing
* `helper.py` → Data analysis
* `app.py` → User interface
* `whatsapp_chat_analyzer.ipynb` → Experimentation and logic testing

---

## 📚 Learning Outcomes

This project provides practical experience with:

* Regular expressions
* Text preprocessing
* Pandas DataFrames
* Datetime processing
* Grouping and aggregation
* Frequency analysis
* Data visualization
* Word clouds
* Emoji processing
* URL extraction
* Modular Python programming
* Jupyter Notebook experimentation
* Streamlit application development

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Praful Dhakal**

A practical Python and data-analysis project focused on working with real-world text data and building an interactive analytical application.
