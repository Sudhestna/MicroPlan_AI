from crewai import Agent,LLM
from langchain_ollama import ChatOllama

llm = LLM(
    model="ollama/llama3.2",
    temperature=0.4
)

situation_agent = Agent(
    role="Situation Understanding Agent",
    goal="Understand the user's current situation from one sentence",
    backstory="Expert at interpreting time, energy, mood, and intent from short inputs.",
    llm=llm,
    verbose=True
)

constraint_agent = Agent(
    role="Constraint Reasoning Agent",
    goal="Identify realistic constraints like time, energy, and effort limits",
    backstory="Specialist in preventing unrealistic planning and overcommitment.",
    llm=llm,
    verbose=True
)

plan_agent = Agent(
    role="Micro-Plan Generator Agent",
    goal="Generate a short, realistic, and actionable micro-plan",
    backstory="Expert in breaking goals into small executable steps.",
    llm=llm,
    verbose=True
)

validation_agent = Agent(
    role="Plan Validation Agent",
    goal="Ensure the plan fits constraints and is realistic",
    backstory="Ensures plans are practical and not overwhelming.",
    llm=llm,
    verbose=True
)

explanation_agent = Agent(
    role="Explanation Agent",
    goal="Explain why the micro-plan fits the situation",
    backstory="Builds user trust through clear reasoning.",
    llm=llm,
    verbose=True
)
