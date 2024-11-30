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
    "motion": [
        {
            "name": "Describing Motion",
            "lesson": """Motion is defined as the change in position of an object with respect to time. It can be described in terms of displacement, velocity, and acceleration. The study of motion is known as kinematics, and it helps us understand how objects move in space. 

            Key Concepts:
            1. **Types of Motion**:
               - **Translatory Motion**: Movement along a straight or curved path, such as a car moving on a road.
               - **Rotational Motion**: Movement around an axis, such as the Earth's rotation.
               - **Oscillatory Motion**: Repetitive back-and-forth motion, like a pendulum.

            2. **Reference Frame**:
               - A reference frame is essential for describing motion. It provides a point from which measurements of position, velocity, and acceleration can be made.

            3. **Scalars and Vectors**:
               - **Distance**: The total path traveled, a scalar quantity.
               - **Displacement**: The shortest distance between the starting and ending point, with direction, a vector quantity.

            4. **Relative Motion**:
               - The motion of an object depends on the observer’s reference frame. Different frames of reference can observe different velocities for the same object.

            Real-World Application:
            - Motion of planets around the Sun and the movement of vehicles in traffic.

            Advanced Concept:
            - Analyzing non-uniform motion through calculus allows us to study the relationship between position and velocity over time.
            """,
            "summary": """Motion is a change in position over time. It can be described as translatory, rotational, or oscillatory motion and is studied in relation to reference frames, distance, and displacement.""",
            "quiz": [
                {
                    "question": "Which type of motion is an example of movement around an axis?",
                    "options": [
                        "Translatory motion",
                        "Rotational motion",
                        "Oscillatory motion",
                        "Linear motion"
                    ],
                    "answer": 1
                },
                {
                    "question": "What is the key difference between distance and displacement?",
                    "options": [
                        "Distance is a scalar, and displacement is a vector.",
                        "Displacement measures total path length, distance considers direction.",
                        "Distance can be negative, displacement cannot.",
                        "Displacement is the total distance traveled along the path."
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "name": "Motion Along a Straight Line",
            "lesson": """This topic covers the motion of objects moving along a straight line, either with constant or changing velocity.

            Key Concepts:
            1. **Uniform Motion**:
               - An object moves with constant velocity, covering equal distances in equal intervals of time.

            2. **Non-Uniform Motion**:
               - An object’s velocity is changing. This can involve acceleration or deceleration, such as a car speeding up or slowing down.

            3. **Speed and Velocity**:
               - **Speed**: The total distance covered divided by the total time taken. It is a scalar quantity.
               - **Velocity**: The displacement divided by the total time taken. It is a vector quantity and includes both magnitude and direction.

            4. **Acceleration**:
               - Acceleration occurs when there is a change in velocity over time, either an increase (acceleration) or a decrease (deceleration) in speed.

            Real-World Application:
            - Vehicles moving along straight roads, with varying speeds, can be analyzed using speed, velocity, and acceleration.

            Advanced Concept:
            - Non-uniform motion often requires calculus to compute displacement and velocity when acceleration is not constant.
            """,
            "summary": """Motion along a straight line can either be uniform (constant velocity) or non-uniform (changing velocity). Concepts such as speed, velocity, and acceleration are central to describing this motion.""",
            "quiz": [
                {
                    "question": "Which of the following is an example of non-uniform motion?",
                    "options": [
                        "A car moving at a constant speed",
                        "A car speeding up",
                        "A rock falling freely",
                        "A plane cruising at constant altitude"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "name": "Uniform Motion and Non-Uniform Motion",
            "lesson": """Motion is categorized into uniform and non-uniform types, based on the behavior of velocity.

            Key Concepts:
            1. **Uniform Motion**:
               - The object’s velocity remains constant throughout its motion.

            2. **Non-Uniform Motion**:
               - The object’s velocity changes over time. It may involve varying acceleration or deceleration.

            3. **Graphical Representation**:
               - In uniform motion, the distance-time graph is a straight line, indicating constant speed.
               - In non-uniform motion, the graph is a curve, indicating changing velocity.

            Real-World Application:
            - Uniform motion is seen in a car moving at a steady pace, while non-uniform motion is common when a vehicle starts and stops.

            Advanced Concept:
            - The use of derivatives and integrals can describe the changes in velocity and position in non-uniform motion.
            """,
            "summary": """Uniform motion occurs at constant velocity, while non-uniform motion involves changing velocity. Graphs help to visualize these types of motion and calculate various quantities.""",
            "quiz": [
                {
                    "question": "What does a distance-time graph for uniform motion look like?",
                    "options": [
                        "A straight, sloped line",
                        "A curved line",
                        "A straight horizontal line",
                        "A zigzag line"
                    ],
                    "answer": 0
                }
            ]
        },
        {
            "name": "Measuring the Rate of Motion",
            "lesson": """The rate of motion is measured in terms of speed and velocity.

            Key Concepts:
            1. **Speed**:
               - Speed is the rate at which distance is covered. It is a scalar quantity, measured in meters per second (m/s).

            2. **Velocity**:
               - Velocity is the rate of change of displacement. Unlike speed, it is a vector, having both magnitude and direction.

            3. **Instantaneous Speed and Velocity**:
               - Instantaneous speed refers to the speed at a particular moment, while instantaneous velocity also accounts for direction at that moment.

            Real-World Application:
            - Speedometers measure the instantaneous speed of vehicles. Velocity is used to describe the motion of particles in physics.

            Advanced Concept:
            - Calculus is often required to calculate average speed and velocity in cases of non-uniform motion.
            """,
            "summary": """Speed and velocity describe the rate of motion. Speed is scalar, and velocity is vectorial, including direction. Instantaneous speed and velocity can be determined at any given moment.""",
            "quiz": [
                {
                    "question": "Which quantity includes direction?",
                    "options": [
                        "Speed",
                        "Time",
                        "Velocity",
                        "Distance"
                    ],
                    "answer": 2
                }
            ]
        },
        {
            "name": "Speed with Direction",
            "lesson": """Speed with direction is referred to as velocity. Velocity has both magnitude (speed) and direction, which distinguishes it from speed.

            Key Concepts:
            1. **Velocity**:
               - Velocity represents both the rate of motion and the direction of the object’s motion.

            2. **Scalar vs. Vector**:
               - Speed is a scalar and tells how fast an object is moving, while velocity is a vector, also indicating the direction of motion.

            3. **Direction of Motion**:
               - The direction is critical in determining the velocity. For example, an object moving northward at 10 m/s has a velocity of 10 m/s north.

            Real-World Application:
            - Airplanes and ships often specify their velocities, including direction, to avoid confusion with speed.

            Advanced Concept:
            - The velocity vector can be broken down into components for motion in multiple directions.
            """,
            "summary": """Speed with direction is velocity. Velocity is a vector that describes both the magnitude of motion (speed) and its direction, unlike speed, which is scalar.""",
            "quiz": [
                {
                    "question": "What distinguishes velocity from speed?",
                    "options": [
                        "Velocity is always greater than speed.",
                        "Velocity includes direction, while speed does not.",
                        "Velocity measures the total distance covered, while speed measures displacement.",
                        "Velocity is a scalar, while speed is a vector."
                    ],
                    "answer": 1
                }
            ]
        }
    ],
    "force_and_laws_of_motion": [
        {
            "name": "Balanced and Unbalanced Forces",
            "lesson": """Forces are vectors that cause changes in motion. 

            Key Concepts:
            1. **Balanced Forces**:
               - Forces are balanced when they are equal in magnitude but opposite in direction. This results in no change in motion.

            2. **Unbalanced Forces**:
               - Unbalanced forces cause acceleration or deceleration, leading to a change in motion.

            3. **Force and Motion**:
               - The net force acting on an object determines its motion according to Newton’s laws of motion.

            Real-World Application:
            - A book resting on a table experiences balanced forces, while a car accelerating involves unbalanced forces.

            Advanced Concept:
            - The net force on an object can be calculated using vector addition when multiple forces are acting on it.
            """,
            "summary": """Balanced forces do not change an object's motion, while unbalanced forces cause acceleration or deceleration, affecting the object's state of motion.""",
            "quiz": [
                {
                    "question": "Which of the following causes an object to accelerate?",
                    "options": [
                        "Balanced forces",
                        "Unbalanced forces",
                        "Equal forces",
                        "Opposite forces"
                    ],
                    "answer": 1
                }
            ]
        },
        {
            "name": "First Law of Motion",
            "lesson": """Newton's First Law states that an object at rest will remain at rest, and an object in motion will continue in motion unless acted upon by an unbalanced external force.

            Key Concepts:
            1. **Inertia**:
               - The tendency of objects to resist changes in motion. More massive objects have greater inertia.

            2. **Constant Velocity**:
               - An object moving with constant velocity will continue moving unless acted on by an external force, like friction or gravity.

            Real-World Application:
            - A passenger in a car feels a jolt when the car suddenly stops due to inertia.

            Advanced Concept:
            - The concept of inertia can be applied to space exploration, where spacecraft can continue their motion without external forces acting on them in the vacuum of space.
            """,
            "summary": """Newton’s First Law, the law of inertia, states that objects will continue their state of motion unless acted upon by an external force.""",
            "quiz": [
                {
                    "question": "What does Newton's First Law describe?",
                    "options": [
                        "The relationship between force and motion",
                        "The effect of unbalanced forces",
                        "The tendency of objects to resist changes in motion",
                        "The behavior of objects at high speeds"
                    ],
                    "answer": 2
                }
            ]
        }
    ],
    "gravitation": [
        {
            "name": "Gravitation",
            "lesson": """Gravitation is the force that attracts objects toward each other. It is responsible for keeping planets in orbit around the Sun.

            Key Concepts:
            1. **Universal Law of Gravitation**:
               - Every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.

            2. **Free Fall**:
               - An object in free fall experiences only the force of gravity, accelerating at 9.8 m/s² (on Earth).

            3. **Gravitational Force**:
               - The force that pulls objects toward the center of the Earth.

            Real-World Application:
            - The weight of an object, or the force it exerts due to gravity, is determined by its mass and the gravitational force of Earth.

            Advanced Concept:
            - Gravitational potential energy is related to the position of an object in a gravitational field.
            """,
            "summary": """Gravitation is a force of attraction between masses. It is described by the universal law of gravitation, influencing the motion of objects in free fall.""",
            "quiz": [
                {
                    "question": "What does the universal law of gravitation state?",
                    "options": [
                        "The force of gravity is constant everywhere.",
                        "Gravity depends only on mass.",
                        "Gravity is stronger the farther apart two objects are.",
                        "Every mass attracts every other mass with a force inversely proportional to the square of the distance."
                    ],
                    "answer": 3
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
