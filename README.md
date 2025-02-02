# **Summarizer**

Project Overview

This is a beginner-level coding project designed to help practice fundamental coding skills at the start of my machine learning journey. The project focuses on extracting and summarizing content from a given news article or webpage URL. It leverages libraries like Flask, nltk, and newspaper to perform the task of summarization.

Features

- URL Content Extraction: The program extracts written material from a provided webpage URL.
- Text Parsing: The text is parsed to handle whitespaces and structure it in a meaningful way.
- Natural Language Processing (NLP): Using NLP techniques, the program deduces key information from the extracted text, including the title, author, and a summarized version of the content.
- User Interface: Flask is used to create a simple webpage for inputting URLs and displaying the summarized content.

Libraries Used

- Flask: Used to create a basic webpage for inputting the article URL and displaying the result.
- nltk (Natural Language Toolkit): Provides functions for natural language processing, such as text tokenization and summarization.
- newspaper3k: Used to extract the article content from a URL, parsing the text for further analysis.
- Bootstrap: Used to create a basic webpage design.

How It Works

1. Extracting Content: The user provides a URL to a news article or webpage. The program uses the `newspaper3k` library to extract the content of the article.
2. Text Parsing: The extracted content is parsed to handle formatting issues like excess whitespace.
3. NLP Summarization: After cleaning and structuring the text, the program uses NLP techniques (from `nltk` and related libraries) to generate a title, identify the author, and summarize the article's main points.
4. Displaying Results: The summarized information, including the title, author, and summary, is displayed through the Tkinter-based GUI.

Objective

The goal of this project is to introduce and practice basic concepts in programming, natural language processing, and web scraping. This beginner project serves as an excellent first step into machine learning and NLP tasks.
