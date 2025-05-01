# idea_generator.py

import random
from config import USE_GPT, OPENAI_API_KEY

# Optionally import OpenAI
if USE_GPT:
    import openai
    openai.api_key = OPENAI_API_KEY

fallback_ideas = {
    "startup": ["An app for pet tracking", "AI-powered resume builder"],
    "novel": ["A time traveler stuck in a loop", "A parallel world ruled by cats"],
    "business": ["A subscription box for socks", "Eco-friendly packaging startup"],
    "game": ["Puzzle game that teaches coding", "VR adventure with emotions"],
    "Smart Project": ["Optimize traffic light timings based on real-time traffic."],
    "Voice Project": ["Control home appliances using voice commands."],
    "Education Project": ["An AI-powered tutor for personalized learning."],
   "Finance Project": ["Predict stock market trends using AI models."], 
   "Security Project": ["Detect anomalies in surveillance footage using AI."], 
   "Eco Project": ["Use AI for smart waste segregation and management."],
   "Emergency Response Project": ["AI-based disaster relief coordination."],
   "Mental Health Project": ["AI-powered chatbot for emotional support."], 
    "Robotics Project": ["AI-powered assistant robot with gesture recognition."],
    "Smart City Project":["AI-based smart energy distribution.","smart city"],
    "Retail Project":["Smart inventory system using AI-driven forecasting."],
    "Weather Project":["AI-based early warning system for natural disasters."],
    "Agriculture Project":["AI-assisted crop disease detection via drones."],
    "Healthcare Project":["Automated patient monitoring using AI."],
    "Communication Project":[ "Real-time speech translation AI."],
    "Food Project":[ "AI-powered food recommendation system based on nutrition."],
}

def generate_idea(category):
    category = category.lower()
    if USE_GPT:
        try:
            prompt = f"Give a creative and innovative idea for a {category}."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error using GPT: {str(e)}"

    # Fallback if not using GPT
    return random.choice(fallback_ideas.get(category, ["Think outside the box!"]))