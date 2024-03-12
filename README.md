# Chatbot Application

A simple chatbot application built using Flask, designed to respond to user messages based on predefined intents. The chatbot uses fuzzy string matching to understand user input and provide relevant responses.

## Features

- **Greeting Detection**: Recognizes common greetings in user messages.
- **Intent Matching**: Utilizes fuzzy string matching to identify user intents.
- **Randomized Responses**: Provides random responses associated with the matched intent.
- **Web Interface**: Offers a basic web interface for user interaction.

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KanmegneTabouguie/chatbotcasino.git
   cd chatbot
   ```

2. **Install Dependencies**

   Ensure you have Python installed. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python app.py
   ```

   Visit [http://127.0.0.1:5018](http://127.0.0.1:5018) in your browser to interact with the chatbot.

## Project Structure

- **`app.py`**: Main Flask application file.
- **`data.json`**: Contains predefined intents and responses.
- **`templates/index.html`**: HTML template for the chat interface.

## Usage

1. Access the chat interface by visiting [http://127.0.0.1:5018](http://127.0.0.1:5018) in your browser.

2. Enter your message in the input field and submit.

3. The chatbot will respond based on recognized intents or provide a default message if no match is found.

## Customization

- **Add/Modify Intents**: Update the `data.json` file with your own intents and associated patterns/responses.
- **Adjust Threshold**: Modify the similarity threshold in `app.py` to fine-tune string matching.

## Dependencies

- Flask
- fuzzywuzzy

## Issues and Contributions

Feel free to open issues or contribute to the project. Your feedback and suggestions are highly appreciated!

**Happy chatting!**
