# Speech Recognition and Generative AI Interaction

This Python project combines the power of speech recognition and generative AI to create an interactive experience. The script allows you to speak, converts your speech into text, performs a mathematical operation, and then generates creative content based on your input.

## Dependencies

Make sure you have the following dependencies installed:

- `os`
- `sys`
- `pyttsx3`
- `speech_recognition`
- `pathlib`
- `textwrap`
- `google.generativeai`

Install them using:

" pip3 install requirements.txt "


## Usage

1. Execute the script.
2. Speak into the microphone when prompted.
3. Your speech will be converted to text using Google Speech Recognition.
4. You will be asked to provide two numbers (`x` and `y`).
5. The sum of `x` and `y` will be spoken back to you.

## Additional Features

### Markdown Formatting

The project incorporates a function to format text in Markdown. The function `to_markdown(text)` replaces bullet points with asterisks and indents the text with a greater than symbol.

### Generative AI Content

The script utilizes Google's Generative AI to generate creative content based on your input. It communicates with the Gemini Pro model provided by Google. The generated content is then converted to speech and played back.

## Configuration

Before running the script, make sure to set your Google API key as the value for `GOOGLE_API_KEY` in the code.

```python
GOOGLE_API_KEY = 'Your_API_Key_Here'
```

Ensure that the dependencies are correctly installed, and you are ready to explore the interactive world of speech recognition and generative AI!
