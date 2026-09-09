# automation-tool-64

`automation-tool-64` is a lightweight, high-performance Python framework designed to streamline repetitive task execution through modular task definitions. It provides a robust engine for managing local file operations, remote system monitoring, and scheduled script execution.

## Features

*   **Task Scheduling Engine:** Execute complex workflows with sub-second precision using the integrated cron-style scheduler.
*   **Dynamic Plugin System:** Easily extend functionality by dropping custom Python modules into the `plugins/` directory.
*   **Error Recovery Logic:** Built-in retry mechanisms with exponential backoff for network-dependent operations.
*   **Resource Monitoring:** Real-time logging of CPU and memory consumption per task to identify performance bottlenecks.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic Usage

To run a task, define your operation in a `.yaml` configuration file and execute it via the CLI:

```bash
# Execute a specific task defined in config.yaml
python main.py --config configs/backup_task.yaml --verbose

# Run the continuous monitor mode
python main.py --daemon
```

For more advanced configurations, check the `examples/` directory to see how to chain multiple tasks into a single automation pipeline.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.