import streamlit as st
import requests

# Diqqat: Bu API URL sizning o'zingiz Hugging Face Spaces'ga yuklagan backend url manzilingiz bo'lishi kerak.
API_URL = "https://mekfnjenfe-ai1.hf.space/chat"

st.set_page_config(page_title="NOVA AI", page_icon="⚡", layout="centered")

# Cyberpunk dizayn uchun maxsus CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&display=swap');
    
    /* Asosiy fon qora */
    .stApp {
        background-color: #050505;
    }
    
    /* NOVA Logotipi uslubi (Orbitron, yashil yozuv va qizil soya) */
    .nova-logo {
        font-family: 'Orbitron', sans-serif;
        font-size: 60px;
        font-weight: 900;
        text-align: center;
        color: #39ff14; 
        text-shadow: 0 0 20px rgba(255, 0, 0, 0.8), 0 0 50px rgba(255, 0, 0, 0.5); 
        letter-spacing: 10px;
        margin-top: 10px;
        margin-bottom: 0px;
    }
    
    /* Chat qabariqlari (Yashil chegarali, qizil soyali qora qutilar) */
    .stChatMessage {
        background-color: #0a0a0a !important;
        border: 1px solid #39ff14; 
        border-radius: 8px;
        box-shadow: 0px 0px 25px 2px rgba(220, 20, 60, 0.3); 
        padding: 15px;
        margin-bottom: 20px;
        color: #e0e0e0;
    }
    
    /* Chat yozish kiritish qutisi */
    .stChatInputContainer {
        border: 1px solid #39ff14 !important;
        box-shadow: 0px 0px 15px rgba(220, 20, 60, 0.4) !important;
        border-radius: 8px !important;
        background-color: #0a0a0a !important;
    }
    
    .stChatInputContainer textarea {
        color: #39ff14 !important;
    }
    
    /* Kichik yozuv */
    .sub-text {
        text-align: center;
        color: #888888;
        font-family: 'Courier New', Courier, monospace;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='nova-logo'>NOVA</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>SYSTEM INITIALIZED: 100% LOCAL INDEPENDENT AI</div>", unsafe_allow_html=True)
st.divider()

if "history" not in st.session_state:
    st.session_state.history = []

# Display history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Yozing..."):
    
    # User message
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
             
    # Assistant response
    with st.chat_message("model"):
        with st.spinner("Miya o'ylamoqda (Local API)..."):
            try:
                response = requests.post(API_URL, json={"message": prompt})
                if response.status_code == 200:
                    reply = response.json().get("reply", "Xatolik!")
                else:
                    reply = f"API ga ulanishda xato: {response.status_code}"
            except Exception as e:
                reply = f"API ishlamayapti! (Iltimos API url manzilini to'g'rilang yoki Backend server uxlab qolmaganiga ishonch hosil qiling)\n\nSystem Error: {str(e)}"
                
        st.markdown(reply)
        
    st.session_state.history.append({"role": "model", "content": reply})
