import os 
from flask import Flask, render_template, jsonify, request
import random
import math
import TurboTalk_Custom

class PhysicsLearningBot:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.current_topic = None
        self.lesson = None 
        self.summary = None
        self.challenge = None
        self.quiz = []
        
        # Initialize AI chatbot
        self.chatbot = TurboTalk_Custom.turbo_talk_instance(
            company_name="Rango Productions",
            bot_name="Grav Bot", 
            behaviour="Innovative and creative physics teacher specializing in gravitation"
        )
        
        self.topics = { 
            "gravitation": [
                {
                    "name": "Universal Law of Gravitation",
                    "lesson": """The Universal Law of Gravitation describes how every mass attracts every other mass in the universe with a force that is proportional to the product of their masses and inversely proportional to the square of the distance between them.

                    Key Concepts:
                    1. **Newton's Law of Gravitation**:
                       - The formula for gravitational force is \( F = \frac{Gm_1m_2}{r^2} \), where \( F \) is the force, \( G \) is the gravitational constant, \( m_1 \) and \( m_2 \) are the masses of two objects, and \( r \) is the distance between them.

                    Real-World Application:
                    - The Earth and the Moon are attracted to each other due to gravitational force.

                    Advanced Concept:
                    - The gravitational force decreases rapidly as the distance between two objects increases.
                    """,
                    "summary": "The Universal Law of Gravitation describes how masses attract each other with a force dependent on their masses and distance.",
                    "quiz": [
                        {
                            "question": "What does the Universal Law of Gravitation state?",
                            "options": [
                                "Masses repel each other.",
                                "Gravitational force decreases with distance.",
                                "Gravitational force is independent of mass.",
                                "Gravitational force is constant at all distances."
                            ],
                            "answer": 1
                        }
                    ]
                },
                {
                    "name": "Free Fall",
                    "lesson": """Free fall occurs when an object falls under the influence of gravity alone, without any resistance from air or other forces.

                    Key Concepts:
                    1. **Acceleration Due to Gravity**:
                       - The acceleration of an object during free fall near Earth's surface is approximately \( 9.8 \, \text{m/s}^2 \).
                    
                    Real-World Application:
                    - An object dropped from a height experiences free fall, accelerating until it hits the ground.

                    Advanced Concept:
                    - The time it takes for an object to fall can be calculated using the formula \( t = \sqrt{\frac{2h}{g}} \), where \( h \) is height and \( g \) is acceleration due to gravity.
                    """,
                    "summary": """In free fall, an object accelerates towards Earth due to gravity, experiencing an acceleration of approximately \( 9.8 \, \text{m/s}^2 \).""",
                    "quiz": [
                        {
                            "question": "What is the acceleration due to gravity near Earth's surface?",
                            "options": [
                                "9.8 m/s²",
                                "10 m/s²",
                                "0 m/s²",
                                "9.8 km/s²"
                            ],
                            "answer": 0
                        }
                    ]
                },
                {
                    "name": "To Calculate the Value of \( g \)",
                    "lesson": """The value of acceleration due to gravity can be calculated by measuring the time taken for an object to fall from a known height.
                    
                    Key Concepts:
                    1. **Using Free Fall Formula**:
                       - By measuring the time \( t \) it takes for an object to fall from height \( h \), we can calculate \( g \) using the formula:
                         \[
                         g = \frac{2h}{t^2}
                         \]
                    
                    Real-World Application:
                    - Experiments to measure \( g \) help us understand Earth's gravitational pull.

                    Advanced Concept:
                    - The value of \( g \) varies slightly at different locations on Earth due to altitude and geographical factors.
                    """,
                    "summary": """The value of \( g \) can be calculated using the free fall formula, considering the time and height of the fall.""",
                    "quiz": [
                        {
                            "question": "How do you calculate the acceleration due to gravity?",
                            "options": [
                                "By measuring time and height during free fall.",
                                "By measuring weight and mass.",
                                "By calculating velocity.",
                                "By using the Universal Law of Gravitation."
                            ],
                            "answer": 0
                        }
                    ]
                },
                {
                    "name": "Mass and Weight",
                    "lesson": """Mass is the amount of matter in an object, while weight is the force exerted on an object due to gravity. The weight of an object depends on the gravitational pull at its location.
                    
                    Key Concepts:
                    1. **Mass**:
                       - Mass is a scalar quantity, measured in kilograms (kg), and does not change with location.
                    
                    2. **Weight**:
                       - Weight is a force calculated as \( W = mg \), where \( W \) is weight, \( m \) is mass, and \( g \) is the acceleration due to gravity.

                    Real-World Application:
                    - A person's mass remains the same, but their weight changes on the Moon due to lower gravity.

                    Advanced Concept:
                    - Weight varies depending on the planet or celestial body, as gravity differs.
                    """,
                    "summary": """Mass is the amount of matter, and weight is the force due to gravity. The formula for weight is \( W = mg \).""",
                    "quiz": [
                        {
                            "question": "What is the formula for weight?",
                            "options": [
                                "W = m × g",
                                "W = m ÷ g",
                                "W = g ÷ m",
                                "W = m + g"
                            ],
                            "answer": 0
                        }
                    ]
                }
            ]
        }

    def get_all_topics(self):
        topics_list = []
        for category, topics in self.topics.items():
            for topic in topics:
                topics_list.append({
                    "category": category,
                    "name": topic["name"]
                })
        return topics_list

    def get_topic_by_name(self, topic_name):
        for category, topics in self.topics.items():
            for topic in topics:
                if topic["name"] == topic_name:
                    self.current_topic = topic["name"]
                    self.lesson = topic["lesson"]
                    self.summary = topic["summary"]
                    self.challenge = topic.get("challenge", None)
                    self.quiz = topic.get("quiz", [])
                    return topic
        return None

    def get_lesson(self):
        return self.lesson

    def get_summary(self):
        return self.summary

    def get_quiz(self):
        return self.quiz

    def get_challenge(self):
        return self.challenge
        
    def get_ai_response(self, user_message):
        self.chatbot.set_user_input(user_message)
        self.chatbot.give_response()
        return self.chatbot.get_response()

app = Flask(__name__)
physics_bot = PhysicsLearningBot("PhysicsAI")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-topics', methods=['GET'])
def get_topics():
    return jsonify(physics_bot.get_all_topics())

@app.route('/get-topic/<topic_name>', methods=['GET'])
def get_topic(topic_name):
    topic = physics_bot.get_topic_by_name(topic_name)
    if topic:
        return jsonify(topic)
    return jsonify({"error": "Topic not found"}), 404

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    try:
        response = physics_bot.get_ai_response(user_message)
        
        suggestions = [
            "Can you explain this in simpler terms?",
            "Show me a practical example",
            "How does this relate to real life?",
            "What are the key equations involved?"
        ]
        
        return jsonify({
            "response": response,
            "suggestions": suggestions
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "response": "I apologize, but I'm having trouble processing your request. Could you please rephrase your question?",
            "suggestions": ["Try asking in a different way", "Ask about a specific concept", "Request a simpler explanation"]
        })

@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answers = data.get("answers", [])
    
    if physics_bot.current_topic is None:
        return jsonify({"error": "No topic loaded"}), 400

    quiz = physics_bot.get_quiz()
    
    if not quiz:
        return jsonify({"error": "No quiz available for this topic"}), 400

    correct_count = 0
    total_count = len(quiz)
    
    for index, user_answer in enumerate(user_answers):
        if index < total_count and user_answer == quiz[index]['answer']:
            correct_count += 1
    
    return jsonify({
        "correct": correct_count,
        "total": total_count,
        "message": f"You got {correct_count} out of {total_count} questions correct!"
    })

if __name__ == "__main__":
    app.run(debug=True)
