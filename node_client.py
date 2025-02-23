import utils

class NodeClient:
    def __init__(self, chs):
        self.chs = chs

    def process_task(self, task):
        # Decrypt the task data
        data = utils.decrypt(task['data'], task['encryption_key'])

        # Process the task (placeholder for actual computation)
        result = self.compute(data)

        # Encrypt the result
        encrypted_result = utils.encrypt(result, task['encryption_key'])

        # Send the result back to the CHS
        self.chs.send_result(task['id'], encrypted_result)

    def compute(self, data):
        # Placeholder for the actual computation logic
        return f"Processed: {data}"
