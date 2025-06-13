from flask import Flask, render_template, redirect, url_for
import json
import os

app = Flask(__name__)

# Create a function to load memory data from a JSON file
def load_memories():
    return {
            "categories": [
                {
                    "id": "first-dates",
                    "name": "Our One Month Together",
                    "description": "The best time of my life",
                    "memories": [
                        {
                            "id": "first-month",
                            "title": "Our best memories",
                            "date": "February 24, 2025",
                            "description": "",
                            "thumbnail": "static/images/coffee-date.jpg",
                            "video": "static/videos/coffee-date.mp4",
                            "featured": True
                        },
                        {
                            "id": "park-picnic",
                            "title": "Sunsets at the Beach",
                            "date": "March 24, 2025",
                            "description": "Our second date with homemade sandwiches and that perfect sunset.",
                            "thumbnail": "static/images/park-picnic.jpg",
                            "video": "static/videos/park-picnic.mp4"
                        }
                    ]
                },
                {
                    "id": "trips",
                    "name": "Our Adventures",
                    "description": "The places we've explored together",
                    "memories": [
                        {
                            "id": "beach-weekend",
                            "title": "Weekend at Crystal Beach",
                            "date": "June 12, 2023",
                            "description": "That spontaneous road trip to the coast. Remember when we built that sand castle?",
                            "thumbnail": "static/images/beach-trip.jpg",
                            "video": "static/videos/beach-trip.mp4"
                        },
                        {
                            "id": "mountain-hike",
                            "title": "Eagle's Peak Hike",
                            "date": "August 8, 2023",
                            "description": "We made it to the top despite the rain. The view was worth every step.",
                            "thumbnail": "static/images/mountain-hike.jpg",
                            "video": "static/videos/mountain-hike.mp4"
                        }
                    ]
                },
                {
                    "id": "special-moments",
                    "name": "Special Moments",
                    "description": "The little things that mean everything",
                    "memories": [
                        {
                            "id": "surprise-birthday",
                            "title": "Your Surprise Birthday",
                            "date": "March 17, 2023",
                            "description": "When all our friends helped me surprise you. Your face was priceless!",
                            "thumbnail": "static/images/birthday-surprise.jpg",
                            "video": "static/videos/birthday-surprise.mp4"
                        },
                        {
                            "id": "first-cooking",
                            "title": "First Time Cooking Together",
                            "date": "February 14, 2023",
                            "description": "Our Valentine's Day dinner disaster that still tasted perfect.",
                            "thumbnail": "static/images/cooking-together.jpg",
                            "video": "static/videos/cooking-together.mp4"
                        }
                    ]
                }
            ]
        }

# Create routes for the application
@app.route('/')
def index():
    memories_data = load_memories()
    # Find the featured memory for the hero banner
    if memories_data is None:
        exit(0)
    featured_memory = None
    for category in memories_data["categories"]:
        for memory in category["memories"]:
            if memory.get("featured", False):
                featured_memory = memory
                break
        if featured_memory:
            break
    
    # If no memory is marked as featured, use the first one
    if not featured_memory and memories_data["categories"]:
        featured_memory = memories_data["categories"][0]["memories"][0] if memories_data["categories"][0]["memories"] else None
    
    return render_template('index.html', 
                          categories=memories_data["categories"], 
                          featured_memory=featured_memory)

@app.route('/watch/<memory_id>')
def watch_memory(memory_id):
    memories_data = load_memories()
    
    # Find the memory with the given ID
    memory = None
    for category in memories_data["categories"]:
        for mem in category["memories"]:
            if mem["id"] == memory_id:
                memory = mem
                break
        if memory:
            break
    
    if not memory:
        return redirect(url_for('index'))
    
    return render_template('watch.html', memory=memory)

@app.route('/category/<category_id>')
def category(category_id):
    memories_data = load_memories()
    
    # Find the category with the given ID
    selected_category = None
    for category in memories_data["categories"]:
        if category["id"] == category_id:
            selected_category = category
            break
    
    if not selected_category:
        return redirect(url_for('index'))
    
    return render_template('category.html', 
                          category=selected_category,
                          categories=memories_data["categories"])

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('static/videos', exist_ok=True)
    app.run(debug=True)