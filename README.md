# 💭 Image Generation Agent + Chat Assistant 🧠✨

An intelligent multi-modal agent built with LangGraph that can both generate high-quality images and engage in conversational interactions. The agent uses advanced prompt engineering to refine your descriptions and generate stunning visuals, while also providing helpful responses to general questions.

## 🚀 Features

- **Smart Message Classification**: Automatically detects whether you want an image generated or just want to chat
- **Advanced Prompt Refinement**: Enhances basic descriptions into detailed, AI-optimized prompts for image generation
- **High-Quality Image Generation**: Uses FLUX.1-schnell-Free model for professional-grade image creation
- **Dual Functionality**: Seamlessly switches between image generation and conversational AI
- **Error Handling**: Robust error handling and recovery mechanisms
- **Interactive Interface**: Simple command-line interface for easy interaction
- **Multiple Image Output**: Generates 4 variations of your concept

## 🛠️ Installation

### Prerequisites

- Python 3.13 or higher

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/devgomesai/imageagents.git
   cd image-gen-agent
   ```
2. **Install dependencies**

   ```bash
   pip install -e .
   ```

   or using uv:

   ```bash
   uv sync
   ```
3. **Environment Configuration**

   Create a `.env` file in the project root:

   `code`

   Get your API key from [Together AI](https://together.ai/)

## 🎯 Usage

### Quick Start

Run the interactive agent:

```bash
python test.py
```

The agent will prompt you to enter a message, then:

1. **Classifies** your message as either an image request or chat
2. **For Image Requests**: Refines your description and generates 4 high-quality image variations
3. **For Chat**: Provides helpful conversational responses
4. **Displays** the results

### Example Interactions

#### Image Generation

```
💭 Enter your message: a cat sitting in a garden
```

**Output:**

- **Message Type**: `image`
- **Refined Prompt**: "A majestic cat sitting gracefully in a lush garden, surrounded by vibrant flowers and greenery, soft natural lighting, photorealistic style, shallow depth of field, high quality, detailed, 8k resolution"
- **Image URLs**: [Generated image URLs]

#### Chat Conversation

```
💭 Enter your message: What is the capital of France?
```

**Output:**

- **Message Type**: `chat`
- **AI Response**: "The capital of France is Paris. It's a beautiful city known for its rich history, culture, and iconic landmarks like the Eiffel Tower."

## 🏗️ Architecture

The project uses LangGraph to create a sophisticated workflow with intelligent routing:

### Core Components

- **`graph.py`**: Defines the main workflow graph with nodes for message classification, chat, prompt refinement, and image generation
- **`models.py`**: Handles AI model initialization (GPT-4o-mini for chat and prompt refinement, Together AI for image generation)
- **`prompts.py`**: Contains expert prompt engineering templates and chat prompts
- **`state.py`**: Manages the application state throughout the workflow

### Workflow Steps

1. **Message Classification**: Your input is analyzed to determine if it's an image request or chat
2. **Routing**: Based on classification, routes to either chat or image generation path
3. **For Images**:
   - **Prompt Refinement**: Your input is enhanced by GPT-4o-mini using expert prompt engineering techniques
   - **Image Generation**: The refined prompt generates 4 images using FLUX.1-schnell-Free
4. **For Chat**: Direct response using GPT-4o-mini
5. **Error Handling**: Robust error handling ensures graceful failure recovery

## 🔧 Configuration

### Environment Variables

- `TOGETHER_API_KEY`: Your Together AI API key (required)

### Model Configuration

The agent uses:

- **GPT-4o-mini** for chat responses and prompt refinement (temperature: 0)
- **FLUX.1-schnell-Free** for image generation (4 steps, 4 images)

## 📁 Project Structure

```
image-gen-agent/
├── src/
│   └── imageagents/
│       ├── __init__.py
│       ├── graph.py          # Main workflow definition with routing
│       ├── models.py          # AI model initialization
│       ├── prompts.py         # Prompt engineering and chat templates
│       └── state.py           # State management and message classification
├── test.py                    # Interactive demo script
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
├── my_graph.png              # Workflow visualization
└── README.md                 # This file
```

## 🎨 Prompt Engineering

The agent uses advanced prompt engineering techniques to enhance your image descriptions:

- **Visual Details**: Colors, textures, materials, and specific visual elements
- **Lighting**: Natural, dramatic, golden hour effects, and atmospheric lighting
- **Artistic Style**: Photorealistic, digital art, oil painting, and various artistic approaches
- **Composition**: Centered, rule of thirds, close-up shots, and framing techniques
- **Quality Modifiers**: High quality, detailed, sharp focus, 8k resolution
- **Technical Details**: Depth of field, lens types, and camera settings
- **Mood & Atmosphere**: Emotional and atmospheric descriptors for enhanced visual impact

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Together AI](https://together.ai/)
- Uses [GPT-4o-mini](https://openai.com/) for chat and prompt refinement
- Image generation via [FLUX.1-schnell-Free](https://huggingface.co/black-forest-labs/FLUX.1-schnell-Free)

## 🐛 Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure your `TOGETHER_API_KEY` is set in the `.env` file
2. **Python Version**: Make sure you're using Python 3.13 or higher
3. **Dependencies**: Run `pip install -e .` to install all required packages

### Getting Help

If you encounter any issues, please:

1. Check the error messages for specific details
2. Verify your API key is correct
3. Ensure all dependencies are installed
4. Open an issue on GitHub with detailed error information

---

**Happy Image Generating and Chatting! 🎨✨**
