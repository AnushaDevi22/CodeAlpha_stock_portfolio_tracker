# CodeAlpha_stock_portfolio_tracker

# Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker developed as part of the **CodeAlpha Python Programming Internship**.

## 📌 Project Description

The Stock Portfolio Tracker allows users to manage their stock investments by selecting stocks from a predefined list, entering the quantity, calculating the investment amount, viewing their portfolio, and saving the portfolio details to a text file.

## ✨ Features

* View available stocks and their prices
* Add stocks to the portfolio
* Enter the quantity of each stock
* Automatically calculate investment for each stock
* View complete portfolio
* Calculate total investment
* Validate stock names
* Validate stock quantity
* Save portfolio details to `portfolio.txt`
* Menu-driven console interface

## 🛠️ Technologies Used

* Python
* Python Dictionaries
* Python Lists
* Functions
* Loops
* Conditional Statements
* File Handling

## 📂 Project Structure

```text
CodeAlpha_Task2_Stock_Portfolio_Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python stock_portfolio_tracker.py
```

5. Use the menu to add stocks, view the portfolio, save the portfolio, or exit.

## 📊 Available Stocks

The project currently uses predefined sample stock prices:

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| MSFT  |  $400 |
| GOOGL |  $150 |
| AMZN  |  $180 |

> Note: These are predefined sample prices for the project and are not live market prices.

## 🧮 Calculation

The investment for each stock is calculated using:

```text
Investment = Stock Price × Quantity
```

For example:

```text
AAPL price = $180
Quantity = 3

Investment = $180 × 3
           = $540
```

## 💾 File Storage

When the user selects **Save Portfolio**, the application creates or updates:

```text
portfolio.txt
```

The file contains the selected stocks, quantities, prices, individual investments, and total investment.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python data structures
* User input handling
* Input validation
* Functions
* Loops and conditions
* Basic calculations
* File handling
* Building a menu-driven console application

## 👩‍💻 Author

**Anusha Devi Gali**

GitHub: [AnushaDevi22](https://github.com/AnushaDevi22)
