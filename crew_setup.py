# pyright: reportMissingImports=false


from crewai import Crew
from agents import (
    situation_agent,
    constraint_agent,
    plan_agent,
    validation_agent,
    explanation_agent
)
from tasks import (
    situation_task,
    constraint_task,
    plan_task,
    validation_task,
    explanation_task
)

def run_microplan(user_input):
    t1 = situation_task(situation_agent, user_input)
    t2 = constraint_task(constraint_agent, "{{output of situation task}}")
    t3 = plan_task(plan_agent, "{{output of situation task}}", "{{output of constraint task}}")
    t4 = validation_task(validation_agent, "{{output of plan task}}")
    t5 = explanation_task(explanation_agent, "{{output of situation task}}", "{{output of plan task}}")

    crew = Crew(
        agents=[
            situation_agent,
            constraint_agent,
            plan_agent,
            validation_agent,
            explanation_agent
        ],
        tasks=[t1, t2, t3, t4, t5],
        verbose=True
    )

    crew.kickoff()
    return {
    "plan": t4.output.raw,
    "explanation": t5.output.raw
}