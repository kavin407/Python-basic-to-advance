def create_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Arjun", age=33, job="data engineer")