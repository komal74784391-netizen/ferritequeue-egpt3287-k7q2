from ferritequeue.ring import MpscRing, PinPolicy


def test_policy():
    ring = MpscRing(capacity=1024)
    ring.set_pin_policy(PinPolicy.NUMA_LOCAL)
    assert ring.policy is PinPolicy.NUMA_LOCAL
