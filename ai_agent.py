import requests

# === Configuration ===
API_KEY = "API KEY"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# === Chat Function ===
def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        # Send the POST request to the Groq API
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Ensure no HTTP errors
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# === Main Chat Loop ===
if __name__ == "__main__":
    print("🤖 Welcome to your Groq-powered AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        reply = get_ai_response(user_input)
        print("AI:", reply)