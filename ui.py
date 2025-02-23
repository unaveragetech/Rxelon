class UserInterface:
    def __init__(self, chs):
        self.chs = chs

    def start(self):
        while True:
            user_input = input("Enter a task (or 'exit' to quit): ")
            if user_input == 'exit':
                break

            task = {
                'data': user_input,
                'encryption_key': 'secret_key'  # Placeholder for actual encryption key
            }
            self.chs.submit_task('user', task)
