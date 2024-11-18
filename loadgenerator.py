import requests
import time
import os
 
class LoadGenerator:
    def __init__(self, target, frequency):
        self.target = target
        self.frequency = frequency
        self.noofrequests = 0
        self.nooffailures = 0
        self.totalresponsetime = 0
 
    def generate_load(self):
        while True:
            starttime = time.time()
            try:
                response = requests.get(self.target, timeout=10)
                if response.status_code != 200:
                    self.nooffailures = self.nooffailures + 1
            except requests.exceptions.Timeout:
                self.nooffailures = self.nooffailures + 1
 
            endtime = time.time()
            self.noofrequests = self.noofrequests + 1
            self.totalresponsetime += endtime - starttime
 
            time.sleep(1 / self.frequency)
 
            if self.noofrequests % 10 == 0:  # Print metrics every 10 requests
                self.print_metrics()
 
    def print_metrics(self):
        avgresponsetime = self.totalresponsetime / self.noofrequests 
        if self.total_requests > 0 else 0
        print(f"Metrics after {self.noofrequests} requests:")
        print(f"Average Response Time: {avgresponsetime:.4f} seconds")
        print(f"Accumulated Number of Failures: {self.nooffailures}\n")
 
if __name__ == "__main__":
    target = os.getenv("TARGET_ADDRESS", "http://10.152.183.244:8080/primecheck")  # Replace with default target
    frequency = float(os.getenv("REQUESTS_PER_SECOND", 10))  # Replace with default frequency
 
    load_generator = LoadGenerator(target, frequency)
    load_generator.generate_load()