# SkillYatra AI - The Ultimate Career, Placement & Semester Engine

A production-ready **Streamlit web application** that combines the conversational depth of ChatGPT, the structured clarity of Perplexity, and the intelligence of Google Gemini to help students and professionals with:

- 📚 **Semester Exam Preparation** – Syllabus tracking, subject breakdowns, and study roadmaps
- 💼 **Placement Drive & Interview Prep** – Real company round questions, mock interview scenarios, and hiring insights
- 🚀 **Company Switching & Career Growth** – Career path guidance, skill gaps, and company-specific strategies

## Features

✨ **AI-Powered Career Mentoring**
- Real-time conversational AI using Google Gemini 2.5 Flash
- Context-aware responses based on your preparation focus area and completion status
- Structured, actionable guidance for career and academic growth

📊 **Smart Preparation Tracker**
- Real-time syllabus/prep completion slider (0–100%)
- Visual progress bar with contextual warnings and success banners
- Focus area mode selection for tailored advice

🎨 **Visual Flowchart Diagrams**
- Automatic Mermaid flowchart generation from AI responses
- Real-time rendering of career roadmaps, process timelines, and interview question hierarchies
- Live interactive diagrams embedded directly in the chat

💬 **Full Chat History Management**
- Persistent conversation history during your session
- One-click "Wipe Chat History" button to start fresh
- Seamless message rehydration on app rerun

🎯 **Premium Dark-Mode Dashboard**
- Glassmorphism design with smooth gradients and blur effects
- Developer-friendly, polished UI with smooth interactions
- Responsive layout optimized for all screen sizes

## Quick Start

### Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- **Google Gemini API Key** (free tier available at [aistudio.google.com](https://aistudio.google.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dhilli-prasad/Microsoft.git
   cd Microsoft
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
streamlit run app.py
```

The app will launch locally at **`http://localhost:8501`**

## Configuration

### Getting Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create new secret key"**
4. Copy the API key
5. Paste it into the **"Paste Gemini API Key:"** field in the app sidebar

> **Security Note:** Your API key is stored only in your browser session state during the app run. It is never saved to disk or transmitted beyond your local session.

### Sidebar Controls

- **Paste Gemini API Key:** Enter your Google Gemini API key
- **Focus Area Mode:** Select your preparation focus (Semester Exam, Placement, Company Switching)
- **Syllabus/Prep Completion (%):** Slider to track your current preparation status
- **Wipe Chat History:** Clear all messages and start a fresh session

## How It Works

### The AI Brain

SkillYatra AI uses **Google Gemini 2.5 Flash** with a specialized system prompt that enforces:

1. **Expert career mentoring** with concrete, real-world advice
2. **Automatic Mermaid diagram generation** for every process/roadmap explanation
3. **Safe flowchart syntax** to prevent rendering errors (proper node labeling, no colons/asterisks)
4. **Focus-aware responses** that adapt to your selected preparation mode

### Chat Flow

1. **You ask a question** about placement, semester prep, or career growth
2. **Gemini AI analyzes** your query with context about your preparation status
3. **The model generates** a structured response + embedded Mermaid flowchart
4. **SkillYatra extracts** the flowchart and renders it visually beneath the response
5. **Full message history** is maintained for conversation continuity

## Project Structure

```
Microsoft/
├── app.py              # Main Streamlit application (337 lines, fully functional)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .git/               # Git version control
```

## Technologies Used

- **[Streamlit](https://streamlit.io)** – Web app framework
- **[Google Generative AI](https://ai.google.dev)** – Gemini 2.5 Flash model
- **[Mermaid.js](https://mermaid.js.org)** – Flowchart rendering
- **Python 3.10+** – Core language

## API Role Mapping

SkillYatra AI automatically handles Google Gemini API compatibility by mapping internal roles:
- `user` → `user` (your messages)
- `assistant` → `model` (AI responses)

This ensures full compatibility with Gemini's API specifications.

## Troubleshooting

### 404 Error on Model Name
**Solution:** The app uses `gemini-2.5-flash`. If you see errors, ensure your Gemini API key is valid and your account has access to this model.

### Mermaid Diagram Not Rendering
**Solution:** Check that the AI response includes a valid `\`\`\`mermaid ... \`\`\`` block. The system prompt enforces safe syntax, but ensure no colons or special characters appear inside node labels.

### "Please add your Gemini API key" message
**Solution:** Paste a valid API key in the sidebar **"Paste Gemini API Key:"** field. Create one at [aistudio.google.com](https://aistudio.google.com) if you don't have one.

### API Authentication Failed
**Solution:** Verify your API key is correct and your network connection is active. Google's API endpoints must be reachable.

## Contributing

This is a production-ready single-file application. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Test your changes locally
4. Commit and push (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is open-source and available under the MIT License.

## Support & Feedback

- **Issues:** Open an issue on [GitHub](https://github.com/Dhilli-prasad/Microsoft/issues)
- **Feedback:** Feel free to reach out with suggestions for career guidance features

---

**Built with ❤️ for students and professionals aiming to excel in their careers.**

**Get started now:** Clone the repo, add your Gemini API key, and launch the app!

```bash
git clone https://github.com/Dhilli-prasad/Microsoft.git
cd Microsoft
pip install -r requirements.txt
streamlit run app.py
```
