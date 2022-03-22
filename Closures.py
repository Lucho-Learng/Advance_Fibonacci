# Buenas * 2 -> BuenasBuenasBuenas
# Lucho * 7  -> LuchoLuchoLuchoLuchoLuchoLuchoLucho


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo texto"
        return string * n
    return repeater


def run():
    repeat_2 = make_repeater_of(2)
    print(repeat_2("Buenas"))
    repeat_7 = make_repeater_of(7)
    print(repeat_7("Lucho"))


if __name__ == "__main__":
    run()
