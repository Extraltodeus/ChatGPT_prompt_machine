# ChatGPT_prompt_machine
A simple script that turns chatGPT into a Prompt Generator for Text-to-Image Model

This is a Python script that generates prompts for a text-to-image model using OpenAI's GPT-3.5 language model. The script takes in three command line arguments:

    --sd_prompt: The description of the prompt. This should be a short sentence describing the desired image.
    --prompt_amount: The number of prompts to generate.
    --max_tokens: The maximum number of tokens in the generated prompt.

The generated prompts are saved in a text file located in a prompts folder in the same directory as the script. The filename is generated based on the prompt description given by the user.
Usage

You must have an OpenAI API key and organization ID to use this script. The API key and organization ID should be saved in text files called api_key.txt and org.txt respectively, located in the same directory as the script.

To run the script, open a terminal and navigate to the directory where the script is saved. Then, type:

    python chatgpt_prompt_machina.py --sd_prompt "Describe a summer sky. Make it short." --prompt_amount 6 --max_tokens 80

You can also edit the script to remove the command line arguments and manually set the values of SD_PROMPT, PROMPT_AMOUNT, and MAX_TOKENS. To do this, uncomment the lines in the script that set these values, and edit them accordingly.
Generated Prompts

The script generates prompts based on the user-provided description. It generates a series of prompts by asking the user to provide a single sentence that includes keywords related to the desired image, such as subject, action, emotion, background, foreground, color palette, lighting direction, and more.

The prompts are saved in a text file located in a prompts folder in the same directory as the script. The filename is generated based on the prompt description given by the user.

To install openai python module:
    pip install openai
