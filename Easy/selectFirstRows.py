import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    n = 3
    return employees.head(n)
