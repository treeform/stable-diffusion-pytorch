from stable_diffusion_pytorch import pipeline
from PIL import Image

prompts = ["a photograph of an astronaut riding a horse"]
input_images = [Image.open('red.png')]
images = pipeline.generate(prompts, input_images=input_images)
images[0].save('output.png')
