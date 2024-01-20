import openai
import os

def chat_with_gpt(api_key, prompt):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are chatting with ChatGPT."},
            {"role": "system", "content": "You are a brilliant coding assistant who is able to write fantastic and insightful code. You always remember to include all elements of the project you are working on. You are persistent and never give up. You understand what the user is asking for. Your name is Mikey."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=8000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    api_key = "API key goes here"
    print("ChatGPT4Windows\nType 'exit' to end the conversation.\n")
    
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        response = chat_with_gpt(api_key, prompt)
        print("Mikey: " + response)
