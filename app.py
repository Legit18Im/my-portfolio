import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Jay Shahapurakar | AI Engineer", page_icon="🤖", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Jay Bharamu Shahapurakar")
    st.write("📍 Belgaum, Karnataka")
    st.write("📧 jayshahapurakar@gmail.com")
    st.write("📱 8296597356")
    st.markdown("[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)") # Update these links!
    
    # RESUME DOWNLOAD BUTTON
    # Ensure you have a file named 'resume.pdf' in the same folder as this script
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=pdf_bytes,
            file_name="Jay_Shahapurakar_Resume.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.warning("⚠️ Please upload 'resume.pdf' to the GitHub folder.")

# --- MAIN CONTENT ---
st.title("🤖 AI Engineer & Data Scientist")
st.write("### Building scalable ML pipelines and solving real-world problems.")

st.markdown("---")

# --- SKILLS ---
st.subheader("🛠 Technical Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Languages:** Python, SQL, C++")
with col2:
    st.markdown("**ML/DL:** TensorFlow, Keras, OpenCV, Scikit-learn")
with col3:
    st.markdown("**Tools:** Docker, Git, AWS, Flask, Django")

st.markdown("---")

# --- PROJECTS ---
st.subheader("💻 Featured Projects")

# Project 1
with st.container():
    st.write("### 📄 AI ATS Resume Scanner")
    st.write("Built a full-stack system using **Django & SBERT** to score resumes against job descriptions semantically.")
    st.write("- **Tech:** Python, NLP, Spacy, PDFPlumber")
    st.write("- **Impact:** Automated parsing and weighted scoring for HR efficiency.")

# Project 2
with st.container():
    st.write("### 🔍 Anomaly Detection System (CCTV)")
    st.write("Developed a hybrid **CNN + LSTM** model to detect accidents and fire in real-time video feeds.")
    st.write("- **Tech:** OpenCV, Deep Learning, Real-time Inference")
    st.write("- **Impact:** Achieved 92% accuracy in event classification.")

# Project 3
with st.container():
    st.write("### 💳 Credit Card Default Prediction")
    st.write("Created a credit risk model using **XGBoost** and deployed it via **Flask API**.")
    st.write("- **Tech:** Pandas, Scikit-learn, REST API")
    st.write("- **Impact:** Improved prediction accuracy to 84%.")

st.markdown("---")

# --- EXPERIENCE ---
st.subheader("💼 Experience")
st.write("**AI Engineer @ GTechnoHubb Solutions** (04/2025 - Present)")
st.write("- Building production ML/DL models and real-time inference pipelines.")

st.write("**Data Science Intern @ NullClass** (12/2024 - 04/2025)")
st.write("- Optimized ML models and contributed to data validation pipelines.")