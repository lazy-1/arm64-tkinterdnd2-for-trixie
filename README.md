# arm64-tkinterdnd2-for-trixie

A patched/fixed version of `tkinterdnd2` that **actually works** on Raspberry Pi 5 (arm64) running Debian Trixie.

The official `pip install tkinterdnd2` fails on this platform due to tkdnd library compatibility issues (wrong ELF class, version mismatches, etc.).  
This repo provides a working replacement.

## Tested on
- Raspberry Pi 5 (8 GB)
- Raspberry Pi OS 64-bit (Debian Trixie / Bookworm successor)
- Python 3.11–3.13 (venv)

## What was fixed / changed
- Downgraded to `libtkdnd2.9.2.so` (compiled correctly for arm64)
  - Original 2.9.3 failed with ELF class mismatch
  - 2.9.5 also didn't work
- Modified `tkdnd/linux-arm64/pkgIndex.tcl` → changed all `2.9.3` references to `2.9.2`

That's it — no other code changes.

## It ain't perfect
- in order to get this to work as it doesn't out of the box, I had to bypass the core drop signal as it kept erroring over  e.serial = getint(nsign), _tkinter.TclError: expected integer but got "%#"
- so if you're having issues, check to see that the test script test_tk_dnd.py works and if it does then you have a place to start.

## How to use it (recommended: method 2)

### Method 1: Overwrite files in existing pip install (quick but dirty)
1. `pip install tkinterdnd2` in your venv
2. Copy these files from this repo:
   - `modified_tkinterdnd2/tkdnd/linux-arm64/libtkdnd2.9.2.so`
   - `modified_tkinterdnd2/tkdnd/linux-arm64/pkgIndex.tcl` → overwrite (must match version)
3. Use normal import: `from tkinterdnd2 import TkinterDnD, DND_ALL, ...`

### Method 2: Use the whole folder as a local module (cleaner, recommended)
1. Copy the entire `modified_tkinterdnd2/` folder into your project's module directory. Or create a modules directory and put it in your sys.path:
   ```python
   import sys
   sys.path.insert(0, os.path.expanduser("~/your/modules/path"))```
2. In your script, :
   ```python
   from modified_tkinterdnd2 import TkinterDnD, DND_ALL```

## Happy Dragging and Dropping..




