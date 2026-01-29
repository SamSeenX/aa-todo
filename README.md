# AA Todo

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-blue.svg)]()

> A simple, persistent command-line to-do list application for managing daily tasks.

AA Todo is a lightweight Python-based CLI tool designed to help you track your tasks without leaving the terminal. It uses a local JSON file for persistence, ensuring your tasks are saved between sessions.

## ✨ Features

- 📝 **Add Tasks** - Quickly append new items to your list.
- 📋 **List View** - View all pending and completed tasks at a glance.
- ✅ **Mark as Done** - Easily complete tasks by their ID.
- 💾 **Persistence** - Automatically saves data to `todos.json`.

## 🚀 Quick Start

### Prerequisites

- Python 3.x

### Installation

```bash
# Clone the repository
git clone https://github.com/SamSeenX/aa-todo.git
cd aa-todo

# No external dependencies required (uses standard library)
```

### Basic Usage

Run the application:

```bash
python app.py
```

Follow the on-screen menu to manage your tasks:

1. Add Task
2. List Tasks
3. Mark Task as Done
4. Exit

## 🏗️ Project Structure

```
aa-todo/
├── app.py            # Main application logic
├── todos.json        # Data storage (auto-generated)
└── README.md
```

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/SamSeenX/aa-todo.git
cd aa-todo
```

### Running

```bash
python app.py
```

## 🗺️ Roadmap

- [ ] Add ability to delete tasks
- [ ] Add due dates
- [ ] Add priority levels
- [x] Basic persistence

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ☕ Support

If you find this project useful, please consider supporting me:

- ⭐ Starring this repository
- 🐛 Reporting issues
- ☕ [Buy me a coffee](https://buymeacoffee.com/samseen)

---

Created with ❤️ by [SamSeen](https://buymeacoffee.com/samseen)