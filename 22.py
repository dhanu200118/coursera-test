def test_func(string, sub_str):
    if (string.find(sub_str) == -1):
        print('false')
    else:
        print("True")
string =input('enter first String:')
sub_str =input('enter second string:')
test_func(string, sub_str)
