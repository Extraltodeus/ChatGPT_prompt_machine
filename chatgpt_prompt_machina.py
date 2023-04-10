import argparse
import openai
import os

parser = argparse.ArgumentParser(description='Process command line arguments for the script.')

parser.add_argument('--sd_prompt', type=str, default='Describe a summer sky. Make it short.', help='The description of the prompt')
parser.add_argument('--prompt_amount', type=int, default=6, help='The number of prompts to generate')
parser.add_argument('--max_tokens', type=int, default=80, help='The maximum number of tokens in the generated prompt')
args = parser.parse_args()

SD_PROMPT = args.sd_prompt
PROMPT_AMOUNT = args.prompt_amount
MAX_TOKENS = args.max_tokens

# UNCOMMENT AND EDIT IF YOU WANT TO JUST RUN THE SCRIPT WITHOUT CLI
# SD_PROMPT = "Describe a summer sky. Make it short."
# PROMPT_AMOUNT = 6
# MAX_TOKENS = 80

def append_text_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)


def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def generate_message(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        max_tokens=MAX_TOKENS,
        temperature=1.1
    )
    return response


def main():
    openai.api_key = read_text_file("api_key.txt")
    openai.organization = read_text_file("org.txt")

    prompts = [
        {"role": "system", "content": "you are a filename generator that gives me a single filename based on the description given by the user. These are related to AI image generators. It is important that you only answer the filename. For example: 'describe the face of a beautiful woman' becomes: 'beautiful_woman_faces'"},
        {"role": "user", "content": SD_PROMPT}
    ]

    log_name = generate_message(prompts)['choices'][0]["message"]["content"]
    folder_name = "prompts"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    log_name = f"{len(os.listdir(folder_name)):04d}_{log_name}"
    log_path = os.path.join(folder_name, log_name + ".txt")

    print(f"filename: {log_path}")
    print("-" * 40)

    initial_prompt = """You are a prompt generator for a text-to-image model. Write in one sentence the following keywords separated by a comma. It is not mandatory to use all of the keywords when there is no coherence for the composition. Keywords: subject, action, emotion, background, foreground, midground, color palette, lighting direction, lighting intensity, lighting quality, composition, balance, contrast, depth of field, perspective, scale and proportion, texture, detail, framing and cropping, visual hierarchy, Art Inspiration (name artists or studios). You shall avoid using the keywords ('style', 'technique', 'subject' etc...) but just chain the creative keywords with ', ' (a comma and a space). For example:
a door slightly open, realistic painting, salvador dali, VHS video tape artifacts, etc..."""

    prompts = [
        {"role": "system", "content": initial_prompt},
        {"role": "user", "content": f"Generate the keywords in a single line to compose the image: '{SD_PROMPT}'. I know that this might be a short description but I'm counting on you. Be creative!"}
    ]

    for _ in range(PROMPT_AMOUNT):
        response = generate_message(prompts)['choices'][0]["message"]["content"]
        append_text_to_file(log_path, response + "\n")
        print(response)
        print("-" * 40)


if __name__ == '__main__':
    main()
