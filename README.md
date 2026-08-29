# automation-tool-64

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

automation-tool-64 is a Python-based command-line utility for automating repetitive system and file operations on 64-bit platforms. It lets users define reliable workflows through configuration files rather than writing one-off scripts.

## Features
- YAML-based task definitions with support for variables, conditions, and loops
- Parallel execution with automatic dependency resolution between tasks
- Built-in retry logic, logging, and performance timing for each step
- Environment variable injection and secret handling from external sources

## Installation

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -e .
```

## Usage

Create a `workflow.yaml` file:

```yaml
name: daily-backup
tasks:
  - id: cleanup
    command: find /tmp -type f -mtime +3 -delete
  - id: backup
    command: tar -czf /backups/data.tar.gz /data
    depends_on: cleanup
```

Run the workflow:

```bash
automation-tool-64 run workflow.yaml
```

## License

This project is licensed under the MIT License.