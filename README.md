# 🤖 TalentScout – AI Hiring Assistant Chatbot

TalentScout is an **AI-powered hiring assistant** designed to streamline the initial candidate screening process for technology roles.  
It collects candidate details, confirms them, and generates **tailored technical interview questions** based on the candidate’s declared tech stack.  

---

## 🌟 Features
- Multi-step conversational flow: **Intro → Form → Confirmation → Chatbot Interview**
- Collects candidate details:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position(s)
  - Current Location
  - Tech Stack (e.g., Python, SQL, Flask)
- **Tailored technical questions** based on declared tech stack
- **Context-aware conversation** (no repetition, varied topics)
- **Fallback mechanism** for unclear answers
- **Universal exit handling** (type `exit`, `quit`, or `bye` anytime)
- Graceful conversation ending with next-step instructions

---

## 🛠️ Tech Stack
- **Python** – core language  
- **Streamlit** – user interface  
- **Groq LLM** – question generation & natural language processing  
- **python-dotenv** – secure API key loading  
- **Git** – version control  

---

## ⚡ Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/TejaswiRokkam/TalentScout.git
cd TalentScout
```
### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Add API Key
Create a .env file in the project root:
```bash
GROQ_API_KEY=your_api_key_here
```
### 5. Run the App
```bash
streamlit run app.py
```

---

## 🎬 Usage
- The chatbot greets the candidate and asks permission to proceed.  
- Candidate fills in their details in the form.  
- Details are shown for confirmation.  
- Chatbot starts interview:  
  - Asks varied technical questions based on candidate’s tech stack  
  - Maintains context across Q/A  
  - Allows candidate to exit anytime (`exit`, `quit`, `bye`)  
  - Provides fallback for unclear answers  

  
---


## 🔒 Data Privacy
- Candidate data is stored **temporarily in session state** (not persisted).  
- No sensitive data is saved or logged.  
- API keys are secured with `.env` files.  


---

## 🚀 Future Enhancements

- **Sentiment Analysis**: Detect candidate emotions and adapt questions accordingly.  
- **Multilingual Support**: Allow candidates to interact in multiple languages.  
- **Cloud Deployment**: Deploy on Streamlit Cloud, AWS, or GCP for a live demo.  
- **Personalized Interviews**: Store candidate history to tailor future interview sessions.

---

## 👨‍💻 Author
**Tejaswi Rokkam**  
AI/ML Enthusiast 
Documentaion: https://docs.google.com/document/d/1MlTCt_gJa1nUD4RF-Kht8vYXJ0l93gpCtvlAG9MR9Ug/edit?tab=t.0#heading=h.ugg8hfkoh81

📧 Email: rokkamtejaswi10@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/tejaswi-rokkam-55b089259)
