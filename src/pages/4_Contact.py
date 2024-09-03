import streamlit as st

def contact_form():
    st.title("📬 Contact Me")
    st.write("I'm always open to your questions, feedback, or just a friendly hello! Please fill out the form below, and I'll get back to you as soon as possible.")

    with st.form(key='contact_form', clear_on_submit=True):
        # Form fields
        name = st.text_input("Your Full Name", "")
        email = st.text_input("Your Email Address", "")
        subject = st.text_input("Subject", "")
        message = st.text_area("Your Message", "")
        
        # Submit button
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            # Create a form submission URL
            form_url = "https://formsubmit.co/garciareydante@gmail.com"
            
            # Handle the submission
            if name and email and subject and message:
                # Create a script to submit the form data using JavaScript
                st.markdown(f"""
                <script>
                    (function() {{
                        var form = document.createElement('form');
                        form.method = 'POST';
                        form.action = '{form_url}';

                        var nameField = document.createElement('input');
                        nameField.type = 'hidden';
                        nameField.name = 'name';
                        nameField.value = '{name}';
                        form.appendChild(nameField);

                        var emailField = document.createElement('input');
                        emailField.type = 'hidden';
                        emailField.name = 'email';
                        emailField.value = '{email}';
                        form.appendChild(emailField);

                        var subjectField = document.createElement('input');
                        subjectField.type = 'hidden';
                        subjectField.name = 'subject';
                        subjectField.value = '{subject}';
                        form.appendChild(subjectField);

                        var messageField = document.createElement('textarea');
                        messageField.name = 'message';
                        messageField.value = '{message}';
                        form.appendChild(messageField);

                        document.body.appendChild(form);
                        form.submit();
                    }})();
                </script>
                """, unsafe_allow_html=True)
            else:
                st.error("Please fill out all fields before submitting.")
                
# Render the contact form page
contact_form()
