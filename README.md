\# 🚀 P2P Process Mining \& AI Analytics: Discovering \& Predicting Enterprise Inefficiencies



\## 📌 Executive Summary

Multinational enterprises lose millions annually due to supply chain delays and invisible "rework" loops. This project leverages \*\*Process Mining\*\* and \*\*Predictive AI\*\* on a real-world SAP ERP dataset (BPI Challenge 2019, 1.5M+ logs) to not only visualize past operational bottlenecks but also forecast future risks and automate root cause diagnostics using GenAI.



\## 🛠️ Integrated Tech Stack \& Workflow



The project is structured into four distinct sprints, demonstrating full-stack data analytics capability:



1\.  \*\*Sprint 1: ETL \& Process Discovery (Python + Pm4py)\*\*

&#x20;   \* Engineered event logs from raw XES, handling large-scale (1.5M+ rows) enterprise data.

&#x20;   \* Reconstructed the company's "Happy Path" by filtering the chaotic "Spaghetti Process" with frequency-based algorithms.

2\.  \*\*Sprint 2: Predictive AI Model (Scikit-Learn)\*\*

&#x20;   \* Transformed event logs into a structure feature matrix (Bag of Activities).

&#x20;   \* Trained a \*\*Random Forest Classifier\*\* to predict order delays before clearance, achieving \*\*74.5% Accuracy\*\* and \*\*90% Precision\*\* for high-risk cases.

3\.  \*\*Sprint 3: GenAI Executive Diagnostic (OpenAI API Concept)\*\*

&#x20;   \* Developed a dynamic prompt engineering pipeline to ingest ML metrics (Accuracy, Top Bottlenecks).

&#x20;   \* Leveraged LLM to automatically generate a McKinsey-style \*\*Executive Summary\*\* and actionable recommendations for the CPO.

4\.  \*\*Sprint 4: Business Intelligence Dashboard (Power BI)\*\*

&#x20;   \* Deployed an \*\*interactive Dark Mode Dashboard\*\* with custom DAX measures (e.g., Average Steps per Order).

&#x20;   \* Utilized AI-driven visuals (Decomposition Tree) and Trend analysis to isolate the critical bottleneck: \*\*Invoice Clearance workflow concentration in Q4\*\*.



\## 📊 High-End Visualizations \& Business Insights



\### The Executive Dashboard

\*(Visualizing the critical metrics and interactive drill-down capabilities)\*



!\[Process Mining Dashboard](dashboard\_view.png)



\### 💡 Key Business Findings

\* \*\*The Hidden "Rework" Cost:\*\* The average order requires \*\*13.5 steps\*\* to complete, vs a standard "happy path" of just 5 steps. This indicates severe process friction and rework.

\* \*\*The Root Cause:\*\* The AI Key Influencer tree isolated \*\*'Record Invoice Receipt'\*\* and subsequent modifications as the activities driving the highest rework time per order.

\* \*\*The Time Trend:\*\* Inefficiencies are not uniform; delays surge significantly during Q4 (especially late 2018), indicating severe resource bottlenecks in the Accounts Payable department during year-end closing.



\## ⚙️ Future Enhancements

\* Deploying a live stream connector to the SAP ERP system.

\* Upgrading the predictive model with sequence-aware neural networks (LSTMs) for higher accuracy.



\---

\*Developed as a demonstration of End-to-End Advanced Analytics.\*

