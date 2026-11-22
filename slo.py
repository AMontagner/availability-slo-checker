"""Evaluate an availability SLO from request counts."""
import argparse
from fractions import Fraction


def evaluate(total, failed, target):
    if total <= 0 or not 0 <= failed <= total or not 0 < target < 1:
        raise ValueError("Require total > 0, 0 <= failed <= total, and 0 < target < 1")
    availability = Fraction(total - failed, total)
    burn_rate = Fraction(failed, total) / (1 - target)
    budget = int(total * (1 - target))
    return availability, burn_rate, budget - failed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--total", type=int, required=True)
    parser.add_argument("--failed", type=int, required=True)
    parser.add_argument("--target", type=Fraction, default=Fraction("0.999"))
    args = parser.parse_args()
    try:
        availability, burn, remaining = evaluate(args.total, args.failed, args.target)
    except ValueError as error:
        parser.error(str(error))
    print(f"Availability: {float(availability):.4%}")
    print(f"Error budget burn: {float(burn):.2f}x")
    print(f"Remaining failure allowance: {remaining}")
    return 0 if availability >= args.target else 1


if __name__ == "__main__":
    raise SystemExit(main())
