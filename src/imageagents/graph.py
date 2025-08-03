from typing_extensions import TypedDict, Optional
from typing import List, Literal
from langgraph.graph import START, END, StateGraph
from .state import ImageState
from .models import get_chat_model, get_image_gen_client
from .prompts import CREATE_IMAGE_PROMPT



def refine_user_prompt(state: ImageState) -> ImageState:
    """
    Refines the user's message into an optimized prompt for image generation.
    """
    try:
        llm = get_chat_model()    
        prompt = CREATE_IMAGE_PROMPT + state["message"]
        response = llm.invoke(prompt)
        
        return {
            **state,
            "refined_prompt": response.content,
            "current_step": "in_progress",
            "error": None
        }
    except Exception as e:
        return {
            **state,
            "current_step": "pending",
            "error": f"Error refining prompt: {str(e)}"
        }


def generate_images(state: ImageState) -> ImageState:
    """
    Generates images using the refined prompt.
    """
    try:
        if not state["refined_prompt"]:
            raise ValueError("No refined prompt available")
            
        image_client = get_image_gen_client()
        
        image_url = image_client.images.generate(
            prompt=state["refined_prompt"],
            model="black-forest-labs/FLUX.1-schnell-Free",
            steps=4,
            n=4
        )
        
        return {
            **state,
            "image_urls": image_url,
            "current_step": "completed",
            "error": None
        }
    except Exception as e:
        return {
            **state,
            "current_step": "in_progress",
            "error": f"Error generating images: {str(e)}"
        }


def handle_error(state: ImageState) -> ImageState:
    """
    Handles errors in the image generation process.
    """
    return {
        **state,
        "current_step": "pending",
        # Keep the existing error message
    }


# Create the graph
def create_image_generation_graph():
    """
    Creates and returns the image generation workflow graph.
    """
    workflow = StateGraph(ImageState)
    
    # Add nodes
    workflow.add_node("refine_prompt", refine_user_prompt)
    workflow.add_node("generate_images", generate_images)
    workflow.add_node("handle_error", handle_error)
    
    # Define edges
    workflow.add_edge(START, "refine_prompt")
    
    # Conditional edge after refining prompt
    workflow.add_conditional_edges(
        "refine_prompt",
        lambda state: "generate_images" if not state.get("error") else "handle_error"
    )
    
    # Edge from generate_images to end
    workflow.add_conditional_edges(
        "generate_images",
        lambda state: "end" if not state.get("error") else "handle_error"
    )
    
    # Edge from error handler back to start or end
    workflow.add_conditional_edges(
        "handle_error",
        lambda state: "end"  
    )
    
    workflow.add_edge("generate_images", END)
    workflow.add_edge("handle_error", END)
    
    return workflow.compile()
