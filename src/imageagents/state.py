from typing_extensions import TypedDict, Optional
from typing import List, Literal


class ImageState(TypedDict):
    message: str
    refined_prompt: Optional[str]
    image_urls: List[str]
    current_step: Literal["pending", "in_progress", "completed"]  
    error: Optional[str]


