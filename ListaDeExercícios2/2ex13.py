emails = ["test@gmail.com", "admin@escola.br", "prof@escola.br", "test4477@gmail.com", "estagiario@escola.br"]
print("===Emails Válidos===")
for email in emails:
    if email.endswith("@escola.br"):
        print(email)
