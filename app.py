import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

# LLM Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

# Output Parser
output_parser = StrOutputParser()

# Create the LangChain Chain
chain = prompt | llm | output_parser


# --- Streamlit Front-end ---

st.title("Simple GenAI Chatbot")
st.write("This chatbot uses LangChain and Google's Gemini to answer your questions.")

# Input box for user's question
user_question = st.text_input("Ask me anything:")

if user_question:
    st.write("Thinking...")
    # Invoke the LangChain chain with the user's question
    response = chain.invoke({"question": user_question})
    st.write("Answer:")
    st.write(response)