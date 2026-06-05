# SkillYatra AI – Your Personal Career & Placement Mentor 🎓

Hey there! 👋

Welcome to **SkillYatra AI** – think of it as your always-available career buddy who's part ChatGPT, part Perplexity, and all Gemini-powered intelligence. Whether you're cramming for semester exams, grinding through placement season, or thinking about switching companies, this app's got your back.

## What Can You Use It For?

- **📚 Semester Exams?** Get study plans, subject breakdowns, and exam roadmaps
- **💼 Placements Coming Up?** Practice real interview questions, mock rounds, and insider hiring tips
- **🚀 Thinking of Switching Jobs?** Explore career paths, identify skill gaps, and plan your next move

Pretty much anything career or academic prep – just ask!

## What Makes It Special?

🧠 **Your AI Mentor Actually Listens**
- Chatbot that knows what you're preparing for (exams? interviews? career switch?)
- Gets smarter based on your current prep level (if you're 30% done, it won't throw advanced stuff at you)
- Gives you real, actionable advice – not generic fluff

📈 **See Your Progress**
- Slider to track how much of your prep is done (0–100%)
- Visual progress bar that encourages you
- Gets warnings if you're behind, celebrations when you're crushing it

📊 **Visual Roadmaps That Actually Help**
- AI auto-generates flowchart diagrams for every process or timeline
- See career paths, interview rounds, and study schedules as actual diagrams
- No more imagining – it's all visual and interactive

💾 **Keep Your Conversation Going**
- Your chat history sticks around during your session
- One button to clear everything and start fresh
- Feels like a real conversation, not a transactional chatbot

🎨 **Dark Mode That Doesn't Hurt Your Eyes**
- Premium, sleek dashboard design
- Smooth gradients and blur effects that look modern
- Works great on any screen size

## Getting Started (It's Easy, Promise!) ⚡

### What You Need First

- **Python 3.10+** – Grab it from [python.org](https://www.python.org/downloads/) if you don't have it
- **A Google Gemini API Key** – Free tier available! More on that in a sec
- **Git** (optional but recommended) – To clone the repo

### Step 1: Get the Code

```bash
git clone https://github.com/Dhilli-prasad/Microsoft.git
cd Microsoft
```

### Step 2: Set Up Your Python Environment

Think of this like creating a sandbox just for this project (keeps things clean):

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install What You Need

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Your API Key (Securely! 🔐)

The app reads your Gemini API key from Streamlit secrets – a secure, encrypted way to store sensitive info. Here's how:

1. Create a file called `secrets.toml` in the `.streamlit` folder (we've included a template):

   ```
   .streamlit/secrets.toml
   ```

2. Open it and add your Gemini API key (get it free from [aistudio.google.com](https://aistudio.google.com)):

   ```toml
   GEMINI_API_KEY = "your-actual-api-key-here"
   ```

3. **That's it!** The app automatically reads it when you start Streamlit.

> **Security note:** This file is listed in `.gitignore` so your key will never accidentally get pushed to GitHub. Keep it safe! 🔒

### Step 5: Fire It Up!

```bash
streamlit run app.py
```

Your app will open at **`http://localhost:8501`** in your browser. The API key loads automatically – no need to paste anything! 🚀

## How to Use It (The Fun Part!)

### Streamlit Secrets – Safe & Secure 🔐

Instead of typing your API key every time, SkillYatra AI reads it securely from Streamlit secrets:
- Your key is encrypted and stored locally
- Never gets accidentally pasted in the chat
- Never gets exposed in browser history
- `.gitignore` prevents it from being committed to GitHub

**Already set up?** Just run the app and start chatting – your key loads automatically! ✨

### The Sidebar Controls

**The sidebar is your control panel. Here's what each button does:**

1. **Focus Area Mode** – What are you prepping for?
   - Semester Exam Preparation
   - Placement Drive & Interview Prep
   - Company Switching & Career Growth

3. **Your Syllabus/Prep Completion (%)** – Drag the slider to show how far along you are


### Asking Questions

Just type in the chat input at the bottom. Some example questions:

- "I have Data Structures exam in 2 weeks, create a study roadmap"
- "What are typical Amazon round 2 questions?"
- "I want to switch from QA to DevOps, what skills do I need?"
- "Explain the difference between SQL and NoSQL with examples"

The AI will give you a detailed answer + a visual flowchart showing the process or timeline.

### What Happens Behind the Scenes

1. You ask a question
2. The app sends it to Google's Gemini AI (along with your prep level and focus area)
3. Gemini thinks about it and generates:
   - A detailed, structured answer
   - A Mermaid flowchart diagram (automatically!)
4. SkillYatra strips out the diagram code and renders it visually
5. You see the answer + a beautiful diagram, all in one place

Pretty seamless, right?

## The Tech Stack (For the Nerds 👨‍💻)

- **[Streamlit](https://streamlit.io)** – Makes building web apps super easy
- **[Google Generative AI](https://ai.google.dev)** – The Gemini 2.5 Flash brain
- **[Mermaid.js](https://mermaid.js.org)** – Draws the flowcharts
- **Python 3.10+** – The glue holding it all together

## Project Structure

Spoiler: it's simple! Just one powerful Python file:

```
Microsoft/
├── app.py           # Everything in here (yeah, one file!)
├── requirements.txt # What you need to install
├── README.md        # This file
└── .git/            # Git history
```

## Troubleshooting (When Things Go Sideways 🤔)

### "No API key found" message
**Probably:** Your `GEMINI_API_KEY` isn't set in `.streamlit/secrets.toml`
**Fix:** 
1. Open `.streamlit/secrets.toml`
2. Add your key: `GEMINI_API_KEY = "your-actual-key-here"`
3. Restart Streamlit (stop and run `streamlit run app.py` again)

### "I see a 404 error"
**Probably:** Your Gemini API key is invalid or your account doesn't have access
**Fix:** Double-check your API key at [aistudio.google.com](https://aistudio.google.com), make sure it's copied correctly

### "The flowchart isn't showing up"
**Probably:** The AI response didn't include a valid Mermaid block
**Fix:** Try asking a question that asks for a roadmap or process (e.g., "Create an interview prep timeline")

### "It keeps asking for my API key"
**Probably:** You pasted it wrong or there are extra spaces
**Fix:** Clear the input field and paste it carefully (no extra spaces at the start/end)

### "The app crashed / won't start"
**Probably:** Dependencies not installed
**Fix:** Run `pip install -r requirements.txt` again

### "I can't connect to Gemini"
**Probably:** Network issue or Gemini API is temporarily down
**Fix:** Check your internet connection, wait a minute, and try again

Still stuck? Open an issue on [GitHub](https://github.com/Dhilli-prasad/Microsoft/issues)!

## Want to Contribute? 🤝

This app is open-source, so contributions are welcome! Here's how:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/awesome-idea`)
3. Make your changes and test them locally
4. Commit them (`git commit -m "Add awesome feature"`)
5. Push to your fork (`git push origin feature/awesome-idea`)
6. Open a Pull Request!

We'd love to hear your ideas for new features.

## License

MIT License – basically, do whatever you want with this code, just give credit where it's due.

## Let's Connect 👋

- **Questions?** Open an issue on [GitHub](https://github.com/Dhilli-prasad/Microsoft/issues)
- **Want to chat?** Feel free to reach out with feedback or ideas
- **Found a bug?** Report it! We'll fix it ASAP

---

## TL;DR – Just Get Started!

```bash
# 1. Clone it
git clone https://github.com/Dhilli-prasad/Microsoft.git
cd Microsoft

# 2. Set it up
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt

# 3. Run it
streamlit run app.py

# 4. Open http://localhost:8501 in your browser

# 5. Paste your Gemini API key (free from aistudio.google.com)

# 6. Start chatting and get better at your career!
```

**That's it!** Welcome to SkillYatra AI. Now go crush those exams, nail those interviews, or plan that career move. You got this! 💪
