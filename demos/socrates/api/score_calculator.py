from typing import List, Dict, Any, Tuple

def calculate_truth_score(sources: List[Dict[str, Any]]) -> Tuple[int, List[Dict[str, Any]]]:
    """Calculates weighted truth score from sources."""
    if not sources:
        return 0, []
        
    total_weight = sum(source["sourceTrustLevel"] for source in sources)
    weighted_score = sum(
        source["sourceAlignmentScore"] * source["sourceTrustLevel"]
        for source in sources
    )
    
    truth_score = round(weighted_score / total_weight) if total_weight > 0 else 0
    return max(-100, min(100, truth_score)), sources
