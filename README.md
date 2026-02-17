# An arm64 tkinterdnd2 that works on a pi5 trixie
- A working replacement for the default tkinterdnd2 venv pip install module. Check the supplied test script for syntax to use it as it is slightly different from the default way to use tkinterdnd2.
## Specific files that were modified are
- tkinterdnd2/tkdnd/linux-arm64/libtkdnd2.9.2.so
- I could not get the 2.9.5 to work so downgraded to 2.9.2 as the original 2.9.3 was compiled with the wrong elf class
- tkinterdnd2/tkdnd/linux-arm64/pkgIndex.tcl this was modified by changing the 2.9.3 entries to 2.92
# That is all that was done.
- Recap, an downgraded but working libtkdnd2.9.2.so and a hack of the pkgIndex.tcl so that the module works.
## The OLD Issue!
- in order to get this to work as it doesn't out of the box, I had to bypass the core drop signal as it kept erroring over  e.serial = getint(nsign), _tkinter.TclError: expected integer but got "%#"
## Now Working
- I have tested test_tk_dnd.py the attached script and it works. So if your on a trixi and arm64 then it should work for you.
## Choose the following method.
- pip install in your venv environment the standard tkinterdnd2. Then copy the  files I identified above , pkgIndex.tcl will have to overwrite the original. Then use my test_tk_dnd.py  as a sample guide to your app. Don't forget to activate your venv environment if you do this.
- Or put the whole modified_tkinterdnd2 in your own modules directory and call it it from there.


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

## How to use it (recommended: method 2)

### Method 1: Overwrite files in existing pip install (quick but dirty)
1. `pip install tkinterdnd2` in your venv
2. Copy these files from this repo:
   - `modified_tkinterdnd2/tkdnd/linux-arm64/libtkdnd2.9.2.so` → overwrite venv's version
   - `modified_tkinterdnd2/tkdnd/linux-arm64/pkgIndex.tcl` → overwrite (must match version)
3. Use normal import: `from tkinterdnd2 import TkinterDnD, DND_ALL, ...`

### Method 2: Use the whole folder as a local module (cleaner, recommended)
1. Copy the entire `modified_tkinterdnd2/` folder into your project's module directory (e.g. `~/bin/mypym/`)
2. In your script, add to sys.path **before** importing:
   ```python
   import sys
   sys.path.insert(0, os.path.expanduser("~/bin/mypym"))
   from modified_tkinterdnd2 import TkinterDnD, DND_ALL






