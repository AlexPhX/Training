try:
    num = "1"
    number = int(num)
    raise AttributeError("It's AttributeError!")
    assert 1==1 , "0!=1"
except ValueError:
    print("Value Error")
except AssertionError as err:
    print(f"Assertion Error: {err}")
except AttributeError as err:
    print(f"Raise: {err.args[0]}")
else:
    print(f"Number is: {number}")
finally:
    print("It's finally happen!")
