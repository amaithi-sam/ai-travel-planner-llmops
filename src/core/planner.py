from langchain_core.messages import HumanMessage, AIMessage 
from src.chains.itinerary_chain import generate_itineary 
from src.utils.logger import get_logger 
from src.utils.custom_extension import CustomException 

logger = get_logger(__name__)

class TravelPlanner:

    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests:list
        self.intineary = ""

        logger.info("initialized TravelPlanner instance ")


    def set_city(self, city:str):
        try:
            self.city = city 
            self.messages.append(HumanMessage(content=city))
            logger.info("city set successfully")

        except Exception as e:
            logger.error(f"error while setting city : {e} ")
            raise CustomException("Failed to set city", e)
        
    
    def set_interests(self, interests_str:str):

        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            
            logger.info(f"interests {self.interests}")

            self.messages.append(HumanMessage(content=interests_str))

            logger.info("Internet also set successfully..")

        except Exception as e:
            logger.error(f"error while setting interests : {e}")
            raise CustomException("Failed to set interest", e)
        
    def create_itineary(self):
        try:
            logger.info(f"Generating  itineary for {self.city} and for interests {self.interests}")
            itineary = generate_itineary(self.city, self.interests)

            self.itineary = itineary 
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itineary generated successfully ")

            return itineary 
        except Exception as e:
            logger.error(f"error while creating itineary : {e}")
            raise CustomException("Failed to create itineary", e) 
        



