"""Accelerator helpers."""

from .ring import PinPolicy


def default_policy() -> PinPolicy:
    return PinPolicy.NUMA_LOCAL
