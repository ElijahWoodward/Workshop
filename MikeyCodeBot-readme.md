# ChatGPT API Interaction Script

## Overview

This Python script is designed to interact with the OpenAI GPT-4 model using the OpenAI API. It provides a command-line interface for users to chat with a virtual assistant named "Mikey", which is a customized instance of ChatGPT.

## Dependencies

- `openai`: The OpenAI Python client library, used to interact with the OpenAI API.

## How It Works

1. **API Key Initialization**: The script starts by importing necessary libraries (`openai` and `os`). It defines a function `chat_with_gpt` that takes two arguments: `api_key` and `prompt`.

2. **Setting Up the Chat**: Inside the `chat_with_gpt` function, the provided `api_key` is used to authenticate with the OpenAI API. The function then creates a chat completion request to the GPT-4 model.

3. **Customized Chat Model**: The request includes a series of preset messages that define the role and personality of the virtual assistant "Mikey". These messages are:
    - A system message informing that the user is chatting with ChatGPT.
    - A system message detailing Mikey's characteristics, such as being a brilliant coding assistant and persistent in understanding user requests.

4. **Processing User Input**: The user's input (provided as `prompt`) is added to the messages, and a request is made to the OpenAI API to generate a response.

5. **Response Handling**: The response from the API is formatted and returned. It contains only the content of Mikey's message, stripped of any additional metadata.

6. **Main Loop**: In the `main` section, the script prompts the user to enter their API key and starts a loop where the user can interact with Mikey. The user types in their message, and Mikey responds accordingly. Typing 'exit' will break the loop and end the conversation.

7. **Conversation Interface**: The script provides a simple command-line interface for the conversation. The prompt "You: " appears for the user to type their message, and Mikey's responses are prefixed with "Mikey: ".

## Usage

To use this script:
1. Ensure you have the `openai` Python library installed.
2. Replace `"API key goes here"` with your actual OpenAI API key.
3. Run the script in a Python environment.
4. Interact with Mikey by typing your messages at the prompt. Type 'exit' to end the session.

## Note

- This script is a basic demonstration of interacting with the OpenAI GPT-4 model and can be expanded or modified for more complex applications.
- The `max_tokens` parameter in the chat completion request is set to 8000, which can be adjusted based on the desired verbosity of the responses.
