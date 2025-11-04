# PyPad

Lightweight plain-text editor built with Python and Tkinter. Focuses on fast read/write operations and a minimal, familiar UI.

## Status
- Version: 2.0
- Stable for basic editing and logging. Several UX and safety improvements planned.

## Features
- Open and save plain text files
- Simple event logging to PyPad_Log.txt
- Minimal dependencies (Python + Tkinter + Colorama)

## Quickstart (macOS)
1. Clone the repo:
   git clone <https://github.com/MrSumthun/PyPad.git>
2. Create and activate a virtual environment (recommended):
   python3 -m venv .venv && source .venv/bin/activate
3. Install dependencies :
   pip install -r requirements.txt
4. Run the application:
   python3 PyPad.py

## Default files
- Data file: PyPad.txt
- Log file: PyPad_Log.txt  
These files are created or updated in the current working directory by default.

## Configuration
To change defaults, edit File_Worker.py:
- file_name — base name for the data file
- log_file_name — base name for the log file


## Development notes
- Current implementation opens files at module import and keeps handles open. Prefer using context managers (with open(...)) to avoid resource leaks.
- Logging writes appended timestamped messages. Use seek/end or open with "a" for reliable appends.
- Error handling is minimal; add try/except around I/O operations.

## Roadmap / TODO
- Multiple documents / tabs
- Undo/redo, search/replace
- Replace module-level open() calls with per-operation opens
- Unit tests and CI

## Contributing
1. Fork and create a feature branch.
2. Add tests for behavior changes.
3. Open a pull request with a clear description.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file in the repository for details.

## Contact / Issues
Open issues in the repo for bugs or feature requests and tag them with "help wanted" or "enhancement".


