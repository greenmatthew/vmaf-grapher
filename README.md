# vmaf-grapher

## Summary

The `vmaf-grapher` application provides a visual representation of [Video Multi-Method Assessment Fusion (VMAF)](https://github.com/Netflix/vmaf.git) scores, allowing users to graphically assess video quality. Developed by Netflix, VMAF is a perceptual video quality assessment algorithm that combines human vision modeling with machine learning. This tool is ideal for anyone needing to evaluate and visualize the quality of their video streams against various codecs and settings.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a `Linux/Unix` environment or `Windows 10/11` with WSL2 installed.
- You have installed Python 3.6 or higher.

## Dependencies

Install the necessary system packages and Python libraries:

```bash
sudo apt-get update
sudo apt-get install git make python3 python3-tk
pip install Pillow matplotlib PyInstaller
```

## Installation and Execution

```bash
git clone https://github.com/greenmatthew/vmaf-grapher.git
cd vmaf-grapher/
make build
./bin/vmaf-grapher <file_path>
```

> Replace <file_path> with the path to your VMAF XML output file to visualize the VMAF scores.

## If your having any issues with the prerequisites

Try just running the script directly with python:

```bash
python3 src/vmaf-grapher.py <file_path>
```


> Replace <file_path> with the path to your VMAF XML output file to visualize the VMAF scores.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](./LICENSE) file included with the code.