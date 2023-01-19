import pytest 
def oper(a, b):
    return a/b
"-------------------------------------------1 Вариант ----------------------------------"
# Так писать плохо

@pytest.mark.skip(reason = "Не завершен") # Пропускает эту тест-функцию
def test_oper():

    assert oper(10, 5)==2
    assert oper(20, 4)==5
    assert oper(12, 2)==6
    assert oper(14, 7)==2

"--------------------------------------------- 2 Вариант --------------------------------"
#так тоже плохo

def test_oper1():
    assert oper(10, 5)==2

def test_oper1():
    assert oper(20, 4)==5

def test_oper1():
    assert oper(12, 2)==6


def test_oper1():
    assert oper(14, 7)==2

"------------------------------------------ 3 Вариант --------------------------------"



@pytest.mark.parametrize("num1, num2, result", [(10, 5, 2), (20, 4, 5), (12, 2, 6), (14, 7, 2)])
def test_oper2(num1, num2, result):
    assert oper(num1, num2) == result

"---------------------------- Обработка исключений ---------------------------"
#Плохой способ
def test_oper_zero():
    with pytest.raises(ZeroDivisionError):
   
        oper(10/0)

def test_oper_str():
    with pytest.raises(TypeError):
        oper(10/"str")


# Хороший способ
@pytest.mark.parametrize("a, b, error", [(10, "str", TypeError), (10, 0, ZeroDivisionError)])
def test_oper_error(a, b, error):

    with pytest.raises(error):
        oper(a, b)