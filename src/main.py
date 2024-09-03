import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import os

st.set_page_config(
    page_title="Reyd",
    page_icon="💀",
)

def make_image_circular(img, size=(100, 100)):
    img = img.resize(size, Image.Resampling.LANCZOS)
    np_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
    mask = Image.new('L', np_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + np_img.size, fill=255)
    np_img.putalpha(mask)
    return np_img

def load_image(path, fallback_path=None):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        if fallback_path and os.path.exists(fallback_path):
            image = Image.open(fallback_path)
        else:
            st.error(f"Image not found: {path} and {fallback_path}")
            return None
    return image

# Main page content
left_col, right_col = st.columns(2)

with left_col:
    st.header("Hi, I'm Rey Dante G. Garcia!")
    st.write(
        """
        I'm an IT enthusiast aspiring to delve into the world of front-end development. 
        I aim to create compelling websites using creative visuals and handy tools that surpass expectations.
        """
    )

    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
        }
        .social-buttons a {
            text-decoration: none;
            color: inherit;
        }
        .social-buttons img {
            width: 24px;
            height: 24px;
        }
        </style>
        <div class="social-buttons">
            <a href="https://github.com/satou0419" target="_blank"><img src=https://www.svgrepo.com/show/439171/github.svg alt="GitHub"></a>
            <a href="https://www.upwork.com/freelancers/~01b6d763f70fcce8f2" target="_blank"><img src=https://www.svgrepo.com/show/516513/freelancer-upwork.svg alt="Upwork"></a>
            <a href="https://www.linkedin.com/in/rey-dante-garcia-7a7b8a219/" target="_blank"><img src= https://www.svgrepo.com/show/416903/internet-linkedln-media.svg alt="LinkedIn"></a>
        </div>
        """,
        unsafe_allow_html=True
    )

with right_col:
    image_path = "src/assets/myBanner.png"
    fallback_path = "src/assets/myBanner.png"
    image = load_image(image_path, fallback_path)
    
    if image:
        st.image(image, use_column_width=True)

st.markdown("---")
st.title("Tech Stack")

categories = {
    "Front-End": [
        {"name": "JavaScript", "logo": "https://www.svgrepo.com/show/353925/javascript.svg"},
        {"name": "React", "logo": "https://www.svgrepo.com/show/493719/react-javascript-js-framework-facebook.svg"},
        {"name": "Next.js", "logo": "https://www.svgrepo.com/show/354113/nextjs-icon.svg"},
        {"name": "TypeScript", "logo": "https://www.svgrepo.com/show/349540/typescript.svg"},
        {"name": "jQuery", "logo": "https://www.svgrepo.com/show/452242/jquery.svg"},
        {"name": "CSS/SCSS", "logo": "https://www.svgrepo.com/show/374067/scss2.svg"},
        {"name": "HTML5", "logo": "https://www.svgrepo.com/show/373669/html.svg"}
    ],
    "Back-End": [
        {"name": "Node.js", "logo": "https://www.svgrepo.com/show/452075/node-js.svg"},
        {"name": "Python", "logo": "https://www.svgrepo.com/show/452091/python.svg"},
        {"name": "Java", "logo": "https://www.svgrepo.com/show/452234/java.svg"},
        {"name": "Spring Boot", "logo": "https://www.svgrepo.com/show/333604/spring-boot.svg"},
        {"name": "Express", "logo": "https://www.svgrepo.com/show/353724/express.svg"}
    ],
    "Languages": [
        {"name": "C", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/19/C_Logo.png"},
        {"name": "C++", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png"},
        {"name": "C#", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Logo_C_sharp.svg/1200px-Logo_C_sharp.svg.png"}
    ],
    "Tools": [
        {"name": "VSCode", "logo": "https://www.svgrepo.com/show/374171/vscode.svg"},
        {"name": "Git", "logo": "https://www.svgrepo.com/show/452210/git.svg"},
        {"name": "Docker", "logo": "https://www.svgrepo.com/show/448221/docker.svg"}
    ],
    "Deployment": [        
        {"name": "Render", "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQATbZwZHm43PN4_D2BooUaP--zflkHet-oTw&s"},
        {"name": "Azure", "logo": "https://www.svgrepo.com/show/331302/azure-v2.svg"},
        {"name": "Aiven", "logo": "https://www.drupal.org/files/aiven-logo_RGB.png"},
        {"name": "Vercel", "logo": "https://www.svgrepo.com/show/361653/vercel-logo.svg"}
    ],
    "Databases": [
        {"name": "MongoDB", "logo": "https://1000logos.net/wp-content/uploads/2020/08/MongoDB-Logo.png"},
        {"name": "SQLite", "logo": "https://dwglogo.com/wp-content/uploads/2018/03/SQLite_logo.png"},
        {"name": "MySQL", "logo": "https://upload.wikimedia.org/wikipedia/labs/8/8e/Mysql_logo.png"}
    ],
    "Languages & Frameworks": [
        {"name": "PHP", "logo": "https://pngimg.com/d/php_PNG10.png"},
        {"name": "Flask", "logo": "https://miro.medium.com/v2/resize:fit:438/1*dQvABiWzbE28OTPYjzElKw.png"}
    ]
}

st.markdown(
    """
    <style>
    .card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin: 10px;
        width: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .card img {
        max-width: 60px;
        margin-bottom: 10px;
    }
    .cards-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

for category, items in categories.items():
    st.markdown(f"### {category}")
    st.markdown('<div class="cards-container">', unsafe_allow_html=True)
    for i in range(0, len(items), 3):
        row_items = items[i:i + 3]
        cols = st.columns(len(row_items))
        for col, item in zip(cols, row_items):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <img src="{item['logo']}" alt="{item['name']}">
                        <p>{item['name']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

# Add JLPT Certificate Section
st.markdown("---")
st.title("Certifications")

left_col, right_col = st.columns(2)

with left_col:
    jlpt_image_path = "src/assets/jlpt.png"
    jlpt_fallback_path = "src/assets/jlpt.png"
    jlpt_image = load_image(jlpt_image_path, jlpt_fallback_path)

    if jlpt_image:
        st.image(jlpt_image, use_column_width=True)

with right_col:
    st.subheader("Japanese-Language Proficiency Test (JLPT Mock) N5")
    st.write(
        """
        🎓 **Certification Achieved**: JLPT N5 (4 years ago)
        
        This certification marks my initial achievement in Japanese language proficiency. As I continue my Nihongo studies, this milestone represents a strong foundation in reading, writing, and understanding Japanese. I am committed to advancing my skills and exploring higher proficiency levels as part of my ongoing language education.
        """
    )

st.markdown(
    """
    <style>
    .certification-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #f9f9f9;
    }
    .certification-text {
        margin-left: 20px;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)
