from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import Appsettings

class LLMManager:
    def __init__(self):
        try:
            self.llm = ChatGoogleGenerativeAI(
                model="models/gemini-1.5-flash-latest",
                temperature=1,
                api_key=Appsettings.GEMINI_API_KEY
            )
        except Exception as e:
            print(f"Error initializing LLM: {str(e)}")
            self.llm = None

    def get_llm(self):
        if self.llm is None:
            raise ValueError("LLM was not properly initialized")
        return self.llm