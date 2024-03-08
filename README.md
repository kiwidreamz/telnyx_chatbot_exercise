# Langchain Chatbot

## Description
This is an interactive chatbot application that utilizes the Langchain library for text retrieval and OpenAI's API for language modeling. The chatbot operates in the command line and awaits user queries, responding with the most relevant information extracted from a given documentation file. 

## Prerequisites
- Python 3.6+
- An OpenAI API key
- Langchain + other dependencies installed

## Setup and Run the Project Locally
1. **Clone the repository** 
    ```
    git clone https://github.com/YourUserName/YourRepoName.git
    ```
2. **Set up the OpenAI API key as an environment variable**
   
   For security purposes, the OpenAI API key needs to be saved as an environment variable. Depending on your operating system, the way to do this will vary. On Unix systems, you can use the `export` command:
    ```
    export OPENAI_API_KEY='YourAPIKey'
    ```
   On Windows, you can use the `setx` command in the command prompt:
    ```
    setx OPENAI_API_KEY "YourAPIKey"
    ```
    
3. **Have a `documentation.json` file in the same directory as `app.py`**
    
    This bot uses a `documentation.json` file to generate answers. The provided example uses Telnyx's documentation, which allows the bot to answer questions like:
    - "What are the SMS guidelines for Ireland?"
    - "What country uses the country code 52?"
    - "What is the MCC for Serbia?"

4. **Run the bot**
   
   Navigate to the project directory and run the `app.py` file using your Python compiler. The bot will start, and it will wait for your input in the command line.

5. **Quit the bot**
    You can stop the bot by typing "quit" at the prompt.

## Interacting with the Bot
The bot works through the command line: the bot will wait for a question, provide an answer, and then wait for another one. To close the bot application, simply write "quit" as a prompt.

## Development Challenges and Solutions

While developing this bot, I faced several challenges:

1. **Familiarity with Langchain**: I wasn't familiar with Langchain at all initially. I took some time to get familiar with it mainly by studying the Langchain documentation and watching explanatory videos and tutorials on YouTube about how chatbots work in general.

2. **Understanding of Word Vectors and Embeddings**: The concept of word vectors or embeddings was also new to me. I learned about this by reading more about Natural Language Processing (NLP) and how it is applied in building chatbots.

3. **Vector Storage**: Initially, I tried using Pinecone for vector storage but struggled with its implementation. After some trial and error, I switched to FAISS (Facebook AI Similarity Search) and found it to be much easier to get working. 

Despite these challenges, I learned a lot during the development process, and I'm proud of the chatbot that I've built.

## Source Code
For a deeper understanding of the project, you can review the source code in the `app.py` file.
