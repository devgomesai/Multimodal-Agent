# 💭 Image Generation Agent 🧠✨

An intelligent image generation agent built with LangGraph that transforms your ideas into high-quality images using AI. The agent uses advanced prompt engineering to refine your descriptions and generate stunning visuals.

## 🚀 Features

- **Smart Prompt Refinement**: Automatically enhances your basic descriptions into detailed, AI-optimized prompts
- **High-Quality Image Generation**: Uses FLUX.1-schnell-Free model for professional-grade image creation
- **Error Handling**: Robust error handling and recovery mechanisms
- **Interactive Interface**: Simple command-line interface for easy interaction
- **Multiple Image Output**: Generates 4 variations of your concept

## 🛠️ Installation

### Prerequisites

- Python 3.13 or higher
- Together AI API key

### Setup

1. **Clone the repository**
   ```bash
   git clone 
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
   ```env
   TOGETHER_API_KEY=your_together_ai_api_key_here
   ```

   Get your API key from [Together AI](https://together.ai/)

## 🎯 Usage

### Quick Start

Run the interactive image generation agent:

```bash
python test.py
```

The agent will prompt you to describe what you want to see, then:
1. Refine your description using advanced prompt engineering
2. Generate 4 high-quality image variations
3. Display the results

### Example Interaction

```
💭 Enter what you are imagining 🧠✨: a cat sitting in a garden
```

**Output:**
- **User Message**: "a cat sitting in a garden"
- **Refined Prompt**: "A majestic cat sitting gracefully in a lush garden, surrounded by vibrant flowers and greenery, soft natural lighting, photorealistic style, shallow depth of field, high quality, detailed, 8k resolution"
- **Image URLs**: [Generated image URLs]

## 🏗️ Architecture

The project uses LangGraph to create a workflow with the following components:

### Core Components

- **`graph.py`**: Defines the main workflow graph with nodes for prompt refinement and image generation
- **`models.py`**: Handles AI model initialization (Claude 3.5 Sonnet for prompt refinement, Together AI for image generation)
- **`prompts.py`**: Contains the expert prompt engineering template
- **`state.py`**: Manages the application state throughout the workflow

### Workflow Steps

1. **Prompt Refinement**: Your input is enhanced by Claude 3.5 Sonnet using expert prompt engineering techniques
2. **Image Generation**: The refined prompt is used to generate 4 images using FLUX.1-schnell-Free
3. **Error Handling**: Robust error handling ensures graceful failure recovery

## 🔧 Configuration

### Environment Variables

- `TOGETHER_API_KEY`: Your Together AI API key (required)

### Model Configuration

The agent uses:
- **Claude 3.5 Sonnet** for prompt refinement (temperature: 0)
- **FLUX.1-schnell-Free** for image generation (4 steps, 4 images)

## 📁 Project Structure

```
image-gen-agent/
├── src/
│   └── imageagents/
│       ├── __init__.py
│       ├── graph.py          # Main workflow definition
│       ├── models.py          # AI model initialization
│       ├── prompts.py         # Prompt engineering templates
│       └── state.py           # State management
├── test.py                    # Interactive demo script
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
└── README.md                 # This file
```

## 🎨 Prompt Engineering

The agent uses advanced prompt engineering techniques to enhance your descriptions:

- **Visual Details**: Colors, textures, materials
- **Lighting**: Natural, dramatic, golden hour effects
- **Artistic Style**: Photorealistic, digital art, oil painting
- **Composition**: Centered, rule of thirds, close-up shots
- **Quality Modifiers**: High quality, detailed, sharp focus, 8k
- **Technical Details**: Depth of field, lens types
- **Mood & Atmosphere**: Emotional and atmospheric descriptors

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
- Uses [Claude 3.5 Sonnet](https://www.anthropic.com/claude) for prompt refinement
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
### 🔄 Agent Response

- **User Message**: `A man in the future`

- **Refined Prompt**:

  > A sleek cybernetic man in a neon-lit metropolis, wearing a form-fitting graphene suit with iridescent panels, holographic interface displays floating around him, photorealistic digital art, dramatic rim lighting with cyan and magenta accent lights, ultra-detailed facial features with subtle bio-mechanical augmentations, shallow depth of field with background bokeh effects, cinematic composition following rule of thirds, reflective chrome and glass surfaces, volumetric fog adding atmosphere, 8K resolution, hyperdetailed, sharp focus on face, ray-traced lighting, moody and atmospheric, high contrast, architectural elements with clean geometric lines in background, professional color grading, cinematic aspect ratio

![Futuristic Man](https://api.together.ai/shrt/sMAlyOqpb0PlVJCX)

---

### 🧠 Why This Prompt Works

- **Material Detailing**: Graphene, chrome, glass create realism  
- **Futuristic Cues**: Cybernetic, holograms, bio-augmentations  
- **Lighting Mastery**: Rim lighting, neon accents, ray-tracing  
- **Photographic Precision**: Shallow DOF, bokeh, rule of thirds  
- **Cinematic Mood**: Volumetric fog, moody contrast, color grading  
- **Styling & Resolution**: 8K sharpness, photorealism, high detail

**Happy Image Generating! 🎨✨**
-- Demo
-- 
