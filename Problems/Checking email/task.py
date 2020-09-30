def check_email(string: str):
    if " " in string or "@" not in string or \
            string.find("@") > string.rfind('.') or \
            string.find("@") == string.rfind('.') -1:
        return False
    else:
        return True
