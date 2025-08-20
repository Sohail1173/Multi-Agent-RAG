from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from  langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from src.logger import logging

from dotenv import load_dotenv
import os

load_dotenv()

def get_doc_answer(question:str,k:int=2) ->str:
    """
    This functions gives the answer of the question
    """
    try:
        vectordb=Chroma(
        persist_directory="chroma_db",
        embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    )   
        logging.info("VectorDB loaded successfully")
        retriever = vectordb.as_retriever(search_kwargs={"k": k})
        llm=ChatGroq(model="llama3-70b-8192",api_key=os.getenv("GROQ_API_KEY"))

    # Create a system prompt
        system_prompt= (
        "You are a helpful AI bot, specialist in statistical analysis."
        "You can answer questions using the given the SciPy documentation context."
        "Be clear and concise."
        "{context}"
    )

    # Create a prompt Template
        prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # Create a chain
    # It creates a StuffDocumentsChain, which takes multiple documents (text data) and "stuffs" them together before passing them to the LLM for processing.
        combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    
    # Creates the RAG
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    # Invoke the chain
        result = retrieval_chain.invoke({"input": question})
        return result['answer']
    except Exception as e:
     print(e)


if __name__ == "__main__":
    question = "What is the t-test used for?"
    answer = get_doc_answer(question)
    print("Answer:", answer)