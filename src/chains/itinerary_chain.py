from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY, MODEL_NAME
from typing import List
from src.utils.logger import get_logger

logger = get_logger(__name__)

llm = ChatGroq(
    api_key = GROQ_API_KEY,
    model_name = MODEL_NAME,
    temperature = 0.3,

)


itinerary_prompt = ChatPromptTemplate([
("system", "You are a helpful travel assistant. create a day trip itinerary for {city} based on user's intereset : {interests}. Provide a brief, bulleted itinerary"),
("human", "Create a itinerary for my day trip ")
])



def generate_itineary(city: str, interests: List[str]) -> str:
    logger.info(f"before llm {city} and {interests}")
    response = llm.invoke(
        itinerary_prompt.format_messages(city = city, interests= ', '.join(interests))
    )

    # logger.info(f" {response}")

    return response.content




