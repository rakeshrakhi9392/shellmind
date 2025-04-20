import openai
import sys
import config
from colorama import Fore, Back, Style

# Set your OpenAI API key here
openai.api_key = config.api_key

def chat_with_gpt(prompt: str) -> str:
    generated_text = ""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a code assistant, respond only with the code without explanation"},
            {"role": "user", "content": prompt}
        ],
        stream=True  # Enable streaming
    )

    try:
        # Print the "Sage:" prompt at the beginning

        response_text = ""

        for chunk in response:
            delta_content = chunk['choices'][0]['delta'].get('content', '')
            if delta_content:
                # Print subsequent responses on the same line
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX + delta_content, end='', flush=True)
                response_text += delta_content
        print(Style.RESET_ALL)
        return response_text

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = str(sys.argv[2])
        with open(filename, "w") as output_file:
            user_input = " ".join(sys.argv[3:])
            response_text = chat_with_gpt(user_input)
            output_file.write(response_text)
            print(f"\nResponse saved to {filename}")
    else:
        user_input = " ".join(sys.argv[1:])
        response_text = chat_with_gpt(user_input)
