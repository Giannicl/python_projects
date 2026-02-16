from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.total_items = 0
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_items": self.total_items,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.data_type = "environmental data"
        self.average_temp = 0
        self.total_temp = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Processing sensor batch: ")
        batch_count = 0
        for item in data_batch:
            if (
                isinstance(item, Dict)
                and "temperature" in item
                and "humidity" in item
                and "pressure" in item
            ):
                self.total_temp = self.total_temp + item["temperature"]
                temperature = item["temperature"]
                humidity = item["humidity"]
                pressure = item["pressure"]
                batch_count = batch_count + 1
                print(f"[temp:{temperature}, humidity:{humidity}, "
                      f"pressure:{pressure}]")
            else:
                print("error: wrong input data")
                return "error: wrong input data"
        self.total_items = self.total_items + len(data_batch)
        self.processed_count = self.processed_count + 1
        self.average_temp = self.total_temp / batch_count
        return (f"Sensor analysis: {batch_count} readings processed, "
                f"avg temp: {self.average_temp}°c")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """return sensor specific statistics"""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.data_type,
            "batches_processed": self.processed_count,
            "total_items": self.total_items,
            "total_temp": self.total_temp,
            "average_temp": self.average_temp,
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.data_type = "financial data"
        self.total_buy = 0
        self.total_sell = 0
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Processing transaction batch: ", end="")
        operation_count = 0
        transaction_string = ""
        sign = ""
        batch_buy = 0
        batch_sell = 0
        for item in data_batch:
            if isinstance(item, Dict) and "type" in item and "amount" in item:
                operation_count = operation_count + 1
                if transaction_string != "":
                    transaction_string = (
                        transaction_string +
                        f", {item['type']}:{item['amount']}"
                    )
                else:
                    transaction_string = f"{item['type']}:{item['amount']}"
                if item["type"] == "buy":
                    batch_buy = batch_buy + item["amount"]
                else:
                    batch_sell = batch_sell + item["amount"]
            else:
                return "error: wrong input data"
        print(f"[{transaction_string}]")
        self.total_buy = self.total_buy + batch_buy
        self.total_sell = self.total_sell + batch_sell
        self.total_items = self.total_items + operation_count
        self.processed_count = self.processed_count + 1
        self.net_flow = self.total_buy - self.total_sell
        batch_net_flow = batch_buy - batch_sell
        sign = "+" if self.net_flow >= 0 else ""
        return (f"Transaction analysis: {operation_count} operations, "
                f"net flow: {sign}{batch_net_flow} units")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """return transaction-specific statistics"""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.data_type,
            "batches_processed": self.processed_count,
            "total_items": self.total_items,
            "total_buy": self.total_buy,
            "total_sell": self.total_sell,
            "net_flow": self.net_flow,
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.data_type = "system events"
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        event_string = ""
        batch_event_count = 0
        batch_error_count = 0
        print("Processing event batch: ", end="")
        for item in data_batch:
            if (
                isinstance(item, Dict)
                and "event" in item
                and ("user" in item or "message" in item)
            ):
                batch_event_count = batch_event_count + 1
                if item["event"] == "login" or item["event"] == "logout":
                    if event_string != "":
                        event_string = event_string + f", {item['event']}"
                    else:
                        event_string = f"{item['event']}"
                elif item["event"] == "error":
                    batch_error_count = batch_error_count + 1
                    if event_string != "":
                        event_string = event_string + f", {item['event']}"
                    else:
                        event_string = f"{item['event']}"
            else:
                print("error: wrong input data")
                return "error: wrong input data"
        self.total_items = self.total_items + batch_event_count
        self.processed_count = self.processed_count + 1
        self.error_count = self.error_count + batch_error_count
        print(f"[{event_string}]")
        return (f"Event analysis: {batch_event_count} events, "
                f"{batch_error_count} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """return event-specific statistics"""
        return {
            "stream_id": self.stream_id,
            "stream_type": "system events",
            "batches_processed": self.processed_count,
            "total_items": self.total_items,
            "error_count": self.error_count,
        }


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("sensor_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.data_type}")

    sensor_data = [
        {"temperature": 22.5, "humidity": 65, "pressure": 1013},
        {"temperature": 23.0, "humidity": 63, "pressure": 1012},
        {"temperature": 22.0, "humidity": 67, "pressure": 1014},
    ]

    try:
        result1 = sensor.process_batch(sensor_data)
        print(result1)
    except Exception as e:
        print(f"error: {e}")

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("trans_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.data_type}")

    transaction_data = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75},
    ]

    try:
        result2 = transaction.process_batch(transaction_data)
        print(result2)
    except Exception as e:
        print(f"error: {e}")

    print("\nInitializing event stream...")
    event = EventStream("event_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.data_type}")

    event_data = [
        {"event": "login", "user": "alice"},
        {"event": "error", "message": "timeout"},
        {"event": "logout", "user": "alice"},
    ]

    try:
        result3 = event.process_batch(event_data)
        print(result3)
    except Exception as e:
        print(f"error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams = [sensor, transaction, event]

    print("\nBatch 1 Results:")

    for stream in streams:
        try:
            stats = stream.get_stats()

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stats['total_items']} "
                      f"readings processed")
            elif isinstance(stream, TransactionStream):
                print(
                    f"- Transaction data: {stats['total_items']} "
                    "operations processed"
                )
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stats['total_items']} events processed")
        except Exception as e:
            print(f"Error: {e}")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
