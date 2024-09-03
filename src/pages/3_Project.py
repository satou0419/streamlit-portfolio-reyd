import streamlit as st

# Define your projects
projects = [
    {
        "title": "Tower of Words",
        "description": "A word-based game that challenges users to form words and score points.",
        "tech_stack": ["Next.js", "MySQL", "Docker", "Merriam-Webster API"],
        "image": "https://via.placeholder.com/400x200.png?text=Tower+of+Words",
        "link": "https://your-tower-of-words-url.com"
    },
    {
        "title": "Dictionary",
        "description": "A dictionary application that provides word definitions and usage examples.",
        "tech_stack": ["React.js"],
        "image": "https://via.placeholder.com/400x200.png?text=Dictionary",
        "link": "https://your-dictionary-url.com"
    },
    {
        "title": "Raid of Cash",
        "description": "A financial management game where users manage and grow their virtual cash reserves.",
        "tech_stack": ["MERN Stack"],
        "image": "https://via.placeholder.com/400x200.png?text=Raid+of+Cash",
        "link": "https://your-raid-of-cash-url.com"
    },
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio website showcasing my skills, projects, and contact information.",
        "tech_stack": ["Next.js", "Streamlit", "Vercel"],
        "image": "https://via.placeholder.com/400x200.png?text=Portfolio+Website",
        "link": "https://your-portfolio-url.com"
    },
    {
        "title": "Japanese Quiz App",
        "description": "An interactive quiz app for learning Japanese with audio prompts and progress tracking.",
        "tech_stack": ["Streamlit", "Python"],
        "image": "https://via.placeholder.com/400x200.png?text=Japanese+Quiz+App",
        "link": "https://your-quiz-app-url.com"
    },
    {
        "title": "Capstone Project",
        "description": "A comprehensive capstone project involving frontend and backend development using modern technologies.",
        "tech_stack": ["Next.js", "React.js", "REST API"],
        "image": "https://via.placeholder.com/400x200.png?text=Capstone+Project",
        "link": "https://your-capstone-project-url.com"
    }
]

# Create the project page
def display_projects():
    st.title("Projects")
    st.write("Here are some of the projects I've worked on:")

    for project in projects:
        with st.container():
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 20px; border-radius: 12px; box-shadow: 0 6px 12px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <h3 style="margin-top: 0; text-align: center;">{project['title']}</h3>
                    <img src="{project['image']}" style="width: 100%; border-radius: 8px;"/>
                    <p><strong>Description:</strong> {project['description']}</p>
                    <p><strong>Tech Stack:</strong> {', '.join(project['tech_stack'])}</p>
                    <p><a href="{project['link']}" target="_blank" style="color: #4CAF50; text-decoration: none;">View Project</a></p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Render the project page
display_projects()
