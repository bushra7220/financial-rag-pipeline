from langchain.prompts import PromptTemplate


def get_financial_prompt():
    return PromptTemplate(
        input_variables=["context", "input"],
        template="""
        You are a financial analyst AI. Given the following financial document context, provide detailed summaries, insights, and analytics. 

        Context:
        {context}

        Question:
        {input}

        Answer in a structured and concise way:
        """,
    )
