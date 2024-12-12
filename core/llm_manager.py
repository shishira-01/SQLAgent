from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import Appsettings

class LLMManger:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            temperature=1,
            api_key=Appsettings.GEMINI_API_KEY
        )
    
    def get_llm(self):
        return self.llm
    
    