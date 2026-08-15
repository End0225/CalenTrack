from sys import platform
match platform:
    case "win32":
        import subprocess

        subprocess.run(
            [
                "pyinstaller",
                "--onefile",
                "--windowed",
                "--icon=resources/icons/app-logo.ico",
                "--add-data", "resources/icons;resources/icons",
                "main.py"
            ],
            shell = True
        )
    case "darwin":
        from setuptools import setup

        APP = ['main.py']
        DATA_FILES = [
            ('resources/icons', ['resources/icons/app-logo.icns']),
            ('resources/icons', ['resources/icons/are_you_sure.png']),
            ('resources/icons', ['resources/icons/calendar-icon.png']),
            ('resources/icons', ['resources/icons/delete-icon.png']),
            ('resources/icons', ['resources/icons/export-icons.png']),
            ('resources/icons', ['resources/icons/history-icon.svg']),
            ('resources/icons', ['resources/icons/import-icon.png']),
            ('resources/icons', ['resources/icons/left-arrow-icon.png']),
            ('resources/icons', ['resources/icons/note-icon.png']),
            ('resources/icons', ['resources/icons/reset-icon.png']),
            ('resources/icons', ['resources/icons/right-arrow-icon.png']),
            ('resources/icons', ['resources/icons/save-icon.png']),
            ('resources/icons', ['resources/icons/settings-icons.png']),
            ('resources/icons', ['resources/icons/start-icon.png']),
            ('resources/icons', ['resources/icons/stop-icon.png']),
            ('resources/icons', ['resources/icons/stopwatch-icon.png']),
        ]

        OPTIONS = {
            'argv_emulation': True,
            'iconfile': 'resources/icons/app-logo.icns',
            'plist': {
                'CFBundleName': 'CalenTrack',
                'CFBundleDisplayName': 'CalenTrack',
                'CFBundleIdentifier': 'com.calentrack.app',
                'CFBundleVersion': '1.0.0',
                'CFBundleShortVersionString': '1.0.0',
                'NSHighResolutionCapable': True,
            },
            'packages': ['PyQt6'],
            'includes': ['PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets'],
            'excludes': ['tkinter'],
            'site_packages': True,
        }

        setup(
            app=APP,
            data_files=DATA_FILES,
            options={'py2app': OPTIONS},
            setup_requires=['py2app'],
        )