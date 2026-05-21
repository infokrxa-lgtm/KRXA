import argparse
from scripts.state_engine import StateEngine
from scripts.run_m2m import run_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="KRXA local execution engine")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "reset", "advance", "run-m2m", "recover"])
    parser.add_argument("--message", default="안녕하세요. 말대말 로컬 실행 테스트입니다.")
    args = parser.parse_args()

    engine = StateEngine()

    if args.command == "status":
        print("KRXA EXEC ENGINE: READY")
        print(f"STATE: {engine.current_state()}")
    elif args.command == "reset":
        engine.reset()
        print("KRXA EXEC ENGINE: RESET COMPLETE")
    elif args.command == "advance":
        print(f"STATE: {engine.advance('manual_advance')}")
    elif args.command == "run-m2m":
        run_demo(args.message)
    elif args.command == "recover":
        engine.reconnect_and_recover()
        print(f"STATE: {engine.current_state()}")


if __name__ == "__main__":
    main()
