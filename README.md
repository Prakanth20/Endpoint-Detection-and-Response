# 🛡️ Python EDR (Endpoint Detection and Response)

A lightweight and extensible Python-based Endpoint Detection and Response (EDR) tool for monitoring file system changes and process activity in real time. Designed for educational and research use on Windows, macOS, and Linux.

---

## 📦 Features

### 🗂 File System Monitoring

* Watches the user's home directory (platform-independent).
* Logs:

  * File creation
  * File modification (with SHA-256 hash)
  * File deletion

### 🧠 Process Monitoring

* Tracks:

  * Process starts (includes PID, name, path, and command line)
  * Process terminations

### 📝 JSON Event Logging

* Logs events to a human- and machine-readable `edr_log.json` file.
* Includes timestamps and event types for easy correlation.

### ✉️ Optional: Email Alerts (via SMTP)

* Send real-time email alerts on suspicious activities (configurable).

### 🖥 Optional: GUI Dashboard (Tkinter)

* View live logs in a simple graphical interface.

---

## 🧰 Requirements

* Python 3.6 or later
* OS: Windows, macOS, or Linux

### Python Dependencies

Install with:

```bash
pip install psutil watchdog
```

For optional features:

```bash
pip install tk  # for GUI (Tkinter is built-in on most Python installations)
```

---

## ▶️ Getting Started

### Run the EDR:

```bash
python edr.py
```

To stop monitoring:

```bash
Ctrl + C
```

---

## 📁 Log Format

Logs are written to `edr_log.json`. Example entry:

```json
{
  "event_type": "process_started",
  "timestamp": "Sat Jun 7 14:30:15 2025",
  "data": {
    "pid": 1234,
    "name": "notepad.exe",
    "exe": "C:\\Windows\\System32\\notepad.exe",
    "cmdline": ["notepad.exe"]
  }
}
```

---

## ⚠️ Disclaimer

This tool is designed **for educational purposes only**. It does **not provide active protection**, real-time threat intelligence, or automatic remediation. **Use responsibly and do not deploy in production environments.**

---
