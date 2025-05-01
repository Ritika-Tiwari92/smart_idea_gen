
# main.py

import tkinter as tk
from tkinter import messagebox, scrolledtext,ttk
from idea_generator import generate_idea
from idea_storage import save_idea, load_ideas, clear_all_ideas


#Theme variables
is_dark_mode = False


    
def apply_theme():
    colors = dark_theme if is_dark_mode else light_theme
    app.configure(bg=colors["bg"])
    for widget in all_widgets:
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.config(bg=colors["bg"], fg=colors["fg"])
        if isinstance(widget, tk.Entry) or isinstance(widget, tk.Text) or isinstance(widget, scrolledtext.ScrolledText):
            widget.config(bg=colors["entry_bg"], fg=colors["fg"], insertbackground=colors["fg"])
    ideas_box.config(state=tk.DISABLED)

def toggle_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()

def on_generate():
    category = entry.get()
    if not category:
        messagebox.showerror("Error", "Please enter a category.")
        return
    idea = generate_idea(category)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, idea)

def on_save():
    category = entry.get()
    idea = text_output.get("1.0", tk.END).strip()
    if not category or not idea:
        messagebox.showerror("Error", "Nothing to save.")
        return
    save_idea(category, idea)
    messagebox.showinfo("Saved", "Idea saved successfully!")
    load_and_display_ideas()

def load_and_display_ideas(filter_category=None):
    saved_ideas = load_ideas()
    ideas_box.config(state=tk.NORMAL)
    ideas_box.delete("1.0", tk.END)

    filtered = [i for i in saved_ideas if not filter_category or i['category'].lower() == filter_category.lower()]

    if not filtered:
        ideas_box.insert(tk.END, "No matching ideas found.")
    else:
        for idea in reversed(filtered[-10:]):
            ideas_box.insert(tk.END, f"[{idea.get('time','no time')} ({idea['category']})\n{idea['idea']}\n\n")
    ideas_box.config(state=tk.DISABLED)

def on_filter():
    category = filter_entry.get().strip()
    load_and_display_ideas(filter_category=category)

def on_clear():
    result = messagebox.askyesno("Confirm", "Are you sure you want to delete all saved ideas?")
    if result:
        clear_all_ideas()
        load_and_display_ideas()
        messagebox.showinfo("Cleared", "All ideas have been deleted.")

# Color themes
light_theme = {
    "bg": "#ffffff",
    "fg": "#000000",
    "entry_bg": "#f0f0f0"
}
dark_theme = {
    "bg": "#2e2e2e",
    "fg": "#ffffff",
    "entry_bg": "#3c3c3c"
}

# GUI setup
app = tk.Tk()
app.title("Smart Idea Generator")
app.geometry("550x650")

# Widgets
label_category = tk.Label(app, text="Enter Idea Category:")
entry = tk.Entry(app, width=60)
btn_generate = tk.Button(app, text="Generate Idea", command=on_generate)
text_output = tk.Text(app, height=5, width=60)
btn_save = tk.Button(app, text="Save Idea", command=on_save)

label_filter = tk.Label(app, text="Filter by Category:")
filter_entry = tk.Entry(app, width=30)
btn_filter = tk.Button(app, text="Apply Filter", command=on_filter)

btn_clear = tk.Button(app, text="Clear All Ideas", command=on_clear, fg="red")
btn_toggle = tk.Button(app, text="Toggle Dark/Light Mode", command=toggle_mode)

label_saved = tk.Label(app, text="Saved Ideas:")
ideas_box = scrolledtext.ScrolledText(app, height=12, width=65, state=tk.DISABLED)

# Pack all widgets
widgets = [
    label_category, entry, btn_generate, text_output, btn_save,
    label_filter, filter_entry, btn_filter, btn_clear, btn_toggle,
    label_saved, ideas_box
]

for w in widgets:
    w.pack(pady=2)

all_widgets = widgets
apply_theme()
load_and_display_ideas()

app.mainloop()
