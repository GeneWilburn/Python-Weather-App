# Canadian Weather Console Script (Python)

## Overview

This project is a small, practical Python program that retrieves **current weather conditions for selected Canadian cities** and displays them in a clean, tabular, console-friendly format similar to Environment Canada reports.

It demonstrates:

- Using a **public weather API**
- Working with **Python virtual environments (venv)**
- Fetching and parsing **live JSON data**
- Applying **Canadian wind chill and humidex formulas**
- Formatting aligned console output
- Writing Python in a **structured, professional style**

The result is a reliable, readable command-line weather report suitable for learning, scripting, or daily use.

------

## What is OpenWeatherMap?

**OpenWeatherMap** is a global weather data service operated by a private company based in London, UK.

It provides:

- Current weather conditions
- Forecasts
- Historical data
- Air quality data

for cities worldwide via **HTTP-based APIs**.

Although OpenWeatherMap is not a government service, it aggregates data from many authoritative sources, including:

- National meteorological agencies (such as Environment Canada)
- Weather stations
- Satellites
- Numerical weather prediction models

In this project, OpenWeatherMap acts as a **convenient, stable access point** for Canadian weather data.

More information:
https://openweathermap.org/

------

## Why This Project Uses OpenWeatherMap

Originally, this project explored direct access to Environment Canada’s MSC Datamart and Sarracenia (AMQP) feeds. While powerful, those systems:

- Require additional infrastructure
- Are harder to configure
- Are less suitable for a small learning project

OpenWeatherMap was chosen because it:

- Uses simple HTTP requests
- Returns well-documented JSON
- Requires no message brokers
- Is stable and beginner-friendly
- Still provides Canadian weather data

This makes it ideal for a **clean, reproducible example**.

------

## Requirements

- Linux (tested on Linux Mint)
- Python 3.8 or newer
- Internet access
- An OpenWeatherMap API key (free)

------

## Getting an OpenWeatherMap API Key

1. Visit https://openweathermap.org/api
2. Create a free account
3. Generate an API key
4. Copy the key — you will place it in the script

------

## Project Structure

```text
weather/
├── current_weather.py
├── requirements.txt
├── README.md
└── venv/
```

------

## Why Use a Virtual Environment (venv)?

Linux distributions rely on Python for system tools. Installing packages globally can break the system.

A **virtual environment (venv)**:

- Isolates project dependencies
- Prevents system breakage
- Allows reproducible setups
- Is considered best practice

------

## Creating and Activating the Virtual Environment

```bash
cd ~/weather
python3 -m venv venv
source venv/bin/activate
```

Your prompt will change to:

```text
(venv) user@machine:~/weather$
```

------

## Installing Dependencies

Only one external package is required:

```bash
pip install requests
```

Optionally save dependencies:

```bash
pip freeze > requirements.txt
```

------

## Running the Script

With the venv activated:

```bash
python current_weather.py
```

Or without activating:

```bash
~/weather/venv/bin/python ~/weather/current_weather.py
```

------

## City Names and Country Codes

City names are **not globally unique**. For example:

- London exists in Canada, the UK, and the USA
- Paris exists in France and the USA

For this reason, OpenWeatherMap requires a **country code**:

```text
Toronto,CA
London,CA
Paris,FR
```

Canada uses the ISO country code **CA**.

Some cities require full spelling:

- ❌ `St Catharines,CA`
- ✅ `Saint Catharines,CA`

For maximum reliability, OpenWeatherMap also supports **city IDs**, which uniquely identify locations.

------

## Wind Chill and Humidex

This script calculates:

- **Wind Chill** when:
  - Temperature ≤ 10 °C
  - Wind speed ≥ 4.8 km/h
- **Humidex** when:
  - Temperature ≥ 20 °C

Both calculations use **standard Canadian formulas**, not values supplied by the API.

------

## Script Design Notes

The script is written in a **structured Python style**:

- Helper functions (`get_weather`, `wind_chill`, `humidex`)
- A dedicated `main()` function
- A `__name__ == "__main__"` guard

This allows the script to be:

- Reusable
- Testable
- Importable
- Easy to extend

This is standard practice in professional Python programming.

------

## Sample Output

```text
Observation Time: 2026-01-02 14:30:00

City            | Temp  | Conditions           | RH   | Wind (km/h)| Feels Like
-------------------------------------------------------------------------------------
Vancouver, CA   |   6°C | Light Rain           |  92% |    7.2     |
Toronto, CA     |  -3°C | Overcast Clouds      |  71% |   14.8     | Wind Chill  -9°C
Winnipeg, CA    | -18°C | Clear Sky            |  61% |   21.2     | Wind Chill -29°C
Calgary, CA     |  22°C | Mostly Sunny         |  34% |    9.0     | Humidex     26°C
```

------

## Replicating This Setup on Another System

Copy the project **without the venv**:

```bash
rsync -av --exclude venv weather/ othermachine:~/weather/
```

Then recreate the venv and reinstall dependencies on the new system.

------

## Closing Notes

This project emphasizes:

- Clarity over cleverness
- Correctness over complexity
- Reproducibility over shortcuts

It is intended as both a **useful tool** and a **learning example** for Python, APIs, and Linux-based workflows.

## License

This project is licensed under the **MIT License**.

You are free to:

- Use this software for any purpose
- Modify it
- Distribute it
- Include it in other projects

The only requirement is that the original copyright notice
and license text be included in any substantial portions of
the software.

### MIT License Text

Copyright (c) 2026 Gene Wilburn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.