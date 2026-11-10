from ferritequeue.ring import MpscRing, PinPolicy


def run():
    ring = MpscRing(capacity=1 << 16, producer="host", consumer="npu")
    ring.set_pin_policy(PinPolicy.NUMA_LOCAL)
    return ring.run_backpressure(mode="credit")


if __name__ == "__main__":
    print(run())
