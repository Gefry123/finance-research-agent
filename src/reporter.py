from dotenv import load_dotenv
import os
import anthropic


load_dotenv()
client = anthropic.Anthropic()


def generate_report(ticker: str,  signals: list, news: list):

    prompt = f"""
    You are a financial analyst. Given stock data, technical indicators, and recent news, 
    produce a structured investment report with:

    - Summary
    - Technical analysis (RSI, moving averages, momentum)
    - News sentiment
    - Risk factors
    - Buy / Hold / Sell recommendation with reasoning
    Be concise and data-driven. Avoid speculation.

    ## Stock: {ticker}

    ### Recent News
    {news}

    ###Signals
    {signals}

"""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
    )
    return message.content[0].text
