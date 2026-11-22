# Availability SLO and error budget checker

A dependency-free Python CLI that evaluates a request-based availability SLO for one observation window. Use it with request totals and failed-request counts collected over the same window and for the same service.

```sh
python3 slo.py --total 10000 --failed 5 --target 0.999
python3 -m unittest -v
```

At a 99.9% objective, 10,000 requests allow 10 failures. Five failures yield 99.95% availability, a 0.50× burn rate, and five failures of remaining allowance. The checker exits with code 0 when the SLO is met, 1 when it is missed, or 2 for invalid input. Counts are request-weighted, and the allowed failure count is rounded down.

Burn rate compares the observed failure fraction with the fraction allowed by the objective. This is a single-window calculation for inspection or CI validation. Production alerting can combine multiple windows to distinguish short spikes from sustained budget consumption.
