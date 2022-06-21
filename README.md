# Currency Converter

This Python project provides a simple yet effective script for converting currencies using real-time exchange rates obtained from Floatrates.com. It is designed for those who need a quick way to calculate the exchange amount from one currency to another, enhancing financial planning, travel, and business transactions.

## Features

- Fetches real-time currency exchange rates from Floatrates.com.
- Caches fetched exchange rates for faster repeated access.
- Supports converting from any base currency to USD and EUR directly, and vice versa.
- Dynamic retrieval of exchange rates for currencies not initially cached.
- User-friendly, interactive console interface.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/currency-converter.git
```

2. Navigate to the cloned repository:

```
cd currency-converter
```

3. Create and activate a virtual environment:

```
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies using pip and the requirements.txt file:

```
pip install -r requirements.txt
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

Follow the on-screen prompts:

1. Enter the code of the base currency you are converting from (e.g., `USD`).
2. Enter the code of the target currency you want to convert to (e.g., `EUR`).
3. Enter the amount you want to convert.
4. The script will then either fetch the current exchange rate from its cache or load it from Floatrates.com, calculate the exchange, and display the result.

## How It Works

1. The script first prompts the user to input a base currency.
2. It checks if the target currency's rate is in the cache. If not, it fetches and caches it.
3. The user then inputs another currency and an amount to convert.
4. The script calculates the exchanged amount using the cached or fetched rate and displays it.

## License

This project is licensed under the [MIT License](LICENSE.txt).
