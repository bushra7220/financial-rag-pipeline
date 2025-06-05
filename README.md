# 🧠 POC 1: Financial RAG Pipeline with Streamlit UI

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using `LangChain`, `OpenAI`, and `Streamlit` to extract **summaries, insights, and analytics** from financial PDF documents.

---

## 🔍 Use Case

> "You have some financial data related PDF documents. You need to get document summaries, insights, and analytics from the documents using LLMs."

---

## ✅ Features

- Loads a **financial PDF** via code (no user upload)
- Splits and indexes documents using FAISS
- Uses **LangChain Retrieval Chain** with `create_stuff_documents_chain`
- **Custom PromptTemplate** for financial analysis
- Clean **modular framework** design
- Interactive **Streamlit UI**

---

## 🗂️ Project Structure

├── app/
│ ├── init.py
│ ├── ui.py # Streamlit interface logic
|
│── main.py # Entry point
|
|── data/
│ └── financial_statement_data.pdf # PDF loaded by code
|
|── chains/
│ └── qa_retriever.py
|
|── config/
│ └── config.py
|
|── loaders
│ └── document_loader.py
|
|── utils/
│ └── template_prompt.py
| └── text_splitter.py
| └── vectorestore.py
|
├── .env
├── requirements.txt
└── README.md


## 🧠 Example Questions

- Summarize the key income and expense trends from the financial statement.
- Provide an overview of the monthly cash balance changes.
- What are the major expense categories impacting the cash flow?
- Identify months with the highest income and explain potential reasons.
- Highlight any anomalies or unusual transactions in the data.
- Calculate total revenue and total expenses for the year.
- Analyze how liabilities have changed over the period.
- Suggest financial strategies based on the document insights.


## ⚙️ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


## ⚙️ Run Streamlit App
streamlit run main.py
