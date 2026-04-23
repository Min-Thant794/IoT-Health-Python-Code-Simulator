# 🏥 IoT Health Python Code Simulator

A Python-based IoT health monitoring simulator that continuously generates and tracks patient vital signs, streams data to **Microsoft Azure IoT Hub**, triggers real-time alerts for abnormal readings, and visualises the data through a **Microsoft Power BI** live dashboard. Built as part of an IoT coursework project.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Health Metrics Monitored](#health-metrics-monitored)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Simulator](#running-the-simulator)
- [How It Works](#how-it-works)
- [Alert Thresholds](#alert-thresholds)
- [Project Structure](#project-structure)
- [Coursework Context](#coursework-context)

---

## Overview

This simulator mimics the behaviour of IoT-connected health sensors placed on a patient. It generates realistic vital sign readings at regular intervals, prints live data to the console, streams the data to **Microsoft Azure IoT Hub**, raises alerts when values fall outside safe ranges, and visualises the data in a live **Microsoft Power BI** dashboard — all without requiring any physical hardware.

---

## ✨ Features

- 🔄 **Continuous data simulation** — generates sensor readings at configurable intervals
- 🖥️ **Console output** — prints formatted vital sign readings in real time
- ☁️ **Azure IoT Hub integration** — streams simulated sensor data to the cloud in real time
- 🚨 **Smart alerting** — automatically flags readings that exceed safe thresholds
- 📊 **Power BI live dashboard** — visualises real-time vitals through a connected Microsoft Power BI report
- 🧪 **No hardware required** — runs entirely in software as a code simulator

---

## 💓 Health Metrics Monitored

| Metric | Unit | Normal Range |
|---|---|---|
| Heart Rate | bpm | 60 – 100 bpm |
| Blood Pressure (Systolic) | mmHg | 90 – 120 mmHg |
| Blood Pressure (Diastolic) | mmHg | 60 – 80 mmHg |
| SpO₂ (Oxygen Saturation) | % | 95 – 100% |
| Body Temperature | °C | 36.1 – 37.2 °C |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- [Microsoft Azure](https://portal.azure.com/) account with an **IoT Hub** resource provisioned
- [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) — for the live dashboard

> Other dependencies (if any) can be found in `requirements.txt`.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Min-Thant794/IoT-Health-Python-Code-Simulator.git
```

2. Navigate into the project directory:

```bash
cd IoT-Health-Python-Code-Simulator
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Simulator

```bash
python main.py
```

The simulator will begin generating vital sign readings, printing them to the console, streaming them to Azure IoT Hub, raising alerts for abnormal values, and feeding the live Power BI dashboard.

---

## ⚙️ How It Works

1. **Data Generation** — Each sensor reading is simulated using randomised values within realistic physiological ranges, with occasional spikes to trigger alert conditions.
2. **Console Output** — Each reading cycle prints a timestamped summary of all four metrics to the terminal.
3. **Azure IoT Hub** — Readings are sent as telemetry messages to a configured **Microsoft Azure IoT Hub**, simulating a real IoT device publishing to the cloud.
4. **Alert System** — After each reading, values are compared against predefined safe thresholds. If any metric is out of range, a warning message is printed to the console.
5. **Power BI Dashboard** — Azure streams the data into a **Microsoft Power BI** report, where live charts display the history of each metric over time, making trends easy to monitor at a glance.

---

## 🚨 Alert Thresholds

Alerts are triggered when readings fall outside these bounds:

| Metric | Low Alert | High Alert |
|---|---|---|
| Heart Rate | < 60 bpm | > 100 bpm |
| Systolic BP | < 90 mmHg | > 120 mmHg |
| SpO₂ | < 95% | — |
| Body Temperature | < 36.1 °C | > 37.5 °C |

---

## 📁 Project Structure

```
IoT-Health-Python-Code-Simulator/
│
├── main.py               # Entry point — runs the simulator loop
├── sensors.py            # Simulated sensor data generation logic
├── alerts.py             # Alert threshold checking and notifications
├── requirements.txt      # Python dependencies
├── dashboard.pbix        # Microsoft Power BI dashboard file
└── README.md             # Project documentation
```

> Note: File names may vary slightly — refer to the actual repository contents.

---

## 🎓 Coursework Context

This project was developed as part of an **IoT (Internet of Things)** coursework assignment. The goal was to demonstrate understanding of:

- IoT sensor data simulation and real-time processing
- Cloud connectivity using **Microsoft Azure IoT Hub** for telemetry ingestion
- Threshold-based alerting systems common in healthcare IoT
- Data visualisation using **Microsoft Power BI** for real-time health monitoring dashboards
- Python as a rapid prototyping tool for IoT applications

---

## 📄 License

This project is submitted for academic purposes. Please do not plagiarise.
