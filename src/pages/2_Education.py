import streamlit as st

# Define your education background
education = [
    {
        "institution": "Cebu Institute of Technology - University",
        "degree": "Bachelor of Science in Information Technology",
        "location": "Cebu City, Cebu, Philippines",
        "dates": "2020 - Present",
        "logo": "https://upload.wikimedia.org/wikipedia/en/8/8c/Cebu_Institute_of_Technology_University_logo.png",
        "color": "#4CAF50",
        "academic_experience": [
            {
                "title": "Capstone and Research 1 & 2 - Frontend Developer",
                "details": [
                    "Designed the frontend of the project using Next.js",
                    "Implemented API fetching and REST API integration",
                    "Deployed the website and managed the database"
                ],
                "dates": "August 2024 - present"
            },
            {
                "title": "System Integration and Architecture Course - Project Manager & Frontend Developer",
                "details": [
                    "Led the design of the frontend using React.js",
                    "Managed API fetching and integration",
                    "Oversaw deployment and assisted team members"
                ],
                "dates": "August 2024 - May 2024"
            }
        ]
    },
    {
        "institution": "STI College Cebu Inc.",
        "degree": "Grade 12 - Senior High School, IT - Mobile App and Web Development",
        "location": "Cebu City, Cebu, Philippines",
        "dates": "2019 - 2020",
        "logo": "https://rec-data.kalibrr.com/www.kalibrr.com/logos/5PNVWEQDU5PXEGEXVYV9G4TDWG5PZVG8C4A22ZHY-5f0544a9.png",
        "color": "#2196F3",
        "academic_experience": [
            {
                "title": "Research - Developer",
                "details": [
                    "Developed and designed a Sales and Inventory System desktop application using C#.",
                    "Integrated the system with MySQL."
                ],
                "dates": "2019 - 2020"
            }
        ],
        "achievements": [
            "February 2020: Tagisan ng Talino - Think Quest Champion (Local)",
            "March 2020: Think Quest Cluster"
        ]
    },
    {
        "institution": "STI College Batangas",
        "degree": "Grade 11 - Senior High School, IT - Mobile App and Web Development",
        "location": "Batangas City, Batangas, Philippines",
        "dates": "2018 - 2019",
        "logo": "https://rec-data.kalibrr.com/www.kalibrr.com/logos/5PNVWEQDU5PXEGEXVYV9G4TDWG5PZVG8C4A22ZHY-5f0544a9.png",
        "color": "#2196F3",
        "academic_experience": [
            {
                "title": "Research - Leader",
                "details": [
                    "Led the development of a Digital Payroll System desktop application using Java (Netbeans).",
                    "Integrated the system with SQLite."
                ],
                "dates": "2018 - 2019"
            }
        ]
    },
    {
        "institution": "San Jose National High School",
        "degree": "Junior High School",
        "dates": "2014 - 2018",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwiPqvLDQnjrPCZTvkB-L5tjWAwpgW8YQySQ&s",
        "color": "#FF9800",
        "achievements": [
            "March 2018: With Honor",
            "September 2017: Technolympics Web Design Champion"
        ]
    },
    {
        "institution": "Talibon Central Elementary School",
        "degree": "Primary School",
        "dates": "2008 - 2014",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKq2IxB5SPUDOB6QAcsvnFjJWR3rnIm237cw&s",
        "color": "#FF9800",
        "achievements": [
            "2012 - 2015: MTAP Player",
            "2012 - 2015: Sports Editor",
            "S.Y 2013-2014: Class Salutatorian",
            "2013 - 2014: Science Club President",
            "2013 - 2014: TCES Drum and Lyre Corps Leader"
        ]
    }
]

# Create the education page
def display_education():
    st.title("Education Background")
    st.write("Here's a summary of my educational journey:")

    # Display the first three entries with merged experience and achievements
    for edu in education[:3]:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                        <img src="{edu['logo']}" style="max-width: 120px; max-height: 120px; border-radius: 8px;" />
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.markdown(
                    f"""
                    <div style="border: 1px solid {edu['color']}; padding: 20px; border-radius: 12px; box-shadow: 0 6px 12px rgba(0,0,0,0.1); margin-bottom: 20px;">
                        <h3 style="margin-top: 0; text-align: center;">{edu['institution']}</h3>
                        <p><strong>Degree/Program:</strong> {edu['degree']}</p>
                        {'<p><strong>Location:</strong> ' + edu['location'] + '</p>' if 'location' in edu else ''}
                        <p><strong>Dates Attended:</strong> {edu['dates']}</p>
                        {'<h4>Experience and Achievements:</h4>' + ''.join([f'<p><strong>{exp["title"]}:</strong><br />' + '<br />'.join(exp["details"]) + '<br /><i>Dates:</i> ' + exp["dates"] + '</p>' for exp in edu.get("academic_experience", [])])}
                        {'<ul>' + ''.join([f'<li>{ach}</li>' for ach in edu.get("achievements", [])]) + '</ul>' if 'achievements' in edu else ''}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Display the last two entries separately
    for edu in education[3:]:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                        <img src="{edu['logo']}" style="max-width: 120px; max-height: 120px; border-radius: 8px;" />
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.markdown(
                    f"""
                    <div style="border: 1px solid {edu['color']}; padding: 20px; border-radius: 12px; box-shadow: 0 6px 12px rgba(0,0,0,0.1); margin-bottom: 20px;">
                        <h3 style="margin-top: 0; text-align: center;">{edu['institution']}</h3>
                        <p><strong>Degree/Program:</strong> {edu['degree']}</p>
                        <p><strong>Dates Attended:</strong> {edu['dates']}</p>
                        {'<h4>Achievements:</h4>' + '<ul>' + ''.join([f'<li>{ach}</li>' for ach in edu.get("achievements", [])]) + '</ul>'}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# Render the education page
display_education()
