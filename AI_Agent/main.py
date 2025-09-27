import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        content = sys.argv[1]
        messages = [types.Content(role="user", parts=[types.Part(text=content)])]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages
        )
        print(response.text)
        prompt_token_count = response.usage_metadata.prompt_token_count
        candidates_token_count = response.usage_metadata.candidates_token_count
        print(
            f"""
              Prompt tokens: {prompt_token_count}
              Response tokens: {candidates_token_count}
              """
        )
    else:
        raise Exception("You need to run it with an argument, that has to be a string")


if __name__ == "__main__":
    main()
