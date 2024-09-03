import streamlit as st
import time
import pandas as pd

# Initialize session state for the quiz
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'times' not in st.session_state:
    st.session_state.times = []
if 'results' not in st.session_state:
    st.session_state.results = []

# Quiz questions and options
questions = [
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/1GoodMorning-1536557341462.mp3",
        "options": ["おはよう", "こんにちは", "お元気ですか", "さようなら"],
        "correct": "おはよう"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/2GoodAfternoonHello-1536557456494.mp3",
        "options": ["おはよう", "こんにちは", "お元気ですか", "さようなら"],
        "correct": "こんにちは"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/3Howareyoum4a-1536557504099.mp3",
        "options": ["おはよう", "こんにちは", "お元気ですか", "さようなら"],
        "correct": "お元気ですか"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/4Goodnight-1536557546892.mp3",
        "options": ["おはよう", "こんにちは", "お元気ですか", "おやすみなさい"],
        "correct": "おやすみなさい"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/5Seeyoucasual-1536557609346.mp3",
        "options": ["おはよう", "こんにちは", "お元気ですか", "じゃあ、また"],
        "correct": "じゃあ、また"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/7Goodbye-1536557682671.mp3",
        "options": ["おはよう", "こんにちは", "さようなら", "おやすみなさい"],
        "correct": "さようなら"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/9Imsorry-1536557750838.mp3",
        "options": ["ごめんなさい", "ありがとう", "どういたしまして", "ちょっとまって"],
        "correct": "ごめんなさい"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/10Thankyou-1536557793031.mp3",
        "options": ["ごめんなさい", "ありがとう", "どういたしまして", "ちょっとまって"],
        "correct": "ありがとう"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/11YoureWelcome-1536557821603.mp3",
        "options": ["ごめんなさい", "ありがとう", "どういたしまして", "ちょっとまって"],
        "correct": "どういたしまして"
    },
    {
        "audio": "https://s3.amazonaws.com/thinkific-import/133121/12Waitamoment-1536557852177.mp3",
        "options": ["ごめんなさい", "ありがとう", "どういたしまして", "ちょっとまって"],
        "correct": "ちょっとまって"
    }
]

# Function to handle answer submission
def submit_answer(selected_option):
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()  # Start timing when the first answer is submitted
    
    correct_option = questions[st.session_state.question_index]["correct"]
    end_time = time.time()
    elapsed_time = end_time - st.session_state.start_time
    
    if selected_option == correct_option:
        st.session_state.score += 1
        st.success("Correct!")
    else:
        st.error("Incorrect. Try again.")
    
    st.session_state.times.append(elapsed_time)
    st.session_state.results.append(selected_option == correct_option)
    st.session_state.answered = True

# Function to go to the next question
def next_question():
    st.session_state.question_index += 1
    st.session_state.answered = False
    st.session_state.start_time = time.time()  # Restart timer for the next question

# Display the quiz
def display_quiz():
    if st.session_state.question_index < len(questions):
        question = questions[st.session_state.question_index]
        st.audio(question["audio"], format="audio/mp3")
        st.write(f"Question {st.session_state.question_index + 1}/{len(questions)}")
        st.write("Select the correct option:")

        options = question["options"]
        selected_option = st.radio("Options", options)

        if st.button("Submit Answer"):
            submit_answer(selected_option)

        if st.session_state.answered:
            st.button("Next Question", on_click=next_question)
    else:
        st.write(f"Congratulations, {st.session_state.name}! You completed the quiz.")
        st.write(f"Your score is {st.session_state.score}/{len(questions)}")

        # Plot the time taken for each question
        if st.session_state.times:
            time_df = pd.DataFrame({
                'Question': [f'Q{i+1}' for i in range(len(st.session_state.times))],
                'Time (seconds)': st.session_state.times,
                'Correct': st.session_state.results
            })
            time_df.set_index('Question', inplace=True)
            st.bar_chart(time_df[['Time (seconds)']], use_container_width=True)

# Render the quiz in the app
st.title("Japanese Language Quiz")

# Get examinee's name
if st.session_state.name == "":
    st.write("# Enter Your Name")
    st.session_state.name = st.text_input("Name:")
    if st.session_state.name:
        st.write(f"## Welcome, {st.session_state.name}!")
        if st.button("Start Quiz"):
            st.session_state.start_time = None  # Reset start_time to ensure it's set when answering questions
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.times = []
            st.session_state.results = []
            st.write("Click the button below to start the quiz.")
else:
    display_quiz()
