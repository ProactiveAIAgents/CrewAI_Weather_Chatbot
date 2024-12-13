import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TOMORROW_API_KEY = os.getenv("TOMORROW_API_KEY")

# Weather API Configuration
WEATHER_API_BASE_URL = "https://api.tomorrow.io/v4/weather/realtime"
FORECAST_API_BASE_URL = "https://api.tomorrow.io/v4/weather/forecast"
