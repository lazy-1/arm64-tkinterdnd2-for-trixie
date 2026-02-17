#!/usr/bin/python3
import os
import sys


import tkinter as tk
from tkinter import ttk


try:
    from modified_tkinterdnd2 import TkinterDnD, DND_ALL
    DnD_Class = TkinterDnD.Tk
    DnD_Target = DND_ALL
    print("Pi → using tkinterdnd2 (arm64)", 22)
    root = TkinterDnD.Tk()
    try:
        print("Trying package require tkdnd...")
        version = root.tk.call('package', 'require', 'tkdnd')
        print(f"tkdnd loaded, version: {version}")
    except Exception as e:
        print(f"package require tkdnd failed: {e}", 9)
    root.destroy()
    
except Exception as e:
        print(f"tkinterdnd2 import or setup failed on Pi: {e}", 9)
        DnD_Class = tk.Tk
        DnD_Target = None




class DragDropTestApp(DnD_Class):
    def __init__(self):
        super().__init__()
        self.title("minimal drop test + drag source")
        self.geometry("600x400")

        if DnD_Target is not None:
            try:
                version = self.tk.call('package', 'require', 'tkdnd')
                print(f"tkdnd loaded successfully, version: {version}", 22)
            except Exception as e:
                print(f"package require tkdnd failed: {e}", 9)

        # DROP ZONE (left)
        drop_frame = ttk.Frame(self)
        drop_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)
        tk.Label(drop_frame, text="DROP HERE\n(file / url / text)", font=("Arial", 14, "bold"),
                 bg="#e0e0ff", relief="groove", padx=30, pady=60).pack(expand=True)
        drop_frame.drop_target_register(DnD_Target)
        drop_frame.dnd_bind('<<Drop>>', self.on_drop)

        # DRAG SOURCE (right)
        drag_frame = ttk.Frame(self)
        drag_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

        self.drag_label = tk.Label(drag_frame, text="DRAG ME →\n(custom text)",
                                   font=("Arial", 14, "bold"), bg="#ffe0e0", relief="raised",
                                   padx=40, pady=60, cursor="hand2")
        self.drag_label.pack(expand=True)

        # ─── ADD THESE TWO LINES FOR DRAG SOURCE ───
        self.drag_label.drag_source_register(1)                  # register as source (button 1 = left click)
        self.drag_label.dnd_bind('<<DragInitCmd>>', self.on_drag_init)
        self.drag_label.dnd_bind('<<DragEndCmd>>', self.on_drag_end)  # optional

    def on_drag_init(self, event):
        text_to_send = "Hello from test app - custom string 12345"
        print("Drag init - offering:", repr(text_to_send))
        return "copy", "text/plain", text_to_send

    def on_drag_end(self, event):
        print("Drag operation ended")

    def on_drop(self, event):
        print("DROPPED EVENT FIRED!")
        print("data:    ", repr(event.data))
        print("types:   ", getattr(event, 'types', 'no types attr'))
        print("action:  ", getattr(event, 'action', 'no action attr'))
        print("-"*50)














        

if __name__ == "__main__":
    app = DragDropTestApp()
    app.mainloop()
