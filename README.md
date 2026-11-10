# FerriteQueue

Reference implementation of **FerriteQueue**, lock-free ring buffers for
heterogeneous CPU/accelerator queues.

## Repository layout

```
ferritequeue/
  ring.py
  accel.py
benchmarks/
  queue_bench.py
tests/
  test_ring.py
```

The ring buffer, accelerator pin policy, and benchmark driver are included in
full.

## Citation

> A. Evans, J. Mbeki. FerriteQueue: Lock-Free Task Queues for Heterogeneous
> Accelerators. ASPLOS 2025.
