import streamlit as st

# Define your projects
projects = [
    {
        "title": "Tower of Words",
        "description": "A gamefied spelling and vocabulary game that is intended for elementary students to boost their literary skills. It is also a tool for teachers.",
        "tech_stack": ["Next.js", "MySQL", "Docker", "Merriam-Webster API", "Spring Boot"],
        "image": "https://i.ibb.co/cxqM8Wc/image.png",
        "link": "https://tower-of-words.vercel.app/",
        "github": "https://github.com/satou0419/tower-of-words_repository"
    },
    {
        "title": "Dictionary",
        "description": "A dictionary application that provides word definitions and usage examples.",
        "tech_stack": ["React.js"],
        "image": "https://i.ibb.co/kmP4LHT/image.png",
        "link": "https://merriam-dictionary-api.onrender.com/",
        "github": "https://github.com/satou0419/dictionary-merriam-api"
    },
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio website showcasing my skills, projects, and contact information.",
        "tech_stack": [ "Streamlit"],
        "image": "https://i.ibb.co/yXVfbqq/image.png",
        "link": "https://reydev.streamlit.app/",
        "github": "https://github.com/satou0419/streamlit-portfolio-reyd"
    }
]

# Create the project page
def display_projects():
    st.title("Projects")
    st.write("Here are some of the projects I've worked on:")

    for project in projects:
        with st.container():
            github_link = f'<a href="{project["github"]}" target="_blank"><img src="https://www.svgrepo.com/show/475654/github-color.svg" style="width: 20px; vertical-align: middle;" /></a>' if project['github'] != '#' else ''
            
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; padding: 20px; border-radius: 12px; box-shadow: 0 6px 12px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <h3 style="margin-top: 0; text-align: center;">{project['title']}</h3>
                    <img src="{project['image']}" style="width: 100%; border-radius: 8px;"/>
                    <p><strong>Description:</strong> {project['description']}</p>
                    <p><strong>Tech Stack:</strong> {', '.join(project['tech_stack'])}</p>
                    <p>
                        <a href="{project['link']}" target="_blank" style="color: #4CAF50; text-decoration: none;">View Project</a>
                        {f' | {github_link}' if project['github'] != '#' else ''}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Render the project page
display_projects()
