#!/usr/bin/env python3

"""Minimal CLI for UniversoEspiritual."""

__version__ = "0.1.0"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="UniversoEspiritual CLI")
    parser.add_argument("--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(__version__)
    else:
        print("Bienvenido a UniversoEspiritual — tu viaje comienza aquí.")


if __name__ == "__main__":
    main()
