from crewai import Crew

from agents.weather_agent import WeatherAgent
from tasks.weather_tasks import WeatherTasks


def get_weather_report(location: str) -> str:
    # Initialize the weather agent
    weather_agent = WeatherAgent()
    analyst = weather_agent.create_weather_analyst()

    # Create the weather report task
    tasks = [WeatherTasks.create_weather_report_task(analyst, location)]

    # Create and run the crew
    crew = Crew(agents=[analyst], tasks=tasks, verbose=True)

    result = crew.kickoff()
    return result


if __name__ == "__main__":
    while True:
        location = input("\nEnter a city name (or 'quit' to exit): ")
        if location.lower() == "quit":
            break

        try:
            weather_report = get_weather_report(location)
            print(f"\nWeather Report:\n{weather_report}")
        except Exception as e:
            print(f"Error: {str(e)}")
