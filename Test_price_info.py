import price_info as p
def test_total_cost():
	assert p.total_cost_shopping()==46.75
def test_price():
	assert p.cost_of_fruits("apple",10)==12.0
