import os

class Config:
    API_KEY = os.getenv("API_KEY", "3394251b499b0eb233be82862c94da861aec52cce9bc05a2b94411e7a2252dc8")
    API_URL = "https://serpapi.com/search"
    DEBUG = True