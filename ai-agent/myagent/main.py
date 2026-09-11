import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    print("Hello from Jeebis!")

    parser = argparse.ArgumentParser(description="Jeebis Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError("Error: API Key is missing.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )

    if response.usage is None:
        raise RuntimeError("Error: API response did not include token usage information.")

    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
