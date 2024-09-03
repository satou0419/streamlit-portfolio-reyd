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

# Sidebar content
with st.sidebar:
    st.header("Personal Details")
    
    # Attempt to load the image with fallback
    image_path = "src/assets/garcia.png"
    fallback_path = "assets/garcia.png"
    image = load_image(image_path, fallback_path)
    
    if image:
        circular_image = make_image_circular(image, size=(100, 100))
        st.image(circular_image, width=100)  # Set width to enforce display size
    
    st.markdown("**Zodiac Sign:** Aries ♈")
    st.markdown("**Birthstone:** Diamond 💎")
    st.markdown("**Year of the Rabbit:** 兔")

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
            <a href="https://github.com/yourusername" target="_blank"><img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=FFFFFF" alt="GitHub"></a>
            <a href="https://www.upwork.com/freelancers/~yourprofile" target="_blank"><img src="https://simpleicons.org/icons/upwork.svg" alt="Upwork"></a>
            <a href="https://www.linkedin.com/in/yourprofile" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=FFFFFF" alt="LinkedIn"></a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("######")
    st.button("Message Me")

with right_col:
    image_path = "src/assets/myBanner.png"
    fallback_path = "assets/myBanner.png"
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
        {"name": "C", "logo": "https://www.svgrepo.com/show/347724/c.svg"},
        {"name": "C++", "logo": "https://www.svgrepo.com/show/347739/c-plusplus.svg"},
        {"name": "C#", "logo": "https://www.svgrepo.com/show/452207/c-sharp.svg"}
    ],
    "Tools": [
        {"name": "VSCode", "logo": "https://www.svgrepo.com/show/374171/vscode.svg"},
        {"name": "Git", "logo": "https://www.svgrepo.com/show/452210/git.svg"},
        {"name": "Docker", "logo": "https://www.svgrepo.com/show/448221/docker.svg"}
    ],
    "Deployment": [
        {"name": "Azure", "logo": "https://www.svgrepo.com/show/331302/azure-v2.svg"},
        {"name": "Render", "logo": "https://www.svgrepo.com/show/354890/render.svg"},
        {"name": "Aiven", "logo": "https://www.svgrepo.com/show/464379/aiven.svg"},
        {"name": "Vercel", "logo": "https://www.svgrepo.com/show/361653/vercel-logo.svg"}
    ],
    "Databases": [
        {"name": "MongoDB", "logo": "https://www.svgrepo.com/show/354370/mongodb.svg"},
        {"name": "SQLite", "logo": "https://www.svgrepo.com/show/360570/sqlite.svg"},
        {"name": "MySQL", "logo": "https://www.svgrepo.com/show/327527/mysql.svg"}
    ],
    "Languages & Frameworks": [
        {"name": "PHP", "logo": "https://www.svgrepo.com/show/303551/php.svg"},
        {"name": "Flask", "logo": "https://www.svgrepo.com/show/436157/flask.svg"}
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
