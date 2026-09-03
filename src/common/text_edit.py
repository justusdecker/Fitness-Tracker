def rusaac(text: str):
    """
    Replace underscore -> space, and apply capitalize
    """
    return text.replace('_',' ').capitalize()

def rsadc(text:str):
    """
    Converts rusaac strings back to database-compatible
    """
    return text.replace(' ','_').lower()