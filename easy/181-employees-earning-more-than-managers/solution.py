import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Unir la tabla consigo misma
    merged = employee.merge(
        employee,
        left_on='managerId',
        right_on='id',
        suffixes=('_emp', '_mgr')
    )
    
    # Filtrar empleados con salario mayor que su gerente
    result = merged[merged['salary_emp'] > merged['salary_mgr']]
    
    # Seleccionar solo el nombre del empleado y renombrar columna
    result = result[['name_emp']].rename(columns={'name_emp': 'Employee'})
    
    return result