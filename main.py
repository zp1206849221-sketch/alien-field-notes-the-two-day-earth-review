import os

ENTRY = (
    "Field note, Day 2 - 4/5 stars: Earth's rulers are small, four-legged "
    "and adored; their tall servants trail behind them, bagging "
    "their warm droppings and carrying them home like sacred relics."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
