# idea_storage.py

import json
import os
from datetime import datetime

IDEA_FILE = "ideas.json"

def save_idea(category, idea):
    data = load_ideas()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"category": category, "idea": idea, "time": timestamp}
    data.append(entry)

    with open(IDEA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_ideas():
    if not os.path.exists(IDEA_FILE):
        return []
    with open(IDEA_FILE, "r") as f:
        try:
            data=json.load(f)
            for idea in data:
                 if "time" not in idea:
                  idea["time"]="no time provided"
            return data 
        except json.JSONDecodeError:
            return []
        
def clear_all_ideas():
 with open(IDEA_FILE,"W") as f:
     json.dump([], f)
     