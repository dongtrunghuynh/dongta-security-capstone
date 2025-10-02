from zxcvbn import zxcvbn

def analyze_password(password: str, user_inputs: list[str] = None) -> dict:
    """Returns the raw values """
    
    if user_inputs is None:
        user_inputs = []
    result = zxcvbn(password, user_inputs)
    
    return {
        "score": result["score"],
        "guesses": result["guesses"],
        "crack_times_seconds": result["crack_times_seconds"],
        "crack_times_display": result["crack_times_display"],
        "feedback": result.get("feedback", {}),
        "sequence": result.get("sequence", []),
    }
    