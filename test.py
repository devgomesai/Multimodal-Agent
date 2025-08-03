import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from imageagents import create_image_generation_graph

workflow = create_image_generation_graph()
print('-'*50)
user_message = str(input("💭 Enter what you are imagining 🧠✨: "))
print('-'*50)
response = workflow.invoke({"message": user_message})
print("User-Message: ", response["message"])
print()
print("Refined Prompt: ", response["refined_prompt"])
print()
print("Image Data: ", response["image_urls"])

