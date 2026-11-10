"""Multi-producer/single-consumer ring buffer."""

from enum import Enum


class PinPolicy(Enum):
    NONE = "none"
    NUMA_LOCAL = "numa-local"


class MpscRing:
    def __init__(self, capacity: int, producer: str = "host", consumer: str = "npu"):
        self.capacity = capacity
        self.producer = producer
        self.consumer = consumer
        self.policy = PinPolicy.NONE

    def set_pin_policy(self, policy: PinPolicy):
        self.policy = policy
        return self

    def run_backpressure(self, mode: str = "credit"):
        return {"mode": mode, "capacity": self.capacity}
