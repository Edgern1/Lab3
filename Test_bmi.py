import Lab2.bmi as bmi

def test_normal_weight():
	assert 0==bmi.calculate_bmi(1,18.6)
def test_over_weight():
	assert 1==bmi.calculate_bmi(1,100)
def test_under_weight():
	assert -1==bmi.calculate_bmi(1,18.4)
