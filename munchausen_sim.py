import time

class MunchausenComponent:
    """Simulates a core component philosophy of Munchausen: self-sufficiency and minimal external dependencies."""
    def __init__(self, name):
        self.name = name
        self.state = "initialized"
        print(f"[{self.name}] Component created. State: {self.state}")

    def process_data(self, data):
        """Simulates internal data processing without relying on external services."""
        print(f"[{self.name}] Processing data: {data}")
        # Simulate some internal computation
        processed_data = data.upper() + "_PROCESSED"
        self.state = "processing"
        time.sleep(0.1) # Simulate work
        self.state = "idle"
        print(f"[{self.name}] Data processed. New state: {self.state}")
        return processed_data

    def get_status(self):
        """Provides internal status, reflecting self-contained nature."""
        return f"Status of {self.name}: {self.state}"

class MunchausenApp:
    """Simulates the overall application structure, orchestrating components."""
    def __init__(self):
        print("--- Munchausen Application Simulation ---")
        # Instantiate components, demonstrating modularity without tight coupling
        self.component_a = MunchausenComponent("ComponentA")
        self.component_b = MunchausenComponent("ComponentB")
        self.state = "running"

    def run(self, input_data):
        """Orchestrates data flow between components."""
        print(f"[App] Starting run with data: {input_data}")
        
        # Component A processes data
        processed_by_a = self.component_a.process_data(input_data)
        
        # Component B uses the output of A (simulating internal data flow)
        final_output = self.component_b.process_data(processed_by_a)
        
        print(f"[App] Final output: {final_output}")
        print(f"[App] Component A status: {self.component_a.get_status()}")
        print(f"[App] Component B status: {self.component_b.get_status()}")
        print("--- Run complete ---")

if __name__ == "__main__":
    app = MunchausenApp()
    app.run("sample_input_string")
