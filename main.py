#!/usr/bin/python3 
#shebang . interpreter directive

#  pip install transformers
# to run from terminal, python3 main.py

from transformers import pipeline
import json
import os
import yaml


def startup():

    # Prompt the LLM with a starting sentence
    prompt = "Once upon a time, there was a brave knight..."
    # Initialize the text generation pipeline
    text_generator = pipeline("text-generation")

    # Generate text based on the prompt
    generated_text = text_generator(prompt)

    # Print the generated text
    print(generated_text[0]["generated_text"])

try:
   
    startup()
except Exception as error:
    print("An exception occurred",error)
finally:
    print("Exit")