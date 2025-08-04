from typing_extensions import TypedDict, Optional
from typing import List, Literal
from langchain_core.runnables.graph import MermaidDrawMethod
from langgraph.graph import START, END, StateGraph
from .state import ImageState, MessageClassifier
import os
from .models import get_chat_model, get_image_gen_client
from .prompts import CREATE_IMAGE_PROMPT


def chat_agent(state: ImageState) -> ImageState:
    print('--- Chatting Based on Router ---')
    last_message = state['message'][-1]
    
    messages = [
        {
            "role": "system",
            "content": """
            You are an intelligent chat bot that helps answer user queries
            """ 
        },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    
    llm = get_chat_model()
    resp = llm.invoke(messages)
    
    return {
        "message": [{"role": "assistant", "content": resp.content}],
        "current_step": "completed"
    }


def refine_user_prompt(state: ImageState) -> ImageState:
    try:
        print('--- Refining Prompt for Image Generation ---')
        llm = get_chat_model()    
        
        last_message = state["message"][-1]
        user_content = last_message.content if hasattr(last_message, 'content') else str(last_message)
        
        
        prompt = f"{CREATE_IMAGE_PROMPT}\n\nUser request: {user_content}"
        response = llm.invoke(prompt)
        
        return {
            "refined_prompt": response.content,
            "current_step": "in_progress",
            "error": None
        }
    except Exception as e:
        return {
            "current_step": "error",
            "error": f"Error refining prompt: {str(e)}"
        }


def generate_images(state: ImageState) -> ImageState:
    try:
        if not state.get("refined_prompt"):
            raise ValueError("No refined prompt available")
            
        image_client = get_image_gen_client()
        
        
        image_response = image_client.images.generate(
            prompt=state["refined_prompt"],
            model="black-forest-labs/FLUX.1-schnell-Free",
            steps=4,
            n=4
        )
        
        
        image_url = []
        if hasattr(image_response, 'data'):
            # get the image url from json
            image_url = [img.url for img in image_response.data if hasattr(img, 'url')]
        else:
            image_url = [str(image_response)]
        
        return {
            "image_url": image_url,
            "current_step": "completed",
            "error": None,
            "message": [{"role": "assistant", "content": "Generated images successfully!"}]
        }
    except Exception as e:
        return {
            "current_step": "error",
            "error": f"Error generating images: {str(e)}"
        }


def handle_error(state: ImageState) -> ImageState:
    
    error_message = state.get("error", "An unknown error occurred")
    
    return {
        "message": [{"role": "assistant", "content": f"Sorry, I encountered an error: {error_message}"}],
        "current_step": "completed",
        "error": None  
    }


def classify_message(state: ImageState) -> ImageState:

    last_msg = state["message"][-1]
    
    
    content = last_msg.content 
    
    classifier_llm = get_chat_model().with_structured_output(MessageClassifier)
    
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """
            Classify the user message as either:
            - 'image': if user asks for an image to generate, words like create, generate, draw, make an image, etc.
            - 'chat': if user asks for facts, information, solutions, or general conversation
            """
        },
        {
            "role": "user",
            "content": content
        }
    ])
    
    return {
        "message_type": result.message_type
    }


def route_decision(state: ImageState) -> str:

    message_type = state.get("message_type", "chat")
    
    if message_type == "image":
        return "refine_prompt"
    else:
        return "chat"


def error_check(state: ImageState) -> str:
    
    if state.get("error"):
        return "handle_error"
    elif state.get("current_step") == "in_progress":
        return "generate_images"
    else:
        return "end"


def completion_check(state: ImageState) -> str:

    if state.get("error"):
        return "handle_error"
    else:
        return "end"


def create_image_generation_graph():
    
    workflow = StateGraph(ImageState)
    
    # Nodes
    workflow.add_node("classify_message", classify_message)
    workflow.add_node("chat_agent", chat_agent)
    workflow.add_node("refine_prompt", refine_user_prompt)
    workflow.add_node("generate_images", generate_images)
    workflow.add_node("handle_error", handle_error)
    
    # Start
    workflow.add_edge(START, "classify_message")
    
    # Route based on type of msg
    workflow.add_conditional_edges(
        "classify_message",
        route_decision,
        {
            "chat": "chat_agent",
            "refine_prompt": "refine_prompt"
        }
    )
    
    # Chat agent goes directly to end
    workflow.add_edge("chat_agent", END)
    
    # After refining prompt, check for errors
    workflow.add_conditional_edges(
        "refine_prompt",
        error_check,
        {
            "generate_images": "generate_images",
            "handle_error": "handle_error",
        }
    )
    
    workflow.add_conditional_edges(
        "generate_images",
        completion_check,
        {
            "handle_error": "handle_error",
            "end": END
        }
    )
    
    workflow.add_edge("handle_error", END)
    
    return workflow.compile()

def save_graph(graph, file_name="workflow.png"):
    try:
        graph_img = graph.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API)
        directory = os.path.dirname(file_name)
        
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        with open(file_name, "wb") as file:
            file.write(graph_img)
            
        print(" -- Saved the Workflow --")
        return True
    except Exception as e:
        print(e)