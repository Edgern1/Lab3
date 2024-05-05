import employee_info as e
def test_employee_by_age_range():
	assert e.get_employees_by_age_range(24,26)==[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]
def test_calculate_average_salary():
	assert round(e.calculate_average_salary(),2)==round(60166.66666666666,2)
def test_get_employees_by_dept():
	assert e.get_employees_by_dept("Engineering")==[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
