from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import OpenAIModerationChain
from langchain.chains import OpenAIModerationChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI
import logging

load_dotenv()
logger = logging.getLogger('django')

def get_openai_moderation_client():
    moderate = OpenAIModerationChain()
    logger.info("OpenAI Moderation client initialised")
    return moderate

def moderate_user_message(content):
    moderate = get_openai_moderation_client()

def get_openai_embedding_client():
    logger.info("OpenAI Embedding client initialised")
    return OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)

def get_embedding(content, embedding_client):   
    embedding = embedding_client.embed_query(content)
    logger.info("Text converted to embeddings")
    return embedding

def get_openai_llm_client():
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=500,
        timeout=None,
        max_retries=2,
    )
    logger.info("OpenAI LLM client initialised")
    return llm