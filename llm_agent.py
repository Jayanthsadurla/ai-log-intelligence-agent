import os
from dotenv import load_dotenv

load_dotenv()

def analyze_log_with_ai(log):
    log = log[:500]  # limit size

    api_key = os.getenv("OPENAI_API_KEY")

    # Fallback if no API key
    if not api_key or api_key == "your_actual_api_key_here":
        return f"""
Detected issue in log: {log}

Possible issue:
- {"Database issue" if "database" in log.lower() else "System error detected"}

Suggested fix:
- Restart service
- Check logs carefully
- Verify network/database connection
"""

    try:
        from openai import OpenAI

        client = OpenAI(
            api_key=api_key,
            timeout=10
        )

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
