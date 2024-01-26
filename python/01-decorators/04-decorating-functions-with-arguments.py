from decorators import do_twice

@do_twice
def scream_loudly_with_name(name):
    print(f"HELLOOO {name.upper()}!")

scream_loudly_with_name("Shubham")