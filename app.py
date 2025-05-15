import gradio as gr
from agent_runner import generate_subtasks

def agent_interface(goal):
    if not goal.strip():
        return "⚠️ Please enter a goal."
    try:
        return generate_subtasks(goal)
    except Exception as e:
        return f"❌ Error: {str(e)}"

iface = gr.Interface(
    fn=agent_interface,
    inputs=gr.Textbox(label="Enter your goal", placeholder="e.g., I want to start a YouTube channel..."),
    outputs=gr.Textbox(label="3-Step Task Plan"),
    title="🧠 Mini Agent with Local Chained Tasks",
    description="Breaks your goal into 3 actionable steps using a local LLM (Mistral via Ollama)"
)

if __name__ == "__main__":
    iface.launch()
