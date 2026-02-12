def test_it(function, func_input, supervised_output):
    """
    Function that iterates through the function and checks if it yields the desired result.
    :param function: Function to test
    :param func_input: Any data that function accepts
    :param supervised_output: Data that function usually returns
    :return: True is all tests has passed, false otherwise
    """

    input_output = zip(func_input, supervised_output)
    results = []

    for test in input_output:
        if function(test[0]) == test[1]:
            results.append(True)
            print(f"✅ the function {function.__name__} yields the right answer from {test[0]} : {test[1]}")
        else:
            results.append(False)
            print(f"🚫 function {function.__name__} yields the wrong answer from {test[0]} : {function(test[0])} , expected {test[1]}")
    if all(results):
        print(f"{function.__name__} yields the right answers")
        return True
    else:
        print(f"{function.__name__} yields the wrong answers")