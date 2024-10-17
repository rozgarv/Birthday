import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Shristee", layout="wide")

# Welcome screen
st.title("🎉 Happy Birthday, Shristee! 🎉")
st.write("Today is a special day because it's YOUR day!")

# Fun quiz
if st.button("Start Your Birthday Adventure"):
    st.subheader("How well do you know your favorite things?")
    score = 0

    # Example questions (customize based on Shristee's favorites)
    questions = [
        {"question": "What's your favorite color?", "options": ["Blue", "Green", "Purple", "Red"], "answer": "Purple"},
        {"question": "What's your favorite dessert?", "options": ["Ice Cream", "Cake", "Cookies", "Brownies"], "answer": "Cake"},
        {"question": "Which country do you want to visit?", "options": ["Japan", "France", "New Zealand", "Canada"], "answer": "Japan"},
    ]
    
    for q in questions:
        answer = st.radio(q["question"], q["options"])
        if answer == q["answer"]:
            score += 1

    st.write(f"Your score is: {score}/{len(questions)}")

# Countdown to surprise
st.subheader("Stay tuned for a special birthday surprise... 🎁")

if st.button("Reveal Surprise"):
    with st.spinner("Loading your surprise..."):
        time.sleep(3)  # Add some suspense
    st.success("🎉 Here's your surprise gift! Check your email!")

# Final confetti celebration
if st.button("Celebrate"):
    st.balloons()

# Footer message
st.write("Wishing you all the happiness in the world, Shristee! 💖")
