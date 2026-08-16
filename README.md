 # CalenTrack

[![GitHub release](https://img.shields.io/github/v/release/End0225/CalenTrack)](https://github.com/End0225/CalenTrack/releases/tag/v2.2.0)
[![License](https://img.shields.io/github/license/End0225/CalenTrack)](https://github.com/End0225/CalenTrack/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.9.1%2B-green)](https://pypi.org/project/PyQt6/)
[![SQLite3](https://img.shields.io/badge/SQLite3-3.46.1%2B-green)](https://sqlite.org/)
 
● A desktop time management application built with ***Python (PyQt6)*** using ***MVP architecture*** and ***SQLite3*** for data storage. The app combines a **stopwatch**, **notes** and a **calendar** into a single workflow: track your time with the stopwatch, write notes, and then link both to a specific calendar date — creating a complete snapshot of what you did and how long it took. Each calendar date can be color-coded for visual reference. All data can be exported and imported via `txt` files for backup.

<img width="3076" height="2120" alt="App window" src="https://github.com/user-attachments/assets/4ab1b6a9-cf47-457e-bbcd-3381bf52b8da" />

## Features
- **⏱ Stopwatch** — start, stop, reset. Save time records to history and set any saved records as the current stopwatch time to continue tracking time
- **📋 History** — browse all saved stopwatch records with options to restore a record to the timer or delete it
- **📄 Notes** — create notes with a title. Edit, delete, and link them to calendar dates together with stopwatch records
- **📅 Calendar** — click any date to attach time record and a note, creating a complete snapshot of what you did and how long it took
- **💾 Backup & Restore** – export all data (stopwatch history, notes, calendar entries, settings) to a `txt` file and import it back
- **🌙 Dark theme**

## Stack
- **Python 3.10+** with **PyQt6** for GUI
- **MVP architecture** (Model-View-Presenter)
- **SQLite3** for local data storage
- **PyInstaller** for building standalone `.exe`
- **py2app** for building standalone `.app`

## Installation
### For users
● Download the latest `CalenTrack.exe` (Windows) or `CalenTrack.zip` (macOS) from [Releases](https://github.com/End0225/CalenTrack/releases) and run it.

### Data Storage Location

| Platform | Path |
|----------|------|
| **Windows** | `C:\Users\<User>\AppData\Roaming\CalenTrack\` |
| **macOS** | `~/Library/Application Support/CalenTrack/` |

● The folder contains:
- `app_db.db` — SQLite database with all your data
- `resources/icons/` — application icons

### macOS Troubleshooting
● If you see this error when opening CalenTrack on macOS:
- "Application CalenTrack is damaged and can't be opened. Move it to the Trash."
Don't worry! This is a standard macOS security warning, not a problem with the app. Here's how to fix it:
1. Open Terminal (Finder → Applications → Utilities → Terminal)
2. Run this command:
- ```bash
  sudo xattr -cr
  ```
3. Drag the app into the Terminal window:
- Find `CalenTrack.app` in Finder
- Drag it into the Terminal window (the path will auto-fill)
4. Press Enter
- Terminal will ask for your Mac password
- Note: Characters won't appear while typing — this is normal
- Type your password and press Enter
5. Done! The app will now open normally.

### For developers
● Requires **Python 3.10+**.

```bash
git clone https://github.com/End0225/CalenTrack
cd CalenTrack
pip install -r requirements.txt
python main.py
```

## Build from Source

● To build the application yourself:
```bash
# Windows (creates CalenTrack.exe)
python build.py

# macOS (creates CalenTrack.app)
python3 build.py py2app
```

● The build script automatically detects your OS and uses the appropriate builder:
- Windows: PyInstaller
- macOS: py2app

## Usage
### Run the application
```bash
python main.py
```

## Project Structure
```
CalenTrack/
├── model/                          # Data layer: database and models
│   └── database.py                 # Database operations and models
├── presenters/                     # Business logic presenters
│   ├── stopwatch_presenter.py      # Stopwatch logic
│   ├── history_presenter.py        # History data management
│   ├── notes_presenter.py          # Notes CRUD operations
│   ├── calendar_presenter.py       # Calendar business logic
│   └── settings_presenter.py       # Settings management
├── views/                          # UI components: windows and dialogs
│   ├── main_window.py              # Main application window
│   ├── calendar_view.py            # Calendar widget
│   ├── history_view.py             # History display view
│   ├── notes_view.py               # Notes management view
│   ├── settings_view.py            # Settings configuration view
│   ├── stopwatch_view.py           # Stopwatch widget
│   └── dialogs/                    # Dialog windows
│       ├── calendar_dialog.py      # Calendar selection dialog
│       ├── color_dialog.py         # Color picker dialog
│       ├── confirm_dialog.py       # Confirmation dialog
│       └── date_dialog.py          # Date picker dialog
├── utils/                          # Utilities and helpers
│   ├── button_factory.py           # Button creation utilities
│   └── icon_manager.py             # Icon loading and management
├── resources/                      # Static resources
│   ├── ui/                         # UI design files
│   │   └── CalenTrack.ui           # Main window UI layout
│   └── icons/                      # Application icons
│       ├── app-logo.icns
│       ├── app-logo.ico
│       ├── are_you_sure.png
│       ├── calendar-icon.png
│       ├── delete-icon.png
│       ├── export-icons.png
│       ├── history-icon.svg
│       ├── import-icon.png
│       ├── left-arrow-icon.png
│       ├── note-icon.png
│       ├── reset-icon.png
│       ├── right-arrow-icon.png
│       ├── save-icon.png
│       ├── settings-icons.png
│       ├── start-icon.png
│       ├── stop-icon.png
│       └── stopwatch-icon.png
├── main.py                         # QApplication assembly and entry point
├── build.py                        # Universal build script
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # License file
├── .gitignore                      # Git ignore rules
└── app_db.db                       # SQLite database file
```

## Roadmap
- [ ] **Tag system** — categorize time records with custom tags for filtering and organization
- [ ] **Session-based tracking** — split stopwatch records into individual sessions for accurate statistics and time analysis
- [ ] **Statistics dashboard** — visualize time usage with charts: total time by tags, daily/weekly breakdowns, streaks, and trends
- [ ] **Mobile version** — native Android app
- [ ] **Account sync** — sync data between all devices

## License
● This project is licensed under the MIT License — see the [LICENSE](https://github.com/End0225/CalenTrack/blob/main/LICENSE) file for details.

## Acknowledgements
- Icons by [Icons8](https://icons8.com)
