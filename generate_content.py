import os

categories = [
    "ai-cheatsheets", "ai-guides", "ai-tutorials", "ai-courses", "ai-workflow",
    "ai-tools", "ai-coding", "ai-productivity", "ai-case-studies", "ai-resources",
    "ai-career-tips", "ai-industry-specific", "ai-myths-debunked", "ai-agents",
    "ai-prompts", "ai-design-creative", "ai-model-comparisons", "ai-open-source",
    "ai-soft-skills", "ai-automation", "ai-personal-life"
]

topics = {
    "ai-cheatsheets": "Claude 3.5 Sonnet: The Advanced Prompting Cheat Sheet",
    "ai-guides": "The 2026 State of RAG: From Vector Search to Agentic Retrieval",
    "ai-tutorials": "Build Your Own Local Research Assistant with Ollama & LangGraph",
    "ai-courses": "Top 5 AI Agent Engineering Courses Worth Your Time in 2026",
    "ai-workflow": "How to Automate 80% of Technical Research Using AI Workflows",
    "ai-tools": "Beyond ChatGPT: 5 Specialized AI Tools for Strategic Analysis",
    "ai-coding": "Cursor + Sonnet 3.5: The New Standard for High-Velocity Development",
    "ai-productivity": "The 'Voice-to-Action' Framework: Turning Thoughts into Task Lists",
    "ai-case-studies": "How Klarna Saved $40M in Operations Costs Using AI Agents",
    "ai-resources": "10 AI Newsletters That Filter Hype from Reality",
    "ai-career-tips": "How to Transition from Traditional PM to AI Product Manager",
    "ai-industry-specific": "AI in Supply Chain: Predicting Disruptions Before They Happen",
    "ai-myths-debunked": "Why AI hasn't reached a 'Plateau' (and what's actually happening)",
    "ai-agents": "Multi-Agent Orchestration: Why One AI is Never Enough",
    "ai-prompts": "The 'Reasoning Loop' Prompt: Getting LLMs to Self-Correct",
    "ai-design-creative": "Flux.1: Achieving Brand Consistency in AI-Generated Imagery",
    "ai-model-comparisons": "Llama 3.1 405B vs GPT-4o: The Open Source vs Closed Battle",
    "ai-open-source": "Mistral NeMo: Why Small Models are Winning at the Edge",
    "ai-soft-skills": "AI-Human Feedback Loops: The Most Underrated Soft Skill",
    "ai-automation": "Building an Autonomous Lead Gen System with Make.com & OpenAI",
    "ai-personal-life": "AI-Powered Longevity: Using LLMs for Personalized Health Data"
}

def generate_post(cat, topic):
    content = f"""{topic}

The gap between 'using AI' and 'mastering AI' is widening every single day.

Many professionals are still stuck in the loop of basic prompting and generic outputs.
The real advantage lies in understanding the underlying architecture of how these systems reason.

Mastering this isn't just about speed; it's about accuracy, depth, and the ability to solve complex problems that others find impossible.

Here are 8-12 educational insights to master {topic}:

1. The Architecture of Precision
Focus on the structural hierarchy of your request.
Define the specific boundaries of the output before the content itself.

2. Contextual Anchoring
Never start from a blank slate.
Provide at least three reference points to ground the AI's reasoning process.

3. The Iteration Loop
Treat the first output as a draft, not a final product.
Use specific feedback loops to refine technical accuracy.

4. Bias Mitigation
Identify potential hallucination zones early.
Cross-reference AI outputs with verified data sources.

5. Efficiency Scaling
Automate the repetitive parts of your analysis.
Build templates that work across different models and use cases.

6. Strategic Synthesis
Don't just collect data; ask the AI to find patterns across disparate sources.
This turns raw information into actionable strategy.

7. The Human-AI Interface
The AI is your partner, not your replacement.
Maintain high-level oversight on all final strategic decisions.

8. Future-Proofing
Stay updated on the latest model updates and API changes.
The tool you use today will be different by next month.

Key Takeaway: Mastery of {topic} is about shifting from a 'user' mindset to an 'architect' mindset.

How are you integrating this specific approach into your daily work today?

If you found this useful and want more AI resources, tutorials, prompts, workflows, and tools, join ByteBuilders, my daily AI newsletter with 100K+ subscribers.

https://bytebuilders.beehiiv.com/subscribe

Follow ByteBuilders"""
    return content

def generate_image_guideline(cat, topic):
    guideline = f"""Title: {topic}
Subtitle: A Masterclass by ByteBuilders
Theme: Editorial Minimalist
Layout: Card Grid
Header: {topic} Mastery
Card Structure: 8 Rounded Cards with Thin Gray Borders
Typography: Sans Serif, Premium
Colors: White background, Blue #2563EB accents, Dark Gray #374151 text
Icons: Minimal outline icons for each card
Branding placement: 'Follow ByteBuilders' integrated into the middle right margin
Visual elements: White textured paper background, blue numbered circles
What to avoid: Stock people, clutter, heavy gradients, multiple fonts
Goal: High save-rate educational infographic"""
    return guideline

for cat in categories:
    path = f"categories/{cat}/post1"
    os.makedirs(path, exist_ok=True)
    
    with open(f"{path}/content.txt", "w") as f:
        f.write(generate_post(cat, topics[cat]))
        
    with open(f"{path}/image guideline.txt", "w") as f:
        f.write(generate_image_guideline(cat, topics[cat]))

print("Files generated successfully.")
