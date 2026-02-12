# pyright: reportMissingImports=false



from crewai import Task

def situation_task(agent, user_input):
    return Task(
        description=f"""
        Analyze the following sentence and extract:
        - Available time
        - Energy level
        - User intent or goal

        Sentence:
        {user_input}
        """,
        expected_output="Structured understanding of the situation",
        agent=agent
    )

def constraint_task(agent, situation_output):
    return Task(
        description=f"""
        Based on the situation below, identify realistic constraints.
        Decide what should be avoided.

        Situation:
        {situation_output}
        """,
        expected_output="List of constraints and limits",
        agent=agent
    )

def plan_task(agent, situation_output, constraint_output):
    return Task(
        description=f"""
        Create a small, realistic micro-plan that fits the situation and constraints.
        The plan should:
        - Fit within the time limit
        - Match energy level
        - Be immediately actionable
        STRICT RULE:
        - The total time MUST NOT exceed available time.
        - Explicitly ensure total time ≤ available time

        Situation:
        {situation_output}

        Constraints:
        {constraint_output}
        """,
        expected_output="A short micro-plan with time blocks",
        agent=agent
    )

def validation_task(agent, plan_output):
    return Task(
        description=f"""
        You are a strict plan validator.

        Carefully review the micro-plan.

        1. Calculate total time of all time blocks.
        2. If total time exceeds available time:
           - Reduce, merge, or adjust blocks.
        3. Ensure TOTAL time is LESS THAN OR EQUAL to available time.
        4. Do NOT add suggestions.
        5. Do NOT explain.
        6. Do NOT add commentary.
        7. Return ONLY the corrected final explained micro-plan.

        IMPORTANT:
        Output only the final plan with time blocks.

        Plan:
        {plan_output}
        """,
        expected_output="Corrected micro-plan only",
        agent=agent
    )


def explanation_task(agent, situation_output, plan_output):
    return Task(
        description=f"""
        Explain why this plan fits the user's situation.
        Keep it short and reassuring.

        Situation:
        {situation_output}

        Plan:
        {plan_output}
        """,
        expected_output="Clear explanation",
        agent=agent
    )
