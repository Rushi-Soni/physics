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
        
        content = {
    "motion": [
        {
            "name": "Describing Motion",
            "lesson": """Motion is the change in position of an object over time. It is measured in terms of displacement, distance, velocity, and speed.
            
            Key Concepts:
            1. **Reference Frames**:
               - A reference frame is a coordinate system used to measure the position and motion of an object.
            
            2. **Types of Motion**:
               - Linear motion, circular motion, and oscillatory motion are the main types.
            
            Real-World Application:
            - Cars moving on a road follow a linear motion relative to the road.

            Advanced Concept:
            - The relative motion of an object can be described in different reference frames, such as a moving car or a stationary observer.
            """,
            "summary": "Motion describes the change in position of an object over time, relative to a reference frame.",
            "quiz": [
                {
                    "question": "What is motion?",
                    "options": [
                        "The change in position of an object.",
                        "The speed of an object.",
                        "The force applied to an object.",
                        "The mass of an object."
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "name": "Motion Along a Straight Line",
            "lesson": """Motion along a straight line refers to the movement of objects in one-dimensional space. In this motion, velocity can either be constant or variable.
            
            Key Concepts:
            1. **Uniform Motion**:
               - When an object moves with a constant velocity along a straight line, its motion is uniform.

            2. **Non-Uniform Motion**:
               - When the velocity of an object changes over time, it is in non-uniform motion.

            Real-World Application:
            - A car moving at a constant speed along a highway represents uniform motion.

            Advanced Concept:
            - Non-uniform motion is characterized by acceleration or deceleration, changing the object's velocity.
            """,
            "summary": "Objects moving along a straight line can have uniform or non-uniform motion, characterized by constant or changing velocity.",
            "quiz": [
                {
                    "question": "Which of the following represents uniform motion?",
                    "options": [
                        "A car speeding up on a highway.",
                        "A ball dropped from a height.",
                        "A car moving at constant speed on a highway.",
                        "A person running faster each minute."
                    ],
                    "answer": 2
                }
            ]
        },
        {
            "name": "Uniform Motion and Non-Uniform Motion",
            "lesson": """In uniform motion, the velocity remains constant, while in non-uniform motion, velocity changes with time. 
            
            Key Concepts:
            1. **Constant Velocity**:
               - When an object moves at a constant speed in a straight line, its velocity does not change.

            2. **Changing Velocity**:
               - If an object’s velocity changes over time, the motion is non-uniform. This change can be due to acceleration or deceleration.

            Real-World Application:
            - A speeding car or a car coming to a stop exemplifies non-uniform motion.

            Advanced Concept:
            - Non-uniform motion can be described using acceleration: \( v = u + at \), where \( v \) is final velocity, \( u \) is initial velocity, \( a \) is acceleration, and \( t \) is time.
            """,
            "summary": "Uniform motion has constant velocity, while non-uniform motion has varying velocity with acceleration or deceleration.",
            "quiz": [
                {
                    "question": "Which of the following is an example of non-uniform motion?",
                    "options": [
                        "A car moving at constant speed.",
                        "A car slowing down after reaching a traffic light.",
                        "A ball rolling on a flat surface.",
                        "A clock's second hand."
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "name": "Measuring the Rate of Motion",
            "lesson": """Speed and velocity are used to measure the rate of motion. Speed is a scalar quantity, while velocity is a vector quantity.
            
            Key Concepts:
            1. **Speed**:
               - Speed is the distance traveled per unit time. It is measured in meters per second (m/s).
            
            2. **Velocity**:
               - Velocity is the displacement per unit time and includes both magnitude and direction.

            Real-World Application:
            - When traveling by car, speed is the rate at which you cover distance, while velocity considers your direction of travel.

            Advanced Concept:
            - Instantaneous speed is the speed of an object at a particular moment in time, and can be found from the slope of a distance-time graph.
            """,
            "summary": "Speed measures how fast an object moves, while velocity includes both speed and direction.",
            "quiz": [
                {
                    "question": "Which of the following is a vector quantity?",
                    "options": [
                        "Speed",
                        "Distance",
                        "Time",
                        "Velocity"
                    ],
                    "answer": 3
                }
            ]
        },
        {
            "name": "Graphical Representation of Motion",
            "lesson": """Graphs are used to visually represent motion. The most common graphs are distance-time and velocity-time graphs.

            Key Concepts:
            1. **Distance-Time Graph**:
               - A distance-time graph shows how the distance covered by an object changes over time. The slope represents speed.
            
            2. **Velocity-Time Graph**:
               - A velocity-time graph shows how an object’s velocity changes over time. The slope represents acceleration.

            Real-World Application:
            - The motion of a car during a trip can be represented by distance-time and velocity-time graphs.

            Advanced Concept:
            - The area under a velocity-time graph gives the total distance traveled. For uniformly accelerated motion, this can be calculated as \( \text{Distance} = \frac{1}{2} (u + v) t \), where \( u \) is initial velocity, \( v \) is final velocity, and \( t \) is time.
            """,
            "summary": "Graphs represent motion, with distance-time graphs showing speed and velocity-time graphs showing acceleration.",
            "quiz": [
                {
                    "question": "What does the area under a velocity-time graph represent?",
                    "options": [
                        "Acceleration",
                        "Speed",
                        "Time",
                        "Distance"
                    ],
                    "answer": 3
                }
            ]
        },
        {
            "name": "Equations of Motion",
            "lesson": """The equations of motion describe the relationship between velocity, acceleration, time, and displacement during uniformly accelerated motion.

            Key Concepts:
            1. **First Equation of Motion**:
               - \( v = u + at \), where \( v \) is final velocity, \( u \) is initial velocity, \( a \) is acceleration, and \( t \) is time.

            2. **Second Equation of Motion**:
               - \( s = ut + \frac{1}{2} at^2 \), where \( s \) is displacement, \( u \) is initial velocity, \( a \) is acceleration, and \( t \) is time.

            Real-World Application:
            - These equations can be used to calculate the distance traveled by an object under constant acceleration, such as a car accelerating from rest.

            Advanced Concept:
            - The third equation of motion is \( v^2 = u^2 + 2as \), which relates velocity, acceleration, and displacement.
            """,
            "summary": "The equations of motion describe the relationship between velocity, acceleration, time, and displacement for uniformly accelerated motion.",
            "quiz": [
                {
                    "question": "What is the second equation of motion?",
                    "options": [
                        "v = u + at",
                        "s = ut + \frac{1}{2} at^2",
                        "v^2 = u^2 + 2as",
                        "s = ut + at"
                    ],
                    "answer": 1
                }
            ]
        },
    ],
    "gravitation": [
        {
            "name": "Gravitation",
            "lesson": """Gravitation is the force of attraction that objects exert on each other due to their mass. It affects all matter and plays a crucial role in phenomena like free fall, planetary motion, and tides.

            Key Concepts:
            1. **Gravity**:
               - The force that attracts objects towards each other. Earth’s gravity keeps us grounded.

            2. **Gravitational Force**:
               - The force of attraction between two masses depends on their mass and the distance between them.

            Real-World Application:
            - Objects fall toward the ground because of Earth's gravitational pull.

            Advanced Concept:
            - Gravitational force follows the inverse-square law, meaning the force weakens with the square of the distance between objects.
            """,
            "summary": """Gravitation is the force of attraction between masses, influencing objects' motion, planetary orbits, and more.""",
            "quiz": [
                {
                    "question": "What is the effect of gravity on objects?",
                    "options": [
                        "Objects repel each other.",
                        "Objects move towards each other.",
                        "Objects remain stationary.",
                        "Objects move away from each other."
                    ],
                    "answer": 1
                }
            ]
        },
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
# Flask app and routes remain the same

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
