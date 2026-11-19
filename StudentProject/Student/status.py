def calstatus(average_grades):
    if average_grades is None:
        return "Unknown Entry"
    return "Acceptable" if average_grades >= 10 else "Rejected"