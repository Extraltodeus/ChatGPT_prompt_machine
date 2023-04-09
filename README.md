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

### Example (you can find more in the example folder)



Request :

    "Liminal space as seen on an old VHS. Make it short."
    
Generated :

    Desolate parking lot at midnight, flickering streetlamp, low-saturation color palette, grainy texture, vanishing point perspective, Art Inspiration: David Lynch.
    Darkened hallway, flickering light, distant footsteps, sound of a door creaking, VHS tracking lines covering the frame.
    Abandoned swimming pool, flickering lights, muted color palette, hazy and distorted visuals, perpendicular lines distorting the perspective, feeling of unease, subtle sound of water dripping, Art Inspiration: David Lynch.
    Empty parking lot at night, flickering fluorescent lights, distorted audio, white noise, tracking lines.
    A flickering neon sign, desaturated color palette, low lighting intensity, and a subtle haze.
    Desaturated colors, flickering light, grainy texture, empty chairs, mid-century modern architecture, looming shadows, unclear perspective, distant chatter, VHS tracking lines, film burn effect.
    Abandoned parking garage, flickering light beams, eerie atmosphere, low saturation, grainy footage, broken sound, slow zoom in.
    Desolate school hallway, flickering lighting, dusty atmosphere, faded color palette, high contrast, warped perspective, gritty texture, tracking lines, ambiguous presence.
    Disorienting camera angle, dim monochromatic color palette, flickering light leaks, grainy film texture, warped spatial perspective, just barely lit hallway, muffled sound effects, Edward Hopper's Nighthawks inspiration.
    Abandoned gas station in the middle of nowhere, flickering light with a blue tonality, a lone figure wandering aimlessly, dusty wind swirling debris, distant sounds of a highway, high contrast deep shadows, inspired by the cinematography of David Lynch.
    Abandoned mall at night, flickering fluorescent lights, ominous atmosphere, vintage horror movie inspired color grading.
    An abandoned building hallway, flickering lighting casting shadows, muted color palette, VHS tracking distortion, heavy texture, eerie atmosphere.

![output](https://user-images.githubusercontent.com/15731540/230790695-0cf0a046-fa2e-4bb7-a3ac-8e38b88f11de.jpg)

