from langchain import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
import logging

logging.getLogger("langchain").setLevel(logging.ERROR)

openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

loader = TextLoader("documentation.json", encoding="utf-8")
data = loader.load()

text_splitter = CharacterTextSplitter(
    separator="}",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

docsearch = FAISS.from_documents(texts, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=docsearch.as_retriever()
)


def main():
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        print(qa.run(user_input))


if __name__ == "__main__":
    main()
