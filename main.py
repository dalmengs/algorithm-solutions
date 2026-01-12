import subprocess
import sys
from pathlib import Path

def read_problem_number():
    user_input = input("Input problem number: (Press ENTER to use problem number in `problem.txt`): ").strip()
    if user_input:
        return user_input

    problem_file = Path("problem.txt")
    if not problem_file.exists():
        print("[ERR] `problem.txt` not found")
        sys.exit(1)

    return problem_file.read_text().strip()

def read_file(path: Path) -> str:
    if not path.exists():
        print(f"[ERR] `problem.txt` not found: {path}")
        sys.exit(1)
    return path.read_text()

def normalize(text: str):
    return [line.rstrip() for line in text.strip().splitlines()]

def main():
    problem = read_problem_number()
    base = Path(problem)

    main_py = base / "main.py"
    input_txt = base / "input.txt"
    output_txt = base / "output.txt"

    if not main_py.exists():
        print(f"[ERR] no executable file: {main_py}")
        sys.exit(1)

    input_data = read_file(input_txt)
    expected_output = read_file(output_txt)

    try:
        result = subprocess.run(
            [sys.executable, str(main_py)],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5
        )
    except subprocess.TimeoutExpired:
        print("[TLE] Timelimit exceeded")
        sys.exit(1)

    actual = normalize(result.stdout)
    expected = normalize(expected_output)

    if actual == expected:
        print("[AC] Accept")
        print("\n--- 출력 ---")
        print("\n".join(actual))
    else:
        print("[WA] Wrong Answer")
        print("\n--- 예상 출력 ---")
        print("\n".join(expected))
        print("\n--- 실제 출력 ---")
        print("\n".join(actual))

    f = open("output.txt", "w")
    f.write("\n".join(actual))
    f.close()

if __name__ == "__main__":
    main()
