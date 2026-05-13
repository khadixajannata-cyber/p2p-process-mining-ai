\# P2P Process Mining \& Predictive Analytics



\## Project Overview

This repository contains an end-to-end Process Mining and Machine Learning pipeline applied to the BPI Challenge 2019 dataset (1.5M+ SAP ERP event logs). The objective is to identify process inefficiencies in a Procure-to-Pay (P2P) workflow and build a predictive model to flag potential delays.



\## Methodology \& Tech Stack

1\. \*\*Process Discovery (Python/pm4py)\*\*: Extracted and cleaned event logs to reconstruct the actual P2P process flow, isolating the core "happy path" from process deviations.

2\. \*\*Predictive Modeling (scikit-learn)\*\*: Trained a Random Forest classifier on activity sequences to predict late invoice clearances (74.5% Accuracy, 90% Precision on high-risk cases).

3\. \*\*Automated Diagnostic (OpenAI API)\*\*: Implemented an automated reporting script to generate diagnostic summaries based on the identified process bottlenecks.

4\. \*\*Interactive Dashboard (Power BI)\*\*: Developed a visual interface to track process complexity (e.g., Average Steps per Order) and root causes.



\## Dashboard Preview

!\[Power BI Dashboard](dashboard\_view.png)



\## Key Findings

\* \*\*Process Friction\*\*: The average order requires 13.5 steps to complete, compared to the 5-step ideal path, indicating significant rework.

\* \*\*Root Cause\*\*: The model identified 'Record Invoice Receipt' and subsequent modifications as the primary drivers of delay.

\* \*\*Temporal Trends\*\*: Trend analysis revealed a sharp increase in process complexity during Q4, likely tied to year-end closing resource constraints.

