 # CalenTrack
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

## Installation
### For users
● Download the latest `CalenTrack.exe` from [Releases](https://github.com/End0225/CalenTrack/releases) and run it.

### For developers
● Requires **Python 3.10+**.

```bash
git clone https://github.com/End0225/CalenTrack
cd CalenTrack
pip install -r requirements.txt
python main.py
```

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
│       ├── app-logo.ico
│       ├── are_you_sure.webp
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
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # License file
├── .gitignore                      # Git ignore rules
└── app_db.db                       # SQLite database file
```

## Roadmap
- [ ] **macOS support** — native macOS version of CalenTrack
- [ ] **Tag system** — categorize time records with custom tags for filtering and organization
- [ ] **Session-based tracking** — split stopwatch records into individual sessions for accurate statistics and time analysis
- [ ] **Statistics dashboard** — visualize time usage with charts: total time by tags, daily/weekly breakdowns, streaks, and trends
- [ ] **Mobile version** — native Android app
- [ ] **Account sync** — sync data between all devices

## License
● This project is licensed under the MIT License — see the [LICENSE](https://github.com/End0225/CalenTrack/blob/main/LICENSE) file for details.

## Acknowledgements
- Icons by [Icons8](https://icons8.com)
