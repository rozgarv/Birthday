import streamlit as st
import random

# Set page layout
st.set_page_config(page_title="Shristee's Salix Defense Challenge", layout="wide")

# Title and introduction
st.title("🎉 Happy Birthday, Shristee! 🎉")
st.subheader("Welcome to your Salix Defense Challenge!")

st.write("""
Today, you are a brave **Salix tree** facing herbivore attacks, but don't worry! Your research comes to life here. 
Release the right **volatile chemicals** and attract predators to protect yourself from herbivores.
Let's see how well you can balance the defense!
""")

# Initialize session state for question tracking
if 'question_index' not in st.session_state:
    st.session_state['question_index'] = 0
    st.session_state['score'] = 0

# Adventure questions/scenarios
adventure = [
    {
        "scenario": "A caterpillar begins munching on your leaves. You must release a volatile to attract a predator. What will you do?",
        "options": ["Release (Z)-3-hexenyl acetate to attract ladybugs", "Release linalool to attract hoverflies", "Wait to release volatiles"],
        "correct": 0,
        "feedback": [
            "Good choice! Ladybugs love (Z)-3-hexenyl acetate and will help keep the caterpillar population down.",
            "Hoverflies prefer linalool, but they're not the best for this job. Try again!",
            "Oops! The herbivores are causing too much damage while you're waiting!"
        ]
    },
    {
        "scenario": "A new wave of herbivores is attacking! This time, a beetle species is devouring your branches. How will you defend?",
        "options": ["Release methyl salicylate", "Release (E)-β-ocimene", "Release no volatile"],
        "correct": 1,
        "feedback": [
            "Methyl salicylate is good for general plant defense, but not the best for attracting predators here!",
            "Great choice! (E)-β-ocimene will bring in some much-needed hoverflies to fend off the beetles.",
            "Releasing no volatile won’t help. The beetles are still munching away!"
        ]
    },
    {
        "scenario": "The herbivores seem to be adapting. You need to enhance your defense strategy. Which predator will you try to attract more?",
        "options": ["Hoverflies", "Parasitic wasps", "Ladybugs"],
        "correct": 2,
        "feedback": [
            "Hoverflies are helpful, but ladybugs can take on the most herbivores in this situation.",
            "Parasitic wasps can help, but they might not respond well to this scenario.",
            "Excellent! Ladybugs will swarm in and protect your branches from harm!"
        ]
    }
]

# Question display logic
question_index = st.session_state['question_index']

if question_index < len(adventure):
    current_scenario = adventure[question_index]

    st.write(f"**Scenario:** {current_scenario['scenario']}")
    
    # Present multiple choice options
    choice = st.radio("What will you do?", current_scenario["options"])

    if st.button("Submit"):
        selected_index = current_scenario["options"].index(choice)
        feedback = current_scenario["feedback"][selected_index]
        st.write(feedback)

        if selected_index == current_scenario["correct"]:
            st.session_state['score'] += 1

        # Move to next question
        st.session_state['question_index'] += 1
        st.experimental_rerun()  # Re-run app to load next question

else:
    st.write("🎉 You've completed the Salix Defense Challenge! 🎉")
    st.write(f"Your final score: {st.session_state['score']} out of {len(adventure)}")
    
    st.balloons()  # Birthday balloons!

    # Final birthday message
    st.subheader("Happy Birthday Shristee!")
    st.write("Wishing you a wonderful day full of joy, laughter, and lots of good wishes!")
