import streamlit as st

def contact_form():
    st.title("📬 Contact Me")
    st.write("I'm always open to your questions, feedback, or just a friendly hello! Please fill out the form below, and I'll get back to you as soon as possible.")

    # HTML and CSS for styling
    st.markdown("""
    <style>
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .contact-form h3 {
            text-align: center;
        }
        .contact-form label {
            display: block;
            margin-bottom: 8px;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .contact-form button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .contact-form button:hover {
            background-color: #45a049;
        }
    </style>
    <div class="contact-form">
        <h3>Contact Form</h3>
        <form action="https://formsubmit.co/garciareydante@gmail.com" method="POST">
            <label for="name"><strong>Your Full Name:</strong></label>
            <input type="text" name="name" required>
            <label for="email"><strong>Your Email Address:</strong></label>
            <input type="email" name="email" required>
            <label for="subject"><strong>Subject:</strong></label>
            <input type="text" name="subject" required>
            <label for="message"><strong>Your Message:</strong></label>
            <textarea name="message" required></textarea>
            <button type="submit">Send</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# Render the contact form page
contact_form()
