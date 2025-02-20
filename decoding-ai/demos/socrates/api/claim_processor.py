from typing import List

def decompose_claim(claim: str) -> List[str]:
    """Decomposes a claim into Socratic questions."""
    base_questions = [
        f"What primary sources exist about '{claim}'?",
        f"What evidence supports '{claim}'?",
        f"What evidence contradicts '{claim}'?",
        f"What are the credentials of sources discussing '{claim}'?",
        f"When was the most recent research on '{claim}' conducted?"
    ]
    
    return base_questions
