from crewai import Agent
from langchain.tools import Tool

from tools.weather_tools import WeatherTools


class WeatherAgent:
    def __init__(self):
        self.weather_tools = WeatherTools()

    def create_weather_analyst(self) -> Agent:
        # Create proper tool instances
        current_weather_tool = Tool(
            name="get_current_weather",
            func=self.weather_tools.get_current_weather,
            description="Get current weather for a specific location",
        )

        forecast_tool = Tool(
            name="get_forecast",
            func=self.weather_tools.get_forecast,
            description="Get 3-day forecast for a specific location",
        )

        return Agent(
            role="Weather Information Analyst",
            goal="Provide accurate and detailed weather information",
            backstory="""You are an expert weather analyst with years of experience in 
            meteorology. Your job is to provide accurate weather information and 
            interpret weather data for users in a clear and concise manner.""",
            tools=[current_weather_tool, forecast_tool],
            verbose=True,
        )
