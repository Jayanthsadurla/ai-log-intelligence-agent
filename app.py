from fastapi import FastAPI
from pydantic import BaseModel

from anomaly_detector import detect_anomaly
from llm_agent import analyze_log_with_ai
from log_store import save_log, get_logs  # ✅ NEW

app = FastAPI()

# Input schema
class LogInput(BaseModel):
    log: str

# Home route
@app.get("/")
def home():
    return {"message": "AI Log Agent Running"}

# Main API
@app.post("/analyze")
def analyze_log(data: LogInput):
    is_anomaly = detect_anomaly(data.log)

    if not is_anomaly:
        result = {
            "status": "healthy",
            "message": "No issue detected"
        }
        save_log(data.log, result)  # ✅ store log
        return result

    # Try AI safely
    try:
        ai_result = analyze_log_with_ai(data.log)
    except Exception as e:
        ai_result = f"AI failed: {str(e)}"

    result = {
        "status": "issue_detected",
        "analysis": ai_result
    }

    save_log(data.log, result)  # ✅ store log

    return result


# ✅ NEW API: fetch all logs
@app.get("/logs")
def fetch_logs():
    return get_logs()