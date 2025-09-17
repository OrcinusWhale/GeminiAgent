import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) == 1:
        print("Please provide a prompt")
        exit(1)
    verbose = False
    if len(sys.argv) > 2:
        verbose = sys.argv[2] == "--verbose"
    prompt = sys.argv[1]
    if verbose:
        print(f"User prompt: {prompt}")
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(response.text)
    usage_metadata = response.usage_metadata
    if usage_metadata is not None and verbose:
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
