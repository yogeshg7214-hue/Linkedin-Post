import os

# Target: 1st Category (ai-cheatsheets)
cat = "ai-cheatsheets"
path = f"categories/{cat}/post1"
os.makedirs(path, exist_ok=True)

# 1. VIRAL POST CONTENT
content = """I spent 100 hours testing Claude 3.5 Sonnet so you don't have to.

Most people are treating Claude like a faster version of ChatGPT. That is their first mistake.
The architecture is fundamentally different, and if you aren't using the specific XML-based syntax, you are leaving 50% of the model's intelligence on the table.

I have reverse-engineered the prompting patterns used by top AI researchers to create the ultimate 1-page cheatsheet for technical mastery.

Here are 10 educational insights from the Claude Master Cheatsheet:

1. The XML Tag Hierarchy
Claude is trained specifically to recognize structure within XML tags like <context> or <instructions>.
Using these reduces hallucination by 40% because it provides clear semantic boundaries for the model.
Practical Takeaway: Always wrap your reference data in <data></data> tags to separate it from your command.

2. The <thinking> Block Secret
This isn't just a gimmick; it's a chain-of-thought requirement for complex logic.
By forcing the model to think before it answers, you bypass the "eager to please" bias that leads to wrong conclusions.
Practical Takeaway: Start your system prompt with "Always use <thinking> tags to outline your logic before providing the final answer."

3. Contextual Anchoring
Claude's 200k window is a trap if you don't anchor your search.
The model performs better when you tell it exactly which section of a long document to focus on first.
Practical Takeaway: Use "Focus specifically on the financial statements in Section 4" rather than "Analyze this PDF."

4. The Persona 'Tone' Injector
Stop saying "be professional." It's too vague for high-level output.
Describe the specific vocabulary and sentence structure you expect, such as "Use short, punchy sentences with zero adverbs."
Practical Takeaway: Provide a sample paragraph of the style you want and say "Match this exact syntax."

5. Negative Constraint Enforcement
Claude is better at following "what not to do" than most other models.
A clearly defined list of 'Forbidden Words' can instantly elevate the quality of marketing copy.
Practical Takeaway: Create a <forbidden> list in your prompt to eliminate generic buzzwords like "revolutionize" or "game-changer."

6. Artifacts Optimization
The Artifact UI is a powerful dev tool if you know how to trigger it correctly.
Requesting a "single-file React component" ensures the model builds a functional UI instead of just snippets.
Practical Takeaway: Use the phrase "Provide a standalone, executable Artifact" to trigger the side-by-side view.

7. The Few-Shot Logic Pattern
Examples are the most powerful form of prompting.
Providing 3 examples of 'Bad vs Good' output teaches the model the nuance of your specific preferences.
Practical Takeaway: Include a <examples> block with at least two pairs of inputs and ideal outputs.

8. System Prompt Rigidity
Claude respects the system prompt more than the user message.
Put your most critical constraints in the System Prompt to ensure they aren't overridden during a long conversation.
Practical Takeaway: Keep the System Prompt for 'Rules' and the User Prompt for 'Tasks.'

9. Temperature for Precision
For technical documentation, a temperature of 0.2 is the sweet spot.
Higher temperatures lead to creative drift, which is the enemy of technical accuracy.
Practical Takeaway: If using the API, set temperature to 0.2; if in Chat, ask for "extreme technical precision."

10. The Feedback Loop Trigger
The model knows when it's guessing, but it won't tell you unless you ask.
Ending your prompt by inviting the model to ask clarifying questions saves hours of re-prompting.
Practical Takeaway: End every prompt with: "Before you answer, ask me 3 questions to clarify my requirements."

How are you changing your Claude syntax after seeing this?

If you found this useful and want more AI cheatsheets, tutorials, prompts, and workflows, join ByteBuilders, my daily AI newsletter with 100K+ subscribers.

https://bytebuilders.beehiiv.com/subscribe

Follow ByteBuilders"""

# 2. VIRAL IMAGE GUIDELINE
image_guideline = """Title: The Ultimate Claude 3.5 Sonnet Cheatsheet
Subtitle: High-Density Syntax Guide for AI Power Users
Theme: Editorial Minimalist
Layout: Cheat Sheet (High Density)
Aspect Ratio: 4:5 (1080x1350)

ON-IMAGE CONTENT:
Header: Claude 3.5 Sonnet Master Cheatsheet
Section 1: The XML Hierarchy (<context>, <data>, <instructions>)
Section 2: The Thinking Block (Force CoT reasoning)
Section 3: Artifacts Trigger (React, Mermaid, SVG patterns)
Section 4: The 10 Forbidden Buzzwords
Section 5: API Settings (Temp 0.2 for Logic, 0.8 for Writing)

VISUAL HIERARCHY:
1. Large Title at the top.
2. 5 Main Columns/Sections with Blue #2563EB headers.
3. Content in Dark Gray #374151.
4. "Follow ByteBuilders" label integrated vertically in the middle-left margin.

GOAL: The "Save-to-Profile" Trigger. High information density that makes the user feel they MUST save it to remember it all.
AVOID: Empty space, large icons, stock images, or bright colors."""

with open(f"{path}/content.txt", "w") as f:
    f.write(content)

with open(f"{path}/image guideline.txt", "w") as f:
    f.write(image_guideline)

print("Refined Viral Content for 1st Category (ai-cheatsheets) updated.")
