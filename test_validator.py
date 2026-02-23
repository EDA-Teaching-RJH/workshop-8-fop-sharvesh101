from validator import is_valid_email

def test_valid_emails():
    try:    
        assert is_valid_email("student1@kent.ac.uk") == True
        assert is_valid_email("doctor@nhs.net") == True
    except AssertionError:
        print("Waring: A Sneaky email bypassed the REGEX!")

def test_invalid_emails():
    assert is_valid_email("hello@world") == False
    assert is_valid_email("fake@kent.ac.uk.com") == False
    assert is_valid_email("no_at_symbol@ac.uk") == False

    try:
        assert is_valid_email("sneaky@@kent.ec.uk") == False
    except AssertionError:
        print("Waring: A Sneaky email bypassed the REGEX!!")

test_valid_emails()
test_invalid_emails()
print("Done!!!")
