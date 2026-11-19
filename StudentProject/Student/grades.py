def calavg(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def calmax(grades):
    if not grades:
        return None
    return max(grades)

def calmin(grades):
    if not grades:
        return None
    return min(grades)