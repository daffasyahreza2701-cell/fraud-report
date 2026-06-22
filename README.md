# fraud-report
synthetic financial data credit card fraud transaction report using sources from kaggle
The objective is to explore fraud trends across customer demographics, payment methods, purchase categories, transaction locations, and transaction timing to simulate the workflow of a fraud analyst.

Tools used:
1. VScode
2. Python (Pandas)
3. Bash
4. Microsoft Excel
5. Microsoft Word
6. ChatGPT
   
Project Workflow:
The script is created using VScode as the code editor
the synthetic financial data previously stored in .csv gets read using python by utilizing the pandas library
ChatGPT is used to create the framework, helping to guide the scripting process, and refining the questions used in analysis.
The scripting process also gets documented on a google docs later then the data is used to create the mock report
After initial data cleaning process the whole process gets mainly documented on the script fraud_analysis.py
Then intiallizng_df.py is a script meant for calling the data without having to do the whole process
fraud_excel_1.py is a script for exporting the findings into a .xlsx file for further use
Data visualization is created by using the excel files
The report was made using google docs and edited with microsoft word and finallized into a pdf

Repository structure:
fraud_analysis.py – Main exploratory data analysis script.
initializing_df.py – Loads and prepares the dataset for analysis.
fraud_excel_1.py – Exports analysis outputs to an Excel workbook.
Synthetic_fraud_report.pdf – Final analytical report.
synthetic_financial_data.csv – Dataset used for the project.

Key Questions Explored:
How common are fraudulent transactions?
Which card types are used most frequently?
Which card types generate the highest transaction value?
Which card type has the highest fraud rate?
Are fraudulent transactions larger than legitimate transactions?
Which customer recorded the most fraudulent transactions?
Which cities exhibit the highest fraud rates?
Which purchase categories experience the most fraud?
Which age groups appear most frequently in fraudulent transactions?

Key Findings:
The dataset contained approximately equal proportions of fraudulent and legitimate transactions.
MasterCard recorded the highest fraud rate among card types.
Grocery purchases exhibited both the highest fraud count and fraud rate.
City-6 recorded the highest fraud rate, while City-9 recorded the lowest.
Fraudulent transactions had a slightly higher average transaction amount than legitimate transactions.
A small number of customers accounted for repeated fraudulent transactions.
Report

A complete summary of the methodology, findings, visualizations, and recommendations is available in Synthetic_Fraud_Report.pdf.

Acknowledgements

Dataset: Synthetic Financial Transaction Dataset by ISABBAGIN on Kaggle.

AI assistance (ChatGPT) was used to help organize the project structure, refine analytical questions, and improve documentation. All code, analysis, interpretation, and project validation were reviewed and executed by the project author.
