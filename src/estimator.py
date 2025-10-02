# src/estimator.py 

import math

ATTACKER_PROFILES = {
    "Online throttled: (1000/day)": 1000 / 86400.0,
    "Single high-end GPU (est)": 1e11,
    "GPU cluster": 1e12, 

}

def secs_to_human(seconds: float) -> str: 
    if seconds < 1:
        return f"{seconds:.3f} seconds"
    units = [("years", 365*24*3600), ("days", 24*3600), ("hours", 3600), ("minutes", 60), ("seconds", 1)]
    for name, val in units:
        if seconds >= val:
            return f"{seconds/val:.2f} {name}"
    return f"{seconds:.2f} seconds"

def estimate_crack_time(guesses: float, extra_profiles: dict = None) -> dict:
    profiles = ATTACKER_PROFILES.copy()
    if extra_profiles:
        profiles.update(extra_profiles)
    
    result = {}
    for name, hps in profiles.items():
        attempts_per_second = hps
        seconds = guesses / attempts_per_second
        result[name] = {"seconds": seconds, "display": secs_to_human(seconds)}
    return result