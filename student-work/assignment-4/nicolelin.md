# Nicole Lin

My favorite programming language is Python because I feel it is the easiest to use. It is a high-level language, making it easy to understand!

## Example Code

```python
import random
import openai

def generate_random_space_image():
    themes = ["nebula", "galaxy", "black hole", "alien planet", "meteor shower", "star cluster", "supernova"]
    colors = ["vibrant blue", "deep purple", "fiery red", "golden", "mystical green", "icy white", "cosmic multicolor"]
    features = ["with swirling gases", "surrounded by asteroids", "illuminated by a distant quasar", "with glowing particles", "with an enormous ring system", "with a mysterious spacecraft", "with a comet streaking by"]
    
    theme = random.choice(themes)
    color = random.choice(colors)
    feature = random.choice(features)
    
    prompt = f"A breathtaking {color} {theme} {feature}, ultra-high resolution, space photography."
    
    print(f"Generated prompt: {prompt}")
    
    # Generate image using OpenAI DALL·E
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    
    image_url = response["data"][0]["url"]
    print(f"Image URL: {image_url}")
    
    return image_url

# Example usage
generate_random_space_image()

### Code Explanation

This code generates a random space-themed image using OpenAI’s DALL·E model. It begins by defining three lists containing possible space themes (such as galaxies, black holes, and nebulae), colors (like deep purple, fiery red, and icy white), and descriptive features (such as swirling gases or being surrounded by asteroids). The program randomly selects one element from each list to form a unique combination. This combination is then used to construct a descriptive text prompt, which is passed to OpenAI’s image generation API to create a space-themed image. The resulting image URL is printed to the console, allowing the user to view the AI-generated space scene. This process ensures that each generated image is unique, providing a variety of visually stunning and imaginative space landscapes. To run this, write python3 space_generator.py in your terminal. 







