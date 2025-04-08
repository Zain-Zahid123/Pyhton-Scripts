# User se naam aur environment input lein
Name = input("Enter your name: ")
env = input("Enter your environment (e.g., dev, prod, staging): ")

# Greeting message aur environment ke mutabiq output
if env == "dev":
    print(f"Hello {Name}, you are working in the Development environment.")
elif env == "prod":
    print(f"Hello {Name}, you are working in the Production environment.")
elif env == "staging":
    print(f"Hello {Name}, you are working in the Staging environment.")
else:
    print(f"Hello {Name}, your environment is set to {env}.")