"""Problem 49"""


def solver():
    """Prime Permutations"""

    def all_prime_combinations(combinations, digits, remaining_digits):
        """function to find all the combinations of a given number"""
        if len(remaining_digits) == 0:
            if int(digits) in all_primes and int(digits) not in combinations:
                combinations.append(int(digits))
            return
        for index, x in enumerate(remaining_digits):
            if digits == "" and x == "0":
                continue
            all_prime_combinations(
                combinations,
                digits + remaining_digits[index],
                remaining_digits[:index] + remaining_digits[index + 1 :],
            )

    def is_property(combinations):
        """return if the property is satisfied or not"""
        for index, x in enumerate(combinations):
            for y in combinations[index + 1 :]:
                dif = y - x
                if y + dif in combinations:
                    return str(x) + str(y) + str(y + dif)
        return ""

    all_primes = [
        x
        for x in range(1489, 9999)
        if all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    ]
    for term in all_primes:
        combinations = []
        all_prime_combinations(combinations, "", str(term))
        combinations = sorted(combinations)
        if len(combinations) >= 3 and is_property(combinations):
            return is_property(combinations)


if __name__ == "__main__":
    print(solver())
