import os
from dotenv import load_dotenv

load_dotenv()

def analyze_log_with_ai(log):
    api_key = os.getenv("OPENAI_API_KEY")

    # If no API key → fallback (VERY IMPORTANT)
    if not api_key or api_key == "your_actual_api_key_here":
        return f"""
        Detected issue in log: {log}

        Possible issue:
        - System error or failure detected

        Suggested fix:
        - Check logs carefully
        - Restart service
        - Verify database or network connection
        """

    # If API key exists → use OpenAI
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        prompt = f"""
        Analyze the following system log:

        1. Identify the issue
        2. Explain in simple terms
        3. Suggest a fix

        Log:
        {log}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"