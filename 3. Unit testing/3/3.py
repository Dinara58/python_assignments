import re

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+?7|8)\s?(\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

def test_is_correct_mobile_phone_number_ru():
    test_cases = {
        "+7 937 587-47-76": True,
        "8(920)4321587": True,
        "7 900 7654321": False,
        "+7 995 654321": False,
        "8 800 55543587": False
    }

    for test_case, expected_result in test_cases.items():
        result = is_correct_mobile_phone_number_ru(test_case)
        if result == expected_result:
            continue
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    test_is_correct_mobile_phone_number_ru()
