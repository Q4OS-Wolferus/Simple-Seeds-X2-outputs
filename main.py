import random

def generate_seed():
    """
    Generate a random Minecraft world seed for version 1.17.1.
    """
    return random.randint(-2**63, 2**63-1)

seed = generate_seed()

print(f"Your Minecraft world seed is: {seed}")