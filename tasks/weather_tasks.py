from typing import List

from crewai import Task


class WeatherTasks:
    @staticmethod
    def create_weather_report_task(agent, location: str) -> Task:
        return Task(
            description=f"""Create a comprehensive weather report for {location}.
            1. Get the current weather conditions
            2. Include temperature, humidity, and weather description
            3. Check if there are any extreme weather conditions
            4. Get a 3-day forecast
            5. Compile all information in a user-friendly format""",
            agent=agent,
            expected_output="""A detailed weather report containing:
            - Current temperature and conditions
            - Humidity levels
            - Weather description
            - Any extreme weather warnings
            - 3-day forecast summary
            The information should be formatted in a clear, easy-to-read manner.""",
        )
