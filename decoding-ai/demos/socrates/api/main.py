from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
from .claim_processor import decompose_claim
from .source_scraper import gather_sources
from .score_calculator import calculate_truth_score

app = FastAPI(title="Socratic Truth Evaluator")

class Claim(BaseModel):
    claim: str

class DecisionFactor(BaseModel):
    sourceName: str
    sourceURL: str
    sourceDate: str
    sourceTrustLevel: int
    sourceAlignmentScore: int

class VerificationResponse(BaseModel):
    truthScore: int
    decisionFactors: List[DecisionFactor]

@app.post("/verify", response_model=VerificationResponse)
async def verify_claim(claim: Claim):
    try:
        questions = decompose_claim(claim.claim)
        sources = await gather_sources(questions)
        truth_score, factors = calculate_truth_score(sources)
        
        return VerificationResponse(
            truthScore=truth_score,
            decisionFactors=factors
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail="Service temporarily unavailable")
