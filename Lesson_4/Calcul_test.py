from Calcul import Calculator
import pytest

#calculator = Calculator()

@pytest.mark.positive_test
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum (4, 5)
    assert res == 9
#@pytest.mark.xfail(strict=True)    
def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum (-4, -5)
    assert res == -9    

def test_mult_negative_nums():
    calculator = Calculator()
    res = calculator.mult (-4, -5)
    assert res == 20   

#@pytest.mark.positive_test 
@pytest.mark.parametrize( 'num1, num2, result', [
    (4, 5, 0.8), 
    (-2, 2, -1), 
    (2,4,0.5)
    ] 
    )
def test_div_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.div (num1, num2)
    assert res == result

def test_div_zero_nums():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
    
        res = calculator.div (4, 0)

@pytest.mark.parametrize( 'nums, result', [([1,3,5,7,9],5), ([-2, 2, 4, 0], 1)] )
def test_avg_nums(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result


    # assert res == None

 #res = calculator.sum (4, 5)
 #assert res == 9

# res = calculator.sum (-4, -5)
# assert res == -9

# res = calculator.sum (4, -5)
# assert res == -1

# res = calculator.sum (1.12, 2.89)
# res = round(res, 2)

# assert res == 4.01

# res = calculator.sum (0, 5)
# assert res == 5

# res = calculator.div (4, 5)
# assert res == 0.8

# n=[]
# res = calculator.avg(n)
# assert res == 0


# n=[3,6,9,12,15]
# res = calculator.avg(n)
# assert res == 9


# res = calculator.div (4, 0)
# assert res == None