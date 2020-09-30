def what_to_do(instructions: str):
    if instructions.startswith("Simon says") or \
            instructions.endswith("Simon says"):
        pos = instructions.find("Simon says")
        if pos == 0:
            return instructions.replace("Simon says", "I")
        else:
            return "I " + instructions[:pos - 1]
    else:
        return "I won't do it!"
