import utils
import logging
import os
import tempfile
import shutil

class NodeClient:
    def __init__(self, chs):
        self.chs = chs
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        self.encryption_key = None
        self.node_config = self.load_node_configuration()
        self.sandbox_dir = None  # Will hold the path for our sandbox environment

    def load_node_configuration(self):
        """
        Loads node configuration settings.
        This simulates the setup phase where node parameters (resource allocation, pricing, etc.)
        are defined as described in the document.
        """
        # In a production system, load configuration from a secure file or environment variables.
        config = {}
        self.logger.info("Node configuration loaded successfully")
        return config

    def process_task(self, task):
        try:
            # Step 1: Validate hash if provided (ensuring data integrity)
            if 'hash' in task:
                if not utils.validate_hash(task['data'], task['hash']):
                    raise ValueError("Hash validation failed for task data")
                self.logger.info("Task data hash validated successfully")

            # Step 2: Decrypt the task data
            data = utils.decrypt(task['data'], task['encryption_key'])
            self.logger.info("Task data decrypted successfully")

            # Step 3: Run the task in a sandbox environment for isolation
            result = self.run_in_sandbox(data)
            self.logger.info("Task processed successfully in sandbox")

            # Step 4: Encrypt the result
            encrypted_result = utils.encrypt(result, task['encryption_key'])
            self.logger.info("Result encrypted successfully")

            # Step 5: Send the result back to the CHS
            self.chs.send_result(task['id'], encrypted_result)
            self.logger.info("Result sent to CHS successfully")

            # Step 6: Cleanup temporary sandbox environment
            self.cleanup_sandbox()
            self.logger.info("Sandbox environment cleaned up successfully")
        except Exception as e:
            self.logger.error(f"Error processing task: {e}")

    def run_in_sandbox(self, data):
        """
        Simulates running the compute operation in an isolated environment.
        In a production node, this would involve launching a Docker container or VM.
        """
        # Create a temporary directory to act as a sandbox
        self.sandbox_dir = tempfile.mkdtemp()
        self.logger.info(f"Sandbox environment created at {self.sandbox_dir}")

        try:
            # For demonstration, write the input data to a file within the sandbox
            input_file = os.path.join(self.sandbox_dir, "input.txt")
            with open(input_file, "w") as f:
                f.write(data)
            self.logger.info("Input data written to sandbox environment")

            # Execute the computation; in production, this would run within the isolated context.
            result = self.compute(data)
            return result
        finally:
            # Note: Cleanup will be handled in the cleanup_sandbox method.
            pass

    def cleanup_sandbox(self):
        """
        Removes the temporary sandbox directory and all its contents.
        This mimics the node’s cleanup phase described in the document.
        """
        if self.sandbox_dir and os.path.exists(self.sandbox_dir):
            shutil.rmtree(self.sandbox_dir)
            self.logger.info(f"Sandbox environment at {self.sandbox_dir} removed")
            self.sandbox_dir = None

    def compute(self, data):
        """
        Placeholder for the actual computation logic.
        In a production environment, this function would be executed in an isolated container.
        """
        # Actual computation would go here.
        return f"Processed: {data}"

    def update_encryption_key(self, new_key):
        """
        Securely updates the encryption key.
        Ensures the new key meets security standards before applying.
        """
        try:
            # Validate the new encryption key (security check)
            if not utils.is_valid_key(new_key):
                raise ValueError("Invalid encryption key provided")
            self.encryption_key = new_key
            self.logger.info("Encryption key updated successfully")
        except Exception as e:
            self.logger.error(f"Error updating encryption key: {e}")
