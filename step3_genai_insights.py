"""
GenAI Business Insights Module
------------------------------
Integrates Predictive AI outputs with Large Language Models (LLMs) to automatically
generate executive-level process diagnostic reports and action items.
"""

import os
import json
from openai import OpenAI

API_KEY = ""  
BASE_URL = "https://api.openai.com/v1" 

def generate_executive_report(accuracy, top_bottlenecks):
    """Generates an executive summary using an LLM."""
    

    system_prompt = """
    You are a Senior Process Mining Consultant at a top-tier firm (e.g., McKinsey, Celonis).
    Your task is to translate raw machine learning metrics into a concise, high-impact 
    business report for the Chief Procurement Officer (CPO).
    Tone: Professional, actionable, data-driven, and urgent.
    Language: English.
    Format: Use clear bullet points and bold text for emphasis.
    """
    
    user_prompt = f"""
    Based on our latest Process Mining AI model, we have the following results for the Procure-to-Pay (P2P) process:
    1. Predictive Model Accuracy for delayed orders: {accuracy}%
    2. Top 3 Root Causes for delays (Bottlenecks):
       - {top_bottlenecks[0]}
       - {top_bottlenecks[1]}
       - {top_bottlenecks[2]}
       
    Please generate a short Executive Summary (max 150 words) including:
    - A brief summary of the model's performance.
    - An analysis of the primary bottlenecks.
    - 2 actionable recommendations to reduce delays and save costs.
    """

    print("[INFO] Connecting to GenAI Brain...")
    print("-" * 50)

    if not API_KEY:
        print("[WARNING] No API Key detected. Running in Offline Simulation Mode.")
        print("-" * 50)
        mock_report = f"""
**EXECUTIVE SUMMARY: P2P PROCESS DIAGNOSTIC**

**Model Performance & Reliability:**
Our newly deployed Predictive AI model is currently forecasting order delays with a robust **{accuracy}% accuracy**. This gives us a highly reliable early-warning system to proactively intervene before financial penalties occur.

**Root Cause Analysis:**
The AI has isolated the bottlenecks. The delays are NOT in the purchasing phase, but critically concentrated in the financial back-office. The primary drivers are:
1. **{top_bottlenecks[0]}**
2. **{top_bottlenecks[1]}**
3. **{top_bottlenecks[2]}**

**Actionable Recommendations:**
* **Implement OCR Automation:** Deploy Optical Character Recognition (OCR) to automate the 'Record Invoice Receipt' step, reducing manual data entry errors.
* **Audit Clearance Workflow:** Establish a cross-functional task force to review the 'Clear Invoice' approval thresholds, as this is currently creating a severe backlog.
        """
        return mock_report.strip()


    try:
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] Failed to generate report via API: {e}"

def main():
    print("[INFO] Initializing GenAI Insights Module...")
    
    sprint2_accuracy = 74.5
    sprint2_bottlenecks = [
        "Record Invoice Receipt", 
        "Clear Invoice", 
        "Record Goods Receipt"
    ]
    
    print(f"[INFO] Ingesting ML metrics -> Accuracy: {sprint2_accuracy}%")
    
    report = generate_executive_report(sprint2_accuracy, sprint2_bottlenecks)
    
    print("\n" + "="*50)
    print(" 🤖 AI GENERATED EXECUTIVE REPORT ")
    print("="*50)
    print(report)
    print("="*50)
    print("[SUCCESS] Sprint 3 Completed. Ready for management review.")

if __name__ == "__main__":
    main()