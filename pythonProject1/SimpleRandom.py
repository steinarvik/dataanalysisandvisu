from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a single name, email, and integer
name = fake.name()
email = fake.email()
random_int = fake.random_int(min=18, max=80)

# Print the generated values
print(name, email, random_int)