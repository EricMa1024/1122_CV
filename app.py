first_name = "Klay"
last_name = "Thompson"
print(f"Hi, my name is {first_name} {last_name}.")
print(f"I'm {20+8} years old.")

def test():
    print("Hello, Thompson!")

# This will run greet() when the module is executed, but not when it's imported.
if __name__ == "__main__":
    test()
