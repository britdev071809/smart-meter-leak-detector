import subprocess
import sys


def test_script_output():
    """Run the detection script and verify it finds the simulated leak."""
    result = subprocess.run(
        [sys.executable, 'analyze_usage.py'],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()
    expected = 'Potential continuous leak detected from 2025-01-02 00:00:00 to 2025-01-02 23:00:00'
    assert expected in output, f'Expected leak not found. Output:\n{output}'
    print('Test passed: leak correctly detected.')


if __name__ == '__main__':
    test_script_output()