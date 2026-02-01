from langdetect import detect

def detect_language(t):
    try: return detect(t)
    except: return 'unknown'
