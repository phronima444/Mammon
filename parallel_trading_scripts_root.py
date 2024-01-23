
import multiprocessing
import subprocess

def run_script(script_path):
    subprocess.run(["python", script_path], check=True)

if __name__ == "__main__":
    scripts = [
        "/updated_trading_script_with_improvements.py",
        "/retrait_dev40_variante7.py",
        "/2updated_trading_script_performance_optimization.py"
    ]

    processes = []
    for script in scripts:
        p = multiprocessing.Process(target=run_script, args=(script,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
