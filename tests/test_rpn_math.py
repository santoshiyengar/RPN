from rpn_math import RPNMath

#Check percentage values for different data sets
def test_rpn_math_percentage():
    assert int(RPNMath.percentage(300)) == 3
    assert int(RPNMath.percentage(2)) == 0

#Check number's validity for different data sets
def test_rpn_math_is_valid_number():
    assert RPNMath.is_valid_number("2") ==True
    assert RPNMath.is_valid_number("2.3") ==True
    assert RPNMath.is_valid_number("2.3.2") ==False
    assert RPNMath.is_valid_number("2i") ==False