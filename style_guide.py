## Good example
user_name = "Alice"  # correct

# Bad example (PascalCase for variables)
UserName = "Alice"  # wrong - PascalCase is for classes


# Good example (PascalCase for classes)
class UserAccount:
    pass  # correct

# Bad example (snake_case for classes)
class user_account:
    pass  # wrong


# Section: Indentation

# Good example (consistent indentation with 4 spaces)
def greet(name):
    if name:
        print(f"Hello, {name}!")  # correct
    else:
        print("Hello, stranger!")  # correct

# Bad example (missing or inconsistent indentation)
def greet(name):
if name:
print(f"Hello, {name}!")  # wrong
else:
print("Hello, stranger!")  # wrong


# Section: Constants

# Good example (UPPER_CASE_WITH_UNDERSCORES for constants)
PI = 3.14159  # correct

# Bad example (not uppercase for constants)
pi = 3.14159  # wrong



