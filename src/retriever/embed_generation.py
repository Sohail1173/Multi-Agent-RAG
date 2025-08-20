from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from src.logger import logging
from pathlib import Path

def embed_docs():

    """
    This function generate the embeddings
    
    """
    try:
        loader=TextLoader("data/scipy_stats_docs.md",encoding="utf-8")
        docs=loader.load()
        logging.info("data lodded successfully")
    
    # embed_path="retriever"
        splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
        split_docs=splitter.split_documents(docs)
        embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectordb=Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
        vectordb.persist()
        logging.info(f"embeddings generated and saved in retriever")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    embed_docs()