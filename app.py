import streamlit as st
import time
import datetime
import random
import base64
import os
import streamlit.components.v1 as components

# --- CONFIGURATION ---
st.set_page_config(page_title="Birthday Surprise", layout="wide")

# --- NAVIGATION SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- GLOBAL STYLES ---
st.markdown("""
<style>
    .stApp { background-color: #FFF0F5; font-family: 'Comic Sans MS', cursive, sans-serif; }
    h1, h2, h3 { color: #ff4d79; }
    .dash-card {
        background:#ffffff; padding:20px; border-radius:20px;
        text-align:center; box-shadow:0px 10px 25px rgba(0,0,0,0.2);
        color: #ff4d79; font-weight: bold; margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #ff4d79 !important; color: white !important;
        border-radius: 20px !important; width: 100%;
        border: none !important;
    }
    .letter-box {
        background: #fffaf0; padding:30px; border-radius:15px; 
        border:2px solid #e6c9a8; color:#000; font-size:18px; line-height:1.8;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---

# 1. HOME PAGE
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>Happy Birthday हिंदकेसरी ❤️</h1>", unsafe_allow_html=True)

    # Combined Countdown, Heart Rain, and Sparkles
    components.html("""
    <style>
    .countdown-box { text-align:center; font-size:40px; font-weight:bold; color:#ff2d6b; font-family: sans-serif; }
    .heart { position: fixed; top: -50px; color: #ff2d6b; font-size: 28px; animation: fall linear infinite; z-index: 9999; }
    @keyframes fall { 0% { transform: translateY(-50px) rotate(0deg); opacity: 1; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }
    .sparkle { position: fixed; width: 6px; height: 6px; border-radius: 50%; background: white; box-shadow: 0 0 15px white; animation: sparkle 2s linear infinite; z-index: 9999; }
    @keyframes sparkle { 0% {opacity:0;} 50% {opacity:1;} 100% {opacity:0;} }
    </style>

    <div style='text-align:center; font-family: sans-serif;'>
        <h2 style='color:#ff2d6b;'>⏳ Birthday Countdown ⏳</h2>
        <div id="timer" class="countdown-box"></div>
        <p style="color:#ff4d79; font-size:22px;">Your special moment is getting closer my princess 💖💖</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
    function createHeart(){
      const heart = document.createElement("div");
      heart.classList.add("heart"); heart.innerHTML = "❤️";
      heart.style.left = Math.random()*100+"%";
      heart.style.animationDuration = (3 + Math.random()*3)+"s";
      document.body.appendChild(heart);
      setTimeout(()=>heart.remove(),5000);
    }
    setInterval(createHeart,400);

    function sparkleGlow(){
      const s = document.createElement("div");
      s.classList.add("sparkle");
      s.style.left = Math.random()*100+"%"; s.style.top = Math.random()*100+"%";
      document.body.appendChild(s);
      setTimeout(()=>s.remove(),2000);
    }
    setInterval(sparkleGlow,300);

    function countdown(){
        const target = new Date("Jan 3, 2026 00:00:00").getTime();
        const now = new Date().getTime();
        const diff = target - now;
        if(diff <= 0){
            document.getElementById("timer").innerHTML = "🎉 It's Your Special Day 🎉";
            confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
            return;
        }
        let totalSeconds = Math.floor(diff / 1000);
        let hh = Math.floor(totalSeconds / 3600).toString().padStart(2,'0');
        let mm = Math.floor((totalSeconds % 3600) / 60).toString().padStart(2,'0');
        let ss = (totalSeconds % 60).toString().padStart(2,'0');
        document.getElementById("timer").innerHTML = hh + " : " + mm + " : " + ss;
    }
    setInterval(countdown,1000);
    </script>
    """, height=400)

    # Music Player Component
    components.html("""
    <iframe id="ytplayer" width="0" height="0" src="https://www.youtube.com/embed/9OQBDdNHmXo?start=212&autoplay=1&loop=1&playlist=9OQBDdNHmXo&mute=1" frameborder="0" allow="autoplay"></iframe>
    <button onclick="document.getElementById('ytplayer').src='https://www.youtube.com/embed/9OQBDdNHmXo?start=225&autoplay=1&loop=1&playlist=9OQBDdNHmXo&mute=0'" 
    style="position: fixed; bottom: 20px; right: 20px; background:#ff4d79; color:white; padding:12px 18px; border-radius:30px; font-size:18px; border:none; box-shadow:0px 5px 20px rgba(0,0,0,0.3); cursor:pointer; z-index:9999;">
    🔊 Birthday Song
    </button>
    """, height=80)

    # Dashboard Cards
    st.markdown("### 🌸 Birthday Surprise 🌸")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='dash-card'>🎥 Video Surprise 1</div>", unsafe_allow_html=True)
        if st.button("Open Video 1 🎁"): go_to("video1")
    with col2:
        st.markdown("<div class='dash-card'>🎥 Video Surprise 2</div>", unsafe_allow_html=True)
        if st.button("Open Video 2 🎁"): go_to("video2")
    with col3:
        st.markdown("<div class='dash-card'>🎉 Fun Zone Game</div>", unsafe_allow_html=True)
        if st.button("Play Game 🥳"): go_to("fun_zone")

    st.write("---")
    if st.button("💌 Read My Heart Letter"): go_to("letter")

    # Scattered Images Logic
    st.markdown("### 💖 Memories Scattered Like Stickers 💖")
    images = [f"photo{i}.jpeg" for i in range(1,11)] 
    positions = [(50,100),(200,300),(400,150),(650,200),(900,100),(150,600),(350,500),(600,550),(850,450),(1050,300)]
    html_img = "<div style='position:relative; height:900px;'>"
    for i, img in enumerate(images):
        if os.path.exists(img):
            with open(img, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            rotate = random.randint(-15,15)
            top, left = positions[i]
            html_img += f"<img src='data:image/jpeg;base64,{data}' style='width:180px; height:180px; object-fit:cover; border-radius:10px; position:absolute; top:{top}px; left:{left}px; transform:rotate({rotate}deg); box-shadow:0px 6px 18px rgba(0,0,0,0.3);'>"
    html_img += "</div>"
    components.html(html_img, height=950)

# 2. VIDEO SURPRISE 1
elif st.session_state.page == "video1":
    st.markdown("<h1 style='text-align:center;'>🎬 Video Surprise 1 🎬</h1>", unsafe_allow_html=True)
    if os.path.exists("video1.mp4"):
        st.video("video1.mp4")
        st.markdown("### 💗 Edit Queen 💝")
    else:
        st.error("video1.mp4 not found!")
    if st.button("⬅️ Back to Dashboard"): go_to("home")

# 3. VIDEO SURPRISE 2
elif st.session_state.page == "video2":
    st.markdown("<h1 style='text-align:center;'>🎥 Video Surprise 2 🎥</h1>", unsafe_allow_html=True)
    if os.path.exists("video2.mp4"):
        st.video("video2.mp4")
        st.markdown("### ✨ Cheers to your TikTok Era! purely Nostalgia. 💞")
    else:
        st.error("video2.mp4 not found!")
    if st.button("⬅️ Back to Dashboard"): go_to("home")

# 4. FUN ZONE
elif st.session_state.page == "fun_zone":
    st.markdown("<h1 style='text-align:center;'>🎉 Fun Zone – Cute Questionnaire 🎉</h1>", unsafe_allow_html=True)
    st.text_input("🍓 What is my favorite thing about you?", key="q1")
    st.text_input("🌹 Where was our best date?", key="q2")
    st.radio("🐒 Who is the most naughty one?", ["You 😈", "Me 😎", "Both of us 😜"], key="q3")
    if st.button("Check Answers 💖"):
        st.success("Awww that was soooo cuteeeee! 💕💫😍")
        st.balloons()
        st.snow()
    if st.button("⬅️ Back to Dashboard"): go_to("home")

# 5. THE LETTER
elif st.session_state.page == "letter":
    st.markdown("<h1 style='text-align:center;'>💌 माझ्या मनातलं बोल 💌</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='letter-box'>
    तुझ्या येण्याने माझ्या आयुष्याला मिळाला गोड प्रकाश,  
तुझ्या नावानेच धडधडतो आता प्रत्येक श्वास.  
पहिल्यांदा पाहिलंस जेव्हा हसत हसत माझ्याकडे,  
तेव्हाच मनानं ठरवलं, “हीच राहो सोबत शेवटच्या श्वासापर्यंत माझ्याबरोबर.”  

तू रुसलीस की ढग जमतात माझ्या आकाशात,  
तू हसलीस की उमलतात फुलं माझ्या प्रत्येक श्वासात.  
तुझ्या छोट्याशा “काळजी घे रे” मध्ये दडलेलं असतं माझं विश्व,  
तुझ्या डोळ्यांत बघताना विसरतो सगळं, फक्त वाटतं “हीच आहे माझं सर्वस्व.”  

तुझ्या हातात माझा हात असला की वाटतं सगळं काही आहे,  
जग काहीही म्हणू दे, तुझ्याविना मात्र काहीच राहिले नाहीये.  
प्रत्येक स्वप्नात तू, प्रत्येक प्रार्थनेत तूच नाव,  
देवाकडे एकच विनंती, “हीच राहू दे माझ्या शेजारी, जरी कमी मिळाले जगातलं ठाव.”  

आज तुझा दिवस, माझ्यासाठीही सगळ्यात खास,  
तुझ्या सोबतच सुरु होऊ दे प्रत्येक नवीन प्रवास.  
तुझ्या डोळ्यांतील प्रत्येक स्वप्नाला मिळो स्वतःचं आकाश,  
तुझ्या आनंदासाठी देईन प्रत्येक क्षण, प्रत्येक श्वास.  

वाढदिवसाच्या खूप खूप शुभेच्छा माझ्या *प्रेमाला*,  
तूच माझं आज, उद्याचं आणि संपूर्ण जगाला. 🎂💫
    </div>
    """, unsafe_allow_html=True)
    if st.button("⬅️ Back to Dashboard"): go_to("home")