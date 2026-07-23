# Da Vinci

An interactive desktop application for vector drawing and digital whiteboard built with Python and Tkinter, designed to serve as a practical tool for artistic expression and an interactive virtual whiteboard for educational purposes.

**Da Vinci** was developed as the final term project for the **Programação A** (Programming A) course in the **Computer Science** program at **Universidade Federal de Sergipe (UFS)**. The project was conceived as a practical exercise in applying **Object-Oriented Programming (OOP)** principles, **SOLID** design principles, and the **MVC (Model-View-Controller)** architectural pattern to a reactive desktop interface.

---

## 🎨 Features

### 🖌️ Creation Tools
* **Primitive Geometric Shapes:** Rectangles, Squares, Circles, Ovals, Lines, and Right Triangles.
* **Complex Shapes:** Custom Irregular Polygons defined by the user.
* **Freehand Drawing & Eraser:** Freehand scribble tool with adjustable stroke width and an eraser tool to remove canvas elements.

### ✂️ Selection & Manipulation
* **Object Selection:** Dedicated tool for selecting shapes on the canvas.
* **Move & Reposition:** Click and drag to dynamically move and reposition any graphical element.
* **Dynamic Styling:** Edit stroke (border) colors and fill colors for selected objects.
* **Stroke Width Adjustment:** Change pencil and outline thickness on the fly.

### 🔄 Canvas Management & History
* **Undo / Redo:** Step through action history for quick experimentation and error correction.
* **Clear Canvas:** Reset the entire workspace with a single action.
* **Data Persistence:** Save project state to disk and load previously saved drawings from the saves directory.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **GUI Toolkit:** Tkinter (Python's native GUI library)
* **Architecture:** MVC (Model-View-Controller)
* **Persistence:** Built-in Python serialization and file management modules
* **Dependencies:** **Zero third-party libraries.** Built entirely on the Python standard library.

---

## 📂 Project Structure

The codebase enforces a strict separation of concerns following the **MVC** architecture pattern:

```text
Projeto-PA/
├── controller/                 # Controller layer (wires views to models & handles events)
│   ├── ferramentas/            # Tool-specific controllers
│   │   ├── __init__.py
│   │   ├── borracha_ferramenta.py
│   │   ├── circulo_ferramenta.py
│   │   ├── ferramenta.py       # Abstract Base Class for tools
│   │   ├── linha_ferramenta.py
│   │   ├── oval_ferramenta.py
│   │   ├── poligono_ferramenta.py
│   │   ├── quadrado_ferramenta.py
│   │   ├── rabisco_ferramenta.py
│   │   ├── retangulo_ferramenta.py
│   │   ├── selecao_ferramenta.py
│   │   └── triangulo_reto_ferramenta.py
│   ├── __init__.py
│   ├── controlador_selecao.py
│   └── controlador.py         # Central application state controller
├── model/                      # Model layer (business logic & data structures)
│   ├── figuras/                # Shape logic and definitions
│   │   ├── __init__.py
│   │   ├── borracha.py
│   │   ├── circulo.py
│   │   ├── figuras.py          # Base class for graphical shapes
│   │   ├── linha.py
│   │   ├── oval.py
│   │   ├── poligono.py
│   │   ├── quadrado.py
│   │   ├── rabisco.py
│   │   ├── retangulo.py
│   │   ├── selecao.py
│   │   └── triangulo_reto.py
│   ├── desenho.py             # Canvas/workspace state container
│   ├── geometria.py           # Geometry helpers and math utilities
│   └── persistencia.py        # File save/load operations
├── view/                       # View layer (Tkinter rendering only)
│   ├── __init__.py
│   ├── view_canvas.py         # Drawing canvas & interaction area
│   ├── view_interface.py      # Main GUI layout & toolbars
│   └── view_menu_arquivo.py   # Dropdown file menus (Save, Load, Exit)
├── salvamentos/                # Directory reserved for saved workspace files
├── main.py                     # Main application entry point
└── README.md
```

## 🚀 Getting Started

```bash
git clone [https://github.com/MichaelCarvalhoUFS/Da-vinci.git]
cd Da Vinci
python main.py
```

> Note: Always launch the command from the root directory (Projeto-PA) to ensure module resolutions across controller, model, and view packages function correctly.

## Keyboard shortcuts

| Shortcut         | Action                          |
|-------------------|----------------------------------|
| `Delete` / `Backspace` | Delete the selected shape(s) |
| `Ctrl+C` / `Ctrl+V`    | Copy / paste the selected shape(s) |
| `Ctrl+Z` / `Ctrl+Y`    | Undo / Redo |
| `Ctrl-p` | Open menu save |

## 👥 Developers
### Designed and built by Computer Science undergraduate students at Universidade Federal de Sergipe (UFS), São Cristóvão campus:

* **José Michael Carvalho**

* **Max Willian Rocha Martins**

* **Pedro Henrique Chaves Rodrigues Mota**