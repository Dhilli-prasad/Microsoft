import html
import re
from typing import Any, Dict, List

import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai

# App metadata and the strict persona instruction used for every response.
APP_TITLE = "SkillYatra AI"
CORE_MODEL_NAME = "gemini-2.5-flash"
SYSTEM_PROMPT = (
    "You are SkillYatra AI, an expert career mentor combining the conversational depth of ChatGPT and the factual accuracy of Perplexity. "
    "The user is either a student or a technical employee. Your job is to output concrete step-by-step career roadmaps, real-world company interview questions, semester timelines, and specific technical explanations. "
    "IMPORTANT: Whenever explaining a process or a roadmap, you MUST also output a valid syntax block for a Mermaid flowchart wrapped inside ```mermaid text blocks so the app can render a diagram visually for them. "
    "CRITICAL MERMAID GRAPH RULE: When formatting the ```mermaid flowchart code blocks, you must ensure every text label inside a node is safely wrapped in double quotes, for example: A[\"Node Text Here\"]. Do not include colons (:), asterisks (*), or brackets inside the node text blocks under any circumstances. Keep arrows simple using standard --> syntax."
)
# Match the requested dashboard layout exactly.
st.set_page_config(page_title=APP_TITLE, page_icon="🎓", layout="wide")


def inject_custom_styles() -> None:
    # Premium dark-mode styling for the full dashboard.
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(46, 204, 113, 0.14), transparent 28%),
                    radial-gradient(circle at top right, rgba(88, 166, 255, 0.15), transparent 32%),
                    linear-gradient(180deg, #07111f 0%, #0b1220 45%, #050812 100%);
                color: #f3f6fb;
            }
            html, body, [class*="css"] {
                font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }
            section[data-testid="stSidebar"] {
                background: rgba(10, 16, 28, 0.72);
                backdrop-filter: blur(20px);
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }
            .sk-title {
                font-size: 2.35rem;
                font-weight: 800;
                letter-spacing: -0.04em;
                background: linear-gradient(90deg, #ffffff, #9ad7ff, #6dffbd);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.15rem;
            }
            .sk-subtitle {
                color: rgba(232, 240, 255, 0.8);
                font-size: 1rem;
                margin-top: 0;
                margin-bottom: 1rem;
            }
            .glass-card {
                background: rgba(15, 23, 42, 0.7);
                border: 1px solid rgba(255, 255, 255, 0.09);
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.28);
                border-radius: 18px;
                padding: 1rem 1.15rem;
            }
            .hint-pill {
                display: inline-block;
                padding: 0.35rem 0.7rem;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.06);
                color: rgba(255, 255, 255, 0.84);
                border: 1px solid rgba(255, 255, 255, 0.08);
                margin-right: 0.4rem;
                margin-bottom: 0.4rem;
                font-size: 0.85rem;
            }
            [data-testid="stChatMessage"] {
                background: rgba(10, 15, 24, 0.48);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 18px;
                backdrop-filter: blur(18px);
                margin-bottom: 0.75rem;
            }
            [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
            [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] li {
                color: rgba(245, 248, 255, 0.95);
                line-height: 1.65;
            }
            [data-testid="stChatMessage"] code {
                background: rgba(255, 255, 255, 0.08);
                border-radius: 6px;
                padding: 0.15rem 0.35rem;
            }
            .stAlert {
                border-radius: 14px;
            }
            div[data-testid="stProgressBar"] > div {
                background: linear-gradient(90deg, #24d17e, #22c1ff);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_state() -> None:
    # Centralized defaults keep resets predictable.
    defaults = {
        "messages": [],
        "api_key": "",
        "category": "Semester Exam Preparation",
        "completion": 35,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def clear_chat_history() -> None:
    # Wipe all session keys to return to a pristine state.
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    initialize_state()


def extract_mermaid_blocks(text: str) -> List[str]:
    # Pull every Mermaid code fence from a model response.
    pattern = re.compile(r"```mermaid\s*(.*?)```", re.IGNORECASE | re.DOTALL)
    blocks = []
    for match in pattern.findall(text or ""):
        cleaned = match.strip()
        if cleaned:
            blocks.append(cleaned)
    return blocks


def strip_mermaid_blocks(text: str) -> str:
    # Remove diagram fences before rendering the assistant text.
    return re.sub(r"```mermaid\s*.*?```", "", text or "", flags=re.IGNORECASE | re.DOTALL).strip()


def render_mermaid_diagram(mermaid_code: str, key: str) -> None:
    # Draw a live Mermaid diagram underneath the chat response.
    safe_code = html.escape(mermaid_code)
    diagram_html = f"""
    <div style="
        background: rgba(10, 16, 28, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 0.85rem;
        margin: 0.35rem 0 1rem 0;
        overflow-x: auto;
        box-shadow: 0 14px 34px rgba(0, 0, 0, 0.22);
    ">
        <div class="mermaid">{safe_code}</div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        if (window.mermaid) {{
            mermaid.initialize({{ startOnLoad: true, theme: 'dark', securityLevel: 'loose' }});
        }}
    </script>
    """
    components.html(diagram_html, height=420, scrolling=True)


def render_assistant_response(response_text: str, message_index: int) -> None:
    # Render the assistant message and any embedded flowchart.
    text_without_diagrams = strip_mermaid_blocks(response_text)
    mermaid_blocks = extract_mermaid_blocks(response_text)

    if text_without_diagrams:
        st.markdown(text_without_diagrams)

    for idx, block in enumerate(mermaid_blocks):
        render_mermaid_diagram(block, key=f"mermaid_{message_index}_{idx}")


def build_prompt(category: str, completion: int, user_query: str) -> str:
    # Add prep context so the response stays focused and actionable.
    category_context = (
        f"The user is preparing for: {category}. "
        f"Current preparation completion is {completion}%. "
        "Tailor the answer to be practical, structured, and actionable. "
        "When a roadmap or process is involved, include a Mermaid flowchart."
    )
    return f"{category_context}\n\nUser query: {user_query}"


def generate_gemini_response(api_key: str, messages: List[Dict[str, Any]], user_query: str, category: str, completion: int) -> str:
    # Configure Gemini with the exact core model required by the app.
    genai.configure(api_key=api_key.strip())
    model = genai.GenerativeModel(
        model_name=CORE_MODEL_NAME,
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.6,
            "top_p": 0.95,
            "max_output_tokens": 2048,
        },
    )

    prompt = build_prompt(category, completion, user_query)

    # Map roles for Gemini API compatibility (user=user, assistant=model).
    gemini_messages = []
    for msg in messages:
        api_role = "user" if msg["role"] == "user" else "model"
        content = msg.get("content", "")
        if content:
            gemini_messages.append({"role": api_role, "parts": [content]})

    chat = model.start_chat(history=gemini_messages[:-1] if len(gemini_messages) > 1 else None)
    stream = chat.send_message(prompt, stream=True)

    chunks = []
    for chunk in stream:
        chunk_text = getattr(chunk, "text", "")
        if chunk_text:
            chunks.append(chunk_text)
    return "".join(chunks).strip()


inject_custom_styles()
initialize_state()

# Sidebar control panel for key, focus mode, and progress tracking.
with st.sidebar:
    st.markdown("## Configuration Dashboard")
    st.caption("Control the assistant persona, intent, and readiness status.")

    gemini_key = st.text_input(
        "Paste Gemini API Key:",
        type="default",
        placeholder="Paste your Gemini API key here",
        help="Stored only in your browser session state for this app run.",
    )
    st.session_state.api_key = gemini_key

    st.session_state.category = st.selectbox(
        "Focus Area Mode",
        [
            "Semester Exam Preparation",
            "Placement Drive & Mock Interviews",
            "Company Switching & Career Guidance",
        ],
        index=[
            "Semester Exam Preparation",
            "Placement Drive & Mock Interviews",
            "Company Switching & Career Guidance",
        ].index(st.session_state.category) if st.session_state.category in [
            "Semester Exam Preparation",
            "Placement Drive & Mock Interviews",
            "Company Switching & Career Guidance",
        ] else 0,
    )

    st.session_state.completion = st.slider(
        "Current Syllabus/Preparation Completion (%)",
        min_value=0,
        max_value=100,
        value=int(st.session_state.completion),
        step=1,
    )
    st.progress(st.session_state.completion / 100.0)

    if st.session_state.completion < 50:
        st.warning("Your current preparation looks early-stage. Focus on fundamentals and a weekly target plan.")
    elif st.session_state.completion > 80:
        st.success("Great momentum — you are in the final polishing phase.")
    else:
        st.info("You are in the middle phase. Keep revising and do timed practice daily.")

    if st.button("Clear Chat History", use_container_width=True, type="primary"):
        clear_chat_history()
        st.rerun()

# Main page title and summary.
st.markdown('<div class="sk-title">SkillYatra AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sk-subtitle">The Ultimate Career, Placement & Semester Engine for practical roadmaps, mock interviews, and semester planning.</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="glass-card">
        <span class="hint-pill">ChatGPT-like guidance</span>
        <span class="hint-pill">Perplexity-style clarity</span>
        <span class="hint-pill">Gemini-powered answers</span>
        <span class="hint-pill">Mermaid visual roadmaps</span>
    </div>
    """,
    unsafe_allow_html=True,
)

for idx, message in enumerate(st.session_state.messages):
    # Rehydrate the conversation history cleanly on rerun.
    with st.chat_message(message["role"]):
        content = message.get("content", "")
        if message["role"] == "assistant":
            render_assistant_response(content, idx)
        else:
            st.markdown(content)

user_query = st.chat_input("Ask a question about placement rounds, semester backlogs, or switching companies...")

if user_query:
    # Save the user query before generating the assistant response.
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    if not st.session_state.api_key.strip():
        # Keep the UX gentle when no Gemini key is configured.
        reminder = "Please add your Gemini API key in the sidebar to start generating AI responses."
        st.session_state.messages.append({"role": "assistant", "content": reminder})
        with st.chat_message("assistant"):
            st.info(reminder)
    else:
        # Stream a Gemini response inside a spinner for a responsive feel.
        with st.chat_message("assistant"):
            with st.spinner("SkillYatra AI is thinking..."):
                try:
                    assistant_text = generate_gemini_response(
                        api_key=st.session_state.api_key,
                        messages=st.session_state.messages,
                        user_query=user_query,
                        category=st.session_state.category,
                        completion=st.session_state.completion,
                    )
                    if not assistant_text:
                        assistant_text = "I could not generate a response. Please try again with a more specific question."
                    st.session_state.messages.append({"role": "assistant", "content": assistant_text})
                    render_assistant_response(assistant_text, len(st.session_state.messages) - 1)
                except Exception as exc:
                    error_message = (
                        "I ran into an issue while contacting Gemini. "
                        "Please verify your API key, network access, and model availability."
                    )
                    st.session_state.messages.append({"role": "assistant", "content": f"{error_message}\n\nDetails: {exc}"})
                    st.error(error_message)
                    st.caption(str(exc))
