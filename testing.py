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
            "basic_gravitation": [
                {
                    "name": "Newton's Law of Universal Gravitation",
                    "lesson": """Newton's Law of Universal Gravitation is a fundamental principle that describes the gravitational force between all masses in the universe.

                    Key Concepts:
                    1. The Universal Gravitational Constant (G):
                       - G = 6.674 × 10⁻¹¹ N(m/kg)²
                       - This constant is the same throughout the universe
                       - Determines the strength of gravitational force

                    2. Key Equation:
                       F = G(m₁m₂/r²)
                       where:
                       - F is the gravitational force
                       - m₁ and m₂ are the masses of the objects
                       - r is the distance between their centers

                    3. Important Facts:
                       - Force decreases with square of distance
                       - Force is always attractive
                       - Applies to all objects with mass

                    Real-world Applications:
                    - Planetary orbits
                    - Satellite motion
                    - Tidal forces
                    """,
                    "summary": "Newton's Law explains how objects with mass attract each other, with strength depending on their masses and distance.",
                    "quiz": [
                        {
                            "question": "What does Newton's Law of Universal Gravitation describe?",
                            "options": [
                                "The motion of planets",
                                "The gravitational force between two masses",
                                "The speed of light",
                                "The shape of the Earth"
                            ],
                            "answer": 1
                        },
                        {
                            "question": "What happens to gravitational force as distance increases?",
                            "options": [
                                "It increases",
                                "It decreases",
                                "It remains constant",
                                "It becomes zero"
                            ],
                            "answer": 1
                        }
                    ]
                },
            ],
            "gravitational_fields": [
                {
                    "name": "Gravitational Field Strength",
                    "lesson": """Gravitational field strength (g) represents the force per unit mass at any point in a gravitational field.

                    Key Concepts:
                    1. Field Strength:
                       - g = F/m = GM/r²
                       - Measured in N/kg or m/s²
                       - Varies with altitude

                    2. Gravitational Potential Energy:
                       - GPE = mgh (near Earth's surface)
                       - GPE = -GMm/r (general form)
                       - Zero at infinity

                    3. Important Facts:
                       - g = 9.81 m/s² at Earth's surface
                       - Field follows inverse square law
                       - Field lines point toward mass center

                    Applications:
                    - Space mission planning
                    - Satellite positioning
                    - Weight variations with altitude
                    """,
                    "summary": "Gravitational field strength measures the force experienced by a mass in a gravitational field, affected by distance from the mass causing the field.",
                    "quiz": [
                        {
                            "question": "What is the formula for gravitational field strength?",
                            "options": [
                                "F = ma",
                                "E = mc²",
                                "g = F/m = GM/r²",
                                "v = d/t"
                            ],
                            "answer": 2
                        },
                        {
                            "question": "What is the value of g at Earth's surface?",
                            "options": [
                                "9.81 m/s²",
                                "10 m/s²",
                                "8.67 m/s²",
                                "5.0 m/s²"
                            ],
                            "answer": 0
                        }
                    ]
                },
            ],
            "orbital_mechanics": [
                {
                    "name": "Kepler's Laws of Planetary Motion",
                    "lesson": """Kepler's Laws describe the motion of planets and satellites in orbit around a central body.

                    Key Laws:
                    1. First Law - Orbital Shape:
                       - Orbits are elliptical
                       - Central body at one focus
                       - Special case: circular orbits

                    2. Second Law - Equal Areas:
                       - Line joining planet to Sun sweeps equal areas in equal times
                       - Conservation of angular momentum
                       - Planets move faster when closer

                    3. Third Law - Orbital Periods:
                       - T² ∝ r³
                       - T² = (4π²/GM)r³
                       - Applies to all orbiting bodies

                    Applications:
                    - Satellite deployment
                    - Interplanetary missions
                    - Space station orbits
                    """,
                    "summary": "Kepler's laws describe how planets move in elliptical orbits, with varying speeds based on their distance from the Sun.",
                    "quiz": [
                        {
                            "question": "What shape are planetary orbits according to Kepler's First Law?",
                            "options": [
                                "Circular",
                                "Elliptical",
                                "Parabolic",
                                "Hyperbolic"
                            ],
                            "answer": 1
                        },
                        {
                            "question": "What does Kepler's Second Law state?",
                            "options": [
                                "Orbits are circular",
                                "Equal area in equal time",
                                "T² ∝ r³",
                                "Gravitational force is constant"
                            ],
                            "answer": 1
                        }
                    ]
                },
            ],
            "gravitational_effects": [
                {
                    "name": "Tidal Forces and Effects",
                    "lesson": """Tidal forces arise from differential gravitational forces across an extended body.

                    Key Concepts:
                    1. Tidal Bulge:
                       - Caused by gravity gradient
                       - Two bulges: facing and opposite
                       - Earth-Moon interaction

                    2. Tidal Effects:
                       - Ocean tides
                       - Tidal locking
                       - Orbital energy transfer

                    3. Important Facts:
                       - Varies with cube of distance
                       - Affects solid bodies too
                       - Causes tidal heating

                    Applications:
                    - Ocean navigation
                    - Moon's rotation
                    - Planetary geology
                    """,
                    "summary": "Tidal forces are caused by the varying gravitational pull from celestial bodies, leading to phenomena like ocean tides.",
                    "quiz": [
                        {
                            "question": "What causes tidal bulges on Earth?",
                            "options": [
                                "Wind",
                                "Moon's gravitational pull",
                                "Sun's radiation",
                                "Earth's rotation"
                            ],
                            "answer": 1
                        },
                        {
                            "question": "How do tidal forces affect solid bodies?",
                            "options": [
                                "No effect",
                                "Cracking",
                                "Tidal heating",
                                "Shape change"
                            ],
                            "answer": 2
                        }
                    ]
                },
            ],
            "advanced_gravitation": [
                {
                    "name": "Gravitational Waves",
                    "lesson": """Gravitational waves are ripples in spacetime caused by some of the most violent and energetic processes in the Universe.

                    Key Concepts:
                    1. Generation:
                       - Produced by accelerating masses
                       - Notable sources: merging black holes, neutron stars

                    2. Detection:
                       - LIGO and Virgo observatories
                       - Measure tiny changes in distance

                    3. Importance:
                       - New way to observe the universe
                       - Provides information about black hole mergers

                    Real-world Example:
                    - First detected in 2015 by LIGO, confirming Einstein's prediction
                    """,
                    "summary": "Gravitational waves are generated by massive objects moving in space, detectable by observatories like LIGO, revealing information about cosmic events.",
                    "quiz": [
                        {
                            "question": "What causes gravitational waves?",
                            "options": [
                                "Static objects",
                                "Accelerating masses",
                                "Light from stars",
                                "Magnetic fields"
                            ],
                            "answer": 1
                        },
                        {
                            "question": "Which observatory was the first to detect gravitational waves?",
                            "options": [
                                "Hubble",
                                "LIGO",
                                "James Webb",
                                "Chandra"
                            ],
                            "answer": 1
                        }
                    ]
                },
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
        "correctCount": correct_count,
        "totalCount": total_count
    })

if __name__ == '__main__':
    app.run(debug=False)
