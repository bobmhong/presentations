**Objective**  
Create a Python RESTful API that evaluates claims using the **Socratic method**, returning a `truthScore` and a list of `decisionFactors` detailing sources, trust levels, and alignment with the claim.  

---  
### **Requirements**  

1. **Endpoint & Input**  
   - **POST /verify**  
     - **Input**: JSON payload with `claim` (string, max 1000 characters).  
     - **Validation**: Reject overlength claims with HTTP 400.  

2. **Output**:  
   ```json  
   {  
     "truthScore": integer (-100 to 100),  
     "decisionFactors": [  
       {  
         "sourceName": string,  
         "sourceURL": string,  
         "sourceDate": string (ISO 8601),  
         "sourceTrustLevel": integer (1-5),  
         "sourceAlignmentScore": integer (-100 to 100)  
       },  
       ...  
     ]  
   }  
   ```  

3. **Socratic Analysis Workflow**  
   - Decompose the claim into critical sub-questions (e.g., "What primary sources exist?").  
   - Gather evidence from integrated APIs/databases (e.g., Google Fact Check Tools, Snopes, PubMed).  
   - For **each source**:  
     - **sourceName**: Name of the source (e.g., "NASA", "Reuters").  
     - **sourceURL**: Link to the source material.  
     - **sourceDate**: Publication date (prioritize recent data).  
     - **sourceTrustLevel**:  
       - `1`: Low credibility (e.g., unverified blog).  
       - `3`: Neutral (e.g., Wikipedia).  
       - `5`: High credibility (e.g., peer-reviewed journal).  
     - **sourceAlignmentScore**:  
       - `-100`: Source directly refutes the claim.  
       - `100`: Source fully corroborates the claim.  

4. **Scoring Logic**  
   - `truthScore` is a weighted average of `(sourceAlignmentScore * sourceTrustLevel)` across all sources.  
   - Normalize the final score to [-100, 100].  
   - If no sources found, return `truthScore: 0` and empty `decisionFactors`.  

5. **Example Request/Response**  
   - **Request**:  
     ```json  
     { "claim": "Vaccines cause autism." }  
     ```  
   - **Response**:  
     ```json  
     {  
       "truthScore": -95,  
       "decisionFactors": [  
         {  
           "sourceName": "CDC",  
           "sourceURL": "https://www.cdc.gov/vaccinesafety/concerns/autism.html",  
           "sourceDate": "2023-04-15",  
           "sourceTrustLevel": 5,  
           "sourceAlignmentScore": -100  
         },  
         {  
           "sourceName": "The Lancet (Retracted Study)",  
           "sourceURL": "https://example.com/retracted-study",  
           "sourceDate": "1998-02-28",  
           "sourceTrustLevel": 1,  
           "sourceAlignmentScore": 100  
         }  
       ]  
     }  
     ```  

6. **Error Handling**  
   - Return HTTP 503 if external fact-check APIs fail.  
   - Log incomplete source data (e.g., missing `sourceURL`).  

---  
### **Technical Implementation Notes**  

1. **Integration**  
   - Use `aiohttp` for async API calls to fact-checking services.  
   - Validate `sourceDate` with Python’s `datetime` module.  

2. **Modules to Include**  
   - `claim_processor.py`: Decomposes claims into Socratic questions.  
   - `source_scraper.py`: Fetches and normalizes source data.  
   - `score_calculator.py`: Computes `truthScore` and `sourceAlignmentScore`.  

3. **Testing**  
   - Validate scoring logic with mocked sources (e.g., 5 highly trusted anti-claim sources → `truthScore` ≈ -100).  
   - Test edge cases (e.g., conflicting high-trust sources).  

---  
**Deliverables**  
- API code (FastAPI/Flask), Dockerfile, requirements.txt.  
- Documentation explaining scoring weights and Socratic decomposition.  
- OpenAPI schema with `decisionFactors` definitions.  

This prompt ensures transparency in fact-checking by exposing sourced evidence and its impact on the verdict.