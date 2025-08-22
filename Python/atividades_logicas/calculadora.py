import tkinter as tk
from tkinter import ttk, messagebox
import math
import sys

# ---------------------------
# Ambiente seguro para eval
# ---------------------------
safe_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
# adicionar nomes úteis
safe_names.update({
    "pi": math.pi,
    "e": math.e,
    "sqrt": math.sqrt,
    "pow": pow,
    "abs": abs,
    "round": round,
})

# operadores permitidos via eval ainda são os normais; evitamos builtins
SAFE_GLOBALS = {"__builtins__": None}
SAFE_GLOBALS.update(safe_names)

# ---------------------------
# Calculadora Tkinter
# ---------------------------
class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Científica")
        self.geometry("760x480")
        self.minsize(720, 420)
        self.configure(bg="#121315")
        self.angle_mode = tk.StringVar(value="RAD")  # RAD or DEG
        self.memory = 0.0
        self.history = []
        self.create_styles()
        self.create_widgets()
        self.bind_keys()

    def create_styles(self):
        style = ttk.Style(self)
        # tema simples custom
        style.theme_use('clam')
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("TLabel", background="#121315", foreground="white", font=("Segoe UI", 10))
        style.configure("Entry.TEntry", foreground="#111", fieldbackground="#f6f6f6", font=("Consolas", 14))
        style.map("TButton",
                  background=[('active', '#2a2a2a')],
                  foreground=[('active', 'white')])

    def create_widgets(self):
        # top frame: display + mode + theme
        top = tk.Frame(self, bg="#121315")
        top.pack(side="top", fill="x", padx=12, pady=8)

        # left: display & keypad
        left = tk.Frame(self, bg="#121315")
        left.pack(side="left", fill="both", expand=True, padx=(12,6), pady=6)

        # right: history & extra
        right = tk.Frame(self, bg="#0f0f10", width=240)
        right.pack(side="right", fill="y", padx=(6,12), pady=6)
        right.pack_propagate(False)

        # Display
        self.entry_var = tk.StringVar()
        entry_frame = tk.Frame(left, bg="#1c1c1f")
        entry_frame.pack(fill="x", pady=(0,10))
        self.display = ttk.Entry(entry_frame, textvariable=self.entry_var, style="Entry.TEntry", justify="right")
        self.display.pack(ipady=12, fill="x", padx=6, pady=6)

        # small info bar
        info_frame = tk.Frame(entry_frame, bg="#121315")
        info_frame.pack(fill="x", padx=6, pady=(0,6))
        self.angle_label = ttk.Label(info_frame, text=f"Modo: {self.angle_mode.get()}")
        self.angle_label.pack(side="left")
        ttk.Label(info_frame, text="   ").pack(side="left")
        ttk.Label(info_frame, text="© Calculadora").pack(side="left")

        # Buttons grid
        btn_frame = tk.Frame(left, bg="#121315")
        btn_frame.pack(fill="both", expand=True)

        # Define buttons layout (rows of labels)
        buttons = [
            ["MC","MR","M+","M-","C","<-","(",")"],
            ["sin","cos","tan","ln","log","exp","^","!"],
            ["7","8","9","/","sqrt","abs","pi","e"],
            ["4","5","6","*","10^x","%","",""],
            ["1","2","3","-","x!","deg","rad",""],
            ["0",".","±","+","=","ANS","Hist","Theme"]
        ]

        # mapping functions
        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                if label == "":
                    continue
                b = ttk.Button(btn_frame, text=label, command=lambda t=label: self.on_button(t))
                b.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
        # grid config
        for i in range(8):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)

        # Right side: history and controls
        ttk.Label(right, text="Histórico", background="#0f0f10", foreground="white", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        self.history_list = tk.Listbox(right, bg="#0b0b0c", fg="white", bd=0, highlightthickness=0, font=("Consolas",10))
        self.history_list.pack(fill="both", expand=True, padx=10, pady=8)
        self.history_list.bind("<Double-Button-1>", self.on_history_select)

        ctrl_frame = tk.Frame(right, bg="#0f0f10")
        ctrl_frame.pack(fill="x", padx=10, pady=8)
        ttk.Button(ctrl_frame, text="Limpar Hist", command=self.clear_history).pack(side="left", expand=True)
        ttk.Button(ctrl_frame, text="Salvar Mem", command=self.save_memory).pack(side="left", expand=True)

        # footer: status
        self.status = tk.Label(self, text="Pronto", anchor="w", bg="#0f0f10", fg="white")
        self.status.pack(side="bottom", fill="x")

        # initialize
        self.update_theme(dark=True)

    # ---------------------------
    # Button handling and eval
    # ---------------------------
    def on_button(self, label):
        if label == "C":
            self.entry_var.set("")
        elif label == "<-":
            self.entry_var.set(self.entry_var.get()[:-1])
        elif label == "=":
            self.calculate()
        elif label == "ANS":
            if self.history:
                self.entry_var.set(self.entry_var.get() + str(self.history[-1][1]))
        elif label == "Hist":
            self.show_history_popup()
        elif label == "Theme":
            self.toggle_theme()
        elif label == "MC":
            self.memory = 0.0
            self.status.config(text="Memória limpa")
        elif label == "MR":
            self.entry_var.set(self.entry_var.get() + str(self.memory))
        elif label == "M+":
            try:
                v = float(self.safe_eval(self.entry_var.get()))
                self.memory += v
                self.status.config(text=f"Memória: {self.memory}")
            except Exception as e:
                messagebox.showerror("Erro", "Valor inválido para M+")
        elif label == "M-":
            try:
                v = float(self.safe_eval(self.entry_var.get()))
                self.memory -= v
                self.status.config(text=f"Memória: {self.memory}")
            except Exception as e:
                messagebox.showerror("Erro", "Valor inválido para M-")
        elif label == "Hist":
            pass
        elif label == "sqrt":
            self.entry_var.set(self.entry_var.get() + "sqrt(")
        elif label == "ln":
            self.entry_var.set(self.entry_var.get() + "log(")  # natural log in math is log
        elif label == "log":
            self.entry_var.set(self.entry_var.get() + "log10(")
        elif label == "exp":
            self.entry_var.set(self.entry_var.get() + "exp(")
        elif label == "pi":
            self.entry_var.set(self.entry_var.get() + "pi")
        elif label == "e":
            self.entry_var.set(self.entry_var.get() + "e")
        elif label == "sin":
            self.entry_var.set(self.entry_var.get() + "sin(")
        elif label == "cos":
            self.entry_var.set(self.entry_var.get() + "cos(")
        elif label == "tan":
            self.entry_var.set(self.entry_var.get() + "tan(")
        elif label == "sqrt":
            self.entry_var.set(self.entry_var.get() + "sqrt(")
        elif label == "10^x":
            self.entry_var.set(self.entry_var.get() + "10**(")
        elif label == "^":
            self.entry_var.set(self.entry_var.get() + "**")
        elif label == "%":
            self.entry_var.set(self.entry_var.get() + "/100")
        elif label == "±":
            cur = self.entry_var.get()
            if cur.startswith("-"):
                self.entry_var.set(cur[1:])
            else:
                self.entry_var.set("-" + cur)
        elif label == "x!":
            self.entry_var.set(self.entry_var.get() + "fact(")
        elif label == "!":
            self.entry_var.set(self.entry_var.get() + "fact(")
        elif label == "deg":
            self.set_angle("DEG")
        elif label == "rad":
            self.set_angle("RAD")
        elif label == "ln":
            self.entry_var.set(self.entry_var.get() + "log(")
        else:
            # numbers and operators
            self.entry_var.set(self.entry_var.get() + label)

    def set_angle(self, mode):
        self.angle_mode.set(mode)
        self.angle_label.config(text=f"Modo: {mode}")

    def toggle_theme(self):
        current = getattr(self, "_dark", True)
        self.update_theme(dark=not current)

    def update_theme(self, dark=True):
        self._dark = dark
        if dark:
            bg = "#121315"
            right_bg = "#0f0f10"
            entry_bg = "#f6f6f6"
            fg = "white"
        else:
            bg = "#f2f2f2"
            right_bg = "#ffffff"
            entry_bg = "#ffffff"
            fg = "black"
        self.configure(bg=bg)
        for child in self.winfo_children():
            try:
                child.configure(bg=bg)
            except Exception:
                pass
        self.history_list.configure(bg=right_bg, fg=fg)
        self.status.configure(bg=right_bg, fg=fg)

    def safe_eval(self, expr):
        # replace factorial notation fact(x) or trailing 'fact(' usage
        expr = expr.replace("fact(", "factorial(")
        # handle deg mode for trig functions by wrapping sin(x) -> sin(rad(x)) if in DEG
        if self.angle_mode.get() == "DEG":
            # replace sin(x) with sin(radians(x)) etc.
            expr = self._wrap_trig_with_radians(expr, ["sin", "cos", "tan", "asin", "acos", "atan"])
        # prevent accidental double underscores or builtins
        if "__" in expr:
            raise ValueError("unsafe expression")
        # evaluate
        return eval(expr, SAFE_GLOBALS, {})

    def _wrap_trig_with_radians(self, expr, funcs):
        # naive replace: func( -> func(radians(
        for f in funcs:
            expr = expr.replace(f + "(", f"__radians__({f}(")  # temporary marker
        # now replace temporary markers with f"(radians(x))" pattern
        # easier to do double replace: revert to correct pattern using math.radians
        expr = expr.replace("__radians__", "math.radians")
        # But math isn't in local eval namespace, so use radians from safe_names -> 'radians'
        expr = expr.replace("math.radians", "radians")
        return expr

    def calculate(self):
        exp = self.entry_var.get().strip()
        if not exp:
            return
        try:
            # provide factorial support, radians in safe_names already
            # Add 'factorial' alias if not present
            SAFE_GLOBALS_local = SAFE_GLOBALS.copy()
            SAFE_GLOBALS_local.update({"factorial": math.factorial, "radians": math.radians})
            # Use our safe_eval with a modified environment
            result = eval(exp.replace("fact(", "factorial("), SAFE_GLOBALS_local, {})
            # format result
            if isinstance(result, float):
                out = round(result, 12)  # reduce floating noise
            else:
                out = result
            self.entry_var.set(str(out))
            # add to history
            self.history.append((exp, out))
            self.history_list.insert(tk.END, f"{exp} = {out}")
            self.status.config(text="Calculado com sucesso")
        except Exception as e:
            messagebox.showerror("Erro", f"Expressão inválida:\n{e}")
            self.status.config(text="Erro ao calcular")

    # ---------------------------
    # History features
    # ---------------------------
    def on_history_select(self, event):
        sel = self.history_list.curselection()
        if not sel: return
        idx = sel[0]
        expr, res = self.history[idx]
        self.entry_var.set(str(expr))

    def show_history_popup(self):
        txt = "\n".join([f"{e} = {r}" for e, r in self.history[-30:]])
        messagebox.showinfo("Histórico (últimos 30)", txt or "Sem histórico")

    def clear_history(self):
        self.history.clear()
        self.history_list.delete(0, tk.END)
        self.status.config(text="Histórico limpo")

    def save_memory(self):
        # just example to show memory persistence prompt
        messagebox.showinfo("Memória", f"Valor em memória: {self.memory}")

    # ---------------------------
    # Keyboard bindings
    # ---------------------------
    def bind_keys(self):
        for key in "0123456789+-*/().%^":
            self.bind(f"<Key-{key}>", self.on_key)
        self.bind("<Return>", lambda e: self.on_button("="))
        self.bind("<BackSpace>", lambda e: self.on_button("<-"))
        self.bind("<Escape>", lambda e: self.on_button("C"))
        # other keys
        self.bind("<Key-s>", lambda e: self.on_button("sin("))
        self.bind("<Key-c>", lambda e: self.on_button("cos("))
        self.bind("<Key-t>", lambda e: self.on_button("tan("))
        # dot and comma
        self.bind("<Key-.>", lambda e: self.on_button("."))
        self.bind("<Key-comma>", lambda e: self.on_button("."))

    def on_key(self, event):
        # append typed character
        current = self.entry_var.get()
        self.entry_var.set(current + event.char)

# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
