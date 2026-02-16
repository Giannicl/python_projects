from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: invalid data type. Expected integer"
        print("Validation: Numeric data verified")
        count = len(data)
        total = sum(data)
        average = total / count
        return f"Processed {count} numeric values, sum={total}, avg={average}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, List):
            return False
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: invalid data type. Expected string"
        print("Validation: Text data verified")
        characters = len(data)
        words = len(data.split())
        return f"Processed text: {characters} characters, {words} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: invalid data type. Expected string"
        print("Validation: Log entry verified")
        log = data.split(":", 1)
        level = log[0]
        message = log[1].strip()
        prefix = "ALERT" if level == "ERROR" else level
        return f"[{prefix}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    try:
        print("\nInitializing Numeric Processor...")
        numeric_processor = NumericProcessor()
        data = [1, 2, 3, 4, 5]
        print(f"Processing data: {data}")
        result = numeric_processor.process(data)
        output = numeric_processor.format_output(result)
        print(output)
    except Exception as e:
        print(f"Error processing numeric data: {e}")
    try:
        print("\nInitializing Text Processor...")
        text_processor = TextProcessor()
        data = "Hello Nexus World"
        print(f'Processing data: "{data}"')
        result = text_processor.process(data)
        output = text_processor.format_output(result)
        print(output)
    except Exception as e:
        print(f"Error processing text data: {e}")
    try:
        print("\nInitializing Log Processor...")
        log_proc = LogProcessor()
        log_data = "ERROR: Connection timeout"
        print(f'Processing data: "{log_data}"')
        result = log_proc.process(log_data)
        output = log_proc.format_output(result)
        print(output)
    except Exception as e:
        print(f"Error processing log data: {e}")

    try:
        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")
        processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
        data_samples = [[1, 2, 3], "Hello World", "INFO: System ready"]
        result_number = 1
        for i in range(len(processors)):
            try:
                processor = processors[i]
                data = data_samples[i]
                result = processor.process(data)
                print(f"Result {result_number}: {result}")
                result_number = result_number + 1
            except Exception as e:
                print(f"Result {result_number}: Error - {e}")
                result_number = result_number + 1
        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except Exception as e:
        print(f"Error in polymorphic processing: {e}")


if __name__ == "__main__":
    main()
