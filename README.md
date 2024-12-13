# CrewAI Weather Chatbot

A sophisticated weather chatbot powered by CrewAI, providing real-time weather updates and forecasts for any location worldwide.

## 🌟 Features

- Real-time weather information for any city
- Current conditions including temperature, humidity, and weather description
- 3-day weather forecasts
- Extreme weather alerts
- Powered by Tomorrow.io weather API
- Automated workflow using CrewAI

## 🛠️ Technology Stack

- Python 3.8+
- CrewAI for agent-based automation
- LangChain for tool management
- Tomorrow.io Weather API
- OpenAI for natural language processing

## 📁 Project Structure 

```
CrewAI_Weather_Chatbot/
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
├── main.py              # Main application file
├── config/
│   └── config.py        # Configuration settings
├── agents/
│   └── weather_agent.py # Weather agent definition
├── tools/
│   └── weather_tools.py # Weather API tools
└── tasks/
    └── weather_tasks.py # Task definitions
```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ProactiveAIAgents/CrewAI_Weather_Chatbot.git
   cd CrewAI_Weather_Chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TOMORROW_API_KEY=your_tomorrow_api_key
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## 📸 Screenshots

### Project Structure
![Screenshot 2024-12-13 at 4 24 32 PM](https://github.com/user-attachments/assets/9e93c6e9-d96e-45f6-8ab1-40c0d98f185c)
*The organized directory structure of the CrewAI Weather Chatbot*

### Weather Report Example
![Screenshot 2024-12-13 at 2 18 29 PM](https://github.com/user-attachments/assets/2194aea9-d59b-4769-ac1c-e2790c66a756)
*Sample weather report output for Miami*

### Agent Configuration
![Screenshot 2024-12-13 at 4 29 36 PM](https://github.com/user-attachments/assets/ef540c80-e26c-4162-9a33-3da6fdc48260)
*Configuration of the Weather Information Analyst agent*

## 📝 Usage

1. Start the application
2. Enter a city name when prompted
3. Receive detailed weather information including:
   - Current temperature and conditions
   - Humidity levels
   - Weather description
   - Any extreme weather warnings
   - 3-day forecast summary

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Skills Learned

- **CrewAI Development**
  - Building and orchestrating autonomous AI agents
  - Agent task delegation and coordination
  - Custom tool creation for agents

- **API Integration & Data Handling**
  - RESTful API integration with Tomorrow.io
  - JSON data parsing and manipulation
  - Error handling and API rate limiting
  - Environment variable management

- **Python Best Practices**
  - Object-oriented programming principles
  - Clean code architecture
  - Modular design patterns
  - Type hinting and documentation

- **Development Workflow**
  - Git version control
  - Environment management
  - Project structuring
  - Documentation writing

- **AI/ML Concepts**
  - Natural Language Processing (NLP)
  - Prompt engineering
  - AI agent behavior configuration
  - LLM integration and optimization
