# Toy Epidemic Model in 50 Lines of Python

Welcome to a beginner-friendly simulation of how diseases spread — all in just **50 lines of Python**!

This simple SIR (Susceptible-Infected-Recovered) model lets you experiment with how infections move through a population using basic logic and loops. No fancy math or libraries required — just Python, curiosity, and matplotlib for plotting.

---

## What It Does

This script simulates:

- A population of 100 individuals
- A single initial infected person
- Infection spreading with a probability (`beta`)
- Recovery after a fixed number of days

And then it plots how many people are susceptible, infected, or recovered over time.

---

## Who It's For

- Students curious about disease modeling
- Coders trying their first simulation
- Scientists who want to build from a minimal starting point
- Anyone who’s asked: *“How hard is it to simulate an epidemic?”*

---

## Requirements

- Python 3.x
- `matplotlib` (for plotting)

Install `matplotlib` if you don't have it:

```bash
pip install matplotlib
```

---

## How to Run

Clone the repo and run the script:

```bash
git clone https://github.com/pradyutk42/toy-epidemic-model.git
cd toy-epidemic-model
python3 toy_epidemic_model.py
```

You’ll get a plot showing how the epidemic unfolds over time.

---

## Try Tweaking

You can modify:
- `beta` (infection probability)
- `infectious_period`
- Population size `N`
- Starting with more infected people
- Add randomness, vaccination, or even new compartments!

---

## Background / Citation

This toy model is inspired by the classic SIR model introduced by:

> Kermack, W. O., & McKendrick, A. G. (1927). A Contribution to the Mathematical Theory of Epidemics. *Proceedings of the Royal Society of London. Series A*, 115(772), 700–721.

Adapted here as a hands-on coding exercise for educational purposes.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

You’re free to use, modify, and distribute this code — just include credit back to the original author.

---

Made with ☕️ by [Pradyut Kumar](https://github.com/pradyutk42)
