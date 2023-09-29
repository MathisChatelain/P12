import subprocess


def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        exit(1)


def main():
    for command in ["isort", "flake8", "black"]:
        for path in [
            "main.py",
            "controllers/",
            "utils.py",
            "models/",
            "views/",
            "tests/",
        ]:
            print(f"Running {command} on {path}...")
            run_command(f"{command} {path}")


if __name__ == "__main__":
    main()
