def test_analyze_HDL_normal():
	from blood_test import analyze_HDL
	result_1 = analyze_HDL(65)
	assert result_1 == "Normal"
    

def test_analyze_HDL_borderlinelow():
    from blood_test import analyze_HDL
    result_1 = analyze_HDL(50)
    assert result_1 == "Borderline Low"

def test_analyze_HDL_low():
    from blood_test import analyze_HDL
    result_1 = analyze_HDL(20)
    assert result_1 == "Low"

