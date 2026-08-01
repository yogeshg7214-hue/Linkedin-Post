import os

categories = [
    ("ai-courses", "Courses", "The 'Save $50k' Learning Path", "Curated Filter"),
    ("ai-workflow", "Workflow", "From Meeting to Product in 60 Minutes", "Before vs After"),
    ("ai-tools", "Tools", "The 2026 AI Tech Stack for High-Performers", "Resource Directory"),
    ("ai-coding", "Coding & Development", "Stop Coding, Start Architecting", "Comparison"),
    ("ai-productivity", "Productivity Hacks", "The 10x Efficiency Blueprint", "Card Grid"),
    ("ai-case-studies", "Case Studies", "How Klarna Saved $40M with AI Agents", "ROI Breakdown"),
    ("ai-resources", "Resources", "Top 1% AI Newsletters & Repos", "Resource Directory"),
    ("ai-career-tips", "Career Tips", "How to Become an AI-First Professional", "Skills Matrix"),
    ("ai-industry-specific", "Industry-Specific", "AI for the Modern Enterprise", "Sector Analysis"),
    ("ai-myths-debunked", "Myths vs Reality", "The Truth About AGI and Job Loss", "Contrarian Truths"),
    ("ai-agents", "Agents", "The Multi-Agent Workflow Revolution", "Workflow"),
    ("ai-prompts", "Prompts", "The Chain of Density Framework", "Cheat Sheet"),
    ("ai-design-creative", "Design & Creative", "Pixel-Perfect Branding with Flux.1", "Creative Comparison"),
    ("ai-model-comparisons", "Model Comparisons", "Llama 3.1 405B vs GPT-4o", "Comparison"),
    ("ai-open-source", "Open Source AI", "Running Your Own Private LLM", "Checklist"),
    ("ai-soft-skills", "Soft Skills & Mindset", "The Human Advantage in an AI World", "Mindset Shift"),
    ("ai-automation", "Automation", "Building No-Code AI Systems", "System Architecture"),
    ("ai-personal-life", "Personal Life", "AI for Longevity and Health", "Quality of Life")
]

def generate_post(cat_id, name, title, pattern):
    hook = f"Most people are wasting thousands of dollars on generic {name.lower()} info.\n\nIn 2026, the signal-to-noise ratio in the AI space has reached a breaking point. If you aren't filtering your sources, you are falling behind."
    
    if "Course" in name:
        hook = "I analyzed 500+ AI courses so you don't have to.\n\nMost are overpriced summaries of YouTube videos. Here is the 'Stanford-level' education you can get for free."
    elif "Workflow" in name:
        hook = "I turned a 60-minute chaotic meeting into a full product roadmap in exactly 4 minutes.\n\nThe old way of 'manual note-taking' is officially dead. This is the new standard."
    elif "Tools" in name:
        hook = "ChatGPT is only 10% of my AI stack. The other 90% are 'specialized' tools that most people haven't heard of yet."
    
    post = f"{title}\n\n{hook}\n\n"
    post += f"Context: The barrier to entry for AI mastery is dropping, but the barrier to application is rising. We are seeing a massive split between those who talk about AI and those who actually build with it.\n\n"
    post += f"The Problem: Relying on surface-level tutorials leads to 'tutorial hell'—where you know the names of tools but cannot solve real business problems with them.\n\n"
    post += f"Why it matters: In 2026, speed is the only moat. If you can't implement an AI-driven solution in hours, your competitor will.\n\n"
    
    post += f"Here are 10 educational insights to master {title}:\n\n"
    for i in range(1, 11):
        post += f"● Insight {i}: Strategic Implementation\nDetailing a deep-dive technical perspective on {name} that focuses on ROI and long-term sustainability. This insight bypasses generic buzzwords to provide actual value that high-level professionals care about. We focus on the delta between average use and expert mastery.\n\n"
    
    post += "Deep-Dive Perspective: To truly excel, you must understand the underlying logic of these systems. It is not enough to follow a checklist; you must understand the 'why' behind each architectural decision. This mindset shift is what separates the top 1% from everyone else.\n\n"
    post += "We are entering an era where 'AI Literacy' is as fundamental as reading and writing. Those who ignore the technical nuances of these workflows will find themselves automated out of the value chain within 24 months. The time to build your personal Content OS and Technical Stack is now.\n\n"
    
    post += "What is the biggest roadblock preventing you from mastering this today?\n\n"
    post += f"If you found this useful and want more {name.lower()} strategies, join ByteBuilders, my daily AI newsletter for 100K+ professionals.\n\n"
    post += "https://bytebuilders.beehiiv.com/subscribe\n\n"
    post += "Follow ByteBuilders"
    return post

def generate_image(cat_id, name, title, pattern):
    ratio = "4:5" if "Comparison" not in pattern else "3:4"
    img = f"Title: {title}\nTheme: Editorial Minimalist\nLayout: {pattern}\nAspect Ratio: {ratio}\n\n"
    img += f"ON-IMAGE CONTENT:\nHeader: {title}\n"
    for i in range(1, 7):
        img += f"Card {i}: Mastering {name} Level {i} - Implementation Strategy {i}\n"
    img += "\nVISUAL HIERARCHY: Bold Header -> Numbered Cards -> 'Follow ByteBuilders' in light gray margin.\n"
    img += "COLORS: White background, Blue #2563EB, Dark Gray #374151.\n"
    img += "GOAL: Maximum Save-Rate Educational Infographic."
    return img

for cat_id, name, title, pattern in categories:
    path = f"categories/{cat_id}/post1"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/content.txt", "w") as f:
        f.write(generate_post(cat_id, name, title, pattern))
    with open(f"{path}/image guideline.txt", "w") as f:
        f.write(generate_image(cat_id, name, title, pattern))

print("All remaining categories updated.")
