unit_testing_sample.py file for intitial tests

## resources

CS50 - Harvard 2024

https://www.youtube.com/watch?v=tIrcxwLqzjQ&t=24s
https://www.youtube.com/watch?v=0euvEdPwQnQ

https://docs.pytest.org/en/8.2.x/getting-started.html#create-your-first-test


notes

1. You could automate tests by using a list of different values.
2. You could have more than one file for different types of tests
3. You could put all your tests in one folder and run the whole folder.
4. pytest and other libraries standardize capturing the exceptions and give the standard output - they add the try, except, prints for you
5. The essence of testing is to focus only on the inputs and outputs.
6. A function needs a "return" value - all functions that are tested need an input and output.
7. Use f strings as best practice
8. You coudl create a folder called test where all test files are located, but you need python to treat it as a package.
Therefore it needs a file called   __init__.py
9. 