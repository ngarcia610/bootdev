import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    print("Hello from Jeebis!")

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
                "content": "Is Jeebis a good name? Use one paragraph maximum.",
            }
        ],
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
