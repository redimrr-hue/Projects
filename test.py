input("Input:")

class EmailNotifier:

    def send(self, message): 
        print("Email:", message)

class SMSNotifier:

    def send(self, message):
        print("SMS:", message)

print(EmailNotifier)
print(SMSNotifier)