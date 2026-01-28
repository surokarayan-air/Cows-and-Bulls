
# 🐄 Cows and Bulls Game (Python)

A console-based implementation of the classic **Cows and Bulls** number guessing game written in **Python** using object-oriented programming.

---

## 🎯 Game Description

The computer generates a **random 4-digit number** with **no repeating digits**.
Your goal is to guess that number.

After each guess, the program tells you:

* **Cows 🐄** → correct digit in the **correct position**
* **Bulls 🐂** → correct digit but in the **wrong position**

The game continues until you get **4 cows**, meaning you guessed the number correctly.

---

## 🧠 Rules

1. You must enter a **4-digit number**.
2. All digits must be **different**.
3. Only numeric input is allowed.
4. The game tracks:

   * Number of attempts
   * Total time taken to win

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python cows_and_bulls.py
```

---

## 🛠 How the Program Works

### 🔹 Secret Number Generation

The program generates a random 4-digit number:

```python
self.random_tiv = str(random.randint(1000, 9999))
```

It ensures all digits are unique:

```python
len(set(self.random_tiv)) == 4
```

---

### 🔹 User Input Validation

The game keeps asking until the user enters a valid number:

* Must contain digits only
* Must be exactly 4 digits long
* Must not contain repeated digits

---

### 🔹 Cows and Bulls Calculation

```python
for i in range(4):
    if self.user_tiv[i] == self.random_tiv[i]:
        self.cows += 1
    elif self.user_tiv[i] in self.random_tiv:
        self.bulls += 1
```

* Same digit & same position → **Cow**
* Digit exists but different position → **Bull**

---

### 🔹 Game Loop

The game repeats until:

```python
if self.cows == 4:
```

Then it prints:

* Total attempts
* Time spent playing

---

## ⏱ Features

* Object-oriented design
* Input validation
* Attempt counter
* Game timer
* Random unique-digit number generation

---

## 📌 Example Output

```
Տուր ինձ քառանիշ թիվ - 1234
cows = 1
bulls = 2

Տուր ինձ քառանիշ թիվ - 4271
You Win! Դուք փորձեցիք 5 անգամ
```

---

## 👨‍💻 Author

Created as a Python practice project to demonstrate:

* Classes & methods
* Loops & conditions
* String handling
* Game logic
* Time measurement

---
