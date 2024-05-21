
How to test a file and directory?
Test files should be named test_<something>.py or <something>_test.py.
Test methods and functions should be named test_<something>.
Test classes should be named Test<Something>.

What are test outcomes and flags that could be used?
The possible outcomes of a test function include: PASSED (.), FAILED (F), SKIPPED (s), XFAIL (x), XPASS (X), and ERROR (E).
The -v or --verbose command-line flag is used to reveal more verbose output.
The --tb=no command-line flag is used to to turn off tracebacks.