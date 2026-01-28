import random
from datetime import datetime

class CowsAndBulls:
    def __init__(self) -> None:
        self.random_tiv = None
        self.user_tiv = None
        self.cows = 0
        self.bulls = 0
        self.porcer = 1
        self.time_skizb = None
        self.time_verj = None

    def random_number(self) -> None:
        while True:
            self.random_tiv = str(random.randint(1000, 9999))
            if len(set(self.random_tiv)) == 4:
                break
        print(f"Բացել եմ հեշտ հաղթելու համար {self.random_tiv}")  # debug

    def user(self) -> None:
        while True:
            self.user_tiv = input("Տուր ինձ քառանիշ թիվ - ")
            if self.user_tiv.isdigit() and len(self.user_tiv) == 4 and len(set(self.user_tiv)) == 4:
                break

    def hashvich_c_b(self) -> None:
        self.cows = 0
        self.bulls = 0
        for i in range(4):
            if self.user_tiv[i] == self.random_tiv[i]:
                self.cows += 1
            elif self.user_tiv[i] in self.random_tiv:
                self.bulls += 1

    def play(self) -> tuple:
        self.time_skizb = datetime.now()
        self.random_number()

        while True:
            self.user()
            self.hashvich_c_b()
            if self.cows == 4:
                print(f"You Win! Դուք փորձեցիք {self.porcer} անգամ")
                break
            print(f"cows = {self.cows}\nbulls = {self.bulls}")
            self.porcer += 1
        self.time_verj = (datetime.now() - self.time_skizb).seconds
        return self.porcer, self.time_verj


if __name__ == "__main__":
    CowsAndBulls().play()
