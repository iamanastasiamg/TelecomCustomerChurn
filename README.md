# Telecom Customer Churn 🚀

## Table of Contents 📑
- [Description](#Description) ✨
- [Features](#Features) ⬇️
- [Installation](#Installation) 🛠️
- [Prerequisites](#Prerequisites) 📦
- [Steps](#Steps) 📝
- [Usage](#Usage) 💻

## Description ✨

This dataset comes from an Iranian telecom company, with each row representing a customer over a year period. Along with a churn label, there is information on the customers' activity, such as call failures and subscription length.

## Features ⬇️

| Feature                   | Explanation                      
|---------------------------|-------------------------------
| Call Failure              | number of call failures
| Complaints                | binary (0: No complaint, 1: complaint)
| Subscription Length       |	total months of subscription
| Charge Amount             | ordinal attribute (0: lowest amount, 9: highest amount)
| Seconds of Use            | total seconds of calls
| Frequency of use          | total number of calls
| Frequency of SMS          | total number of text messages
| Distinct Called Numbers   | total number of distinct phone calls
| Age Group                 | ordinal attribute (1: younger age, 5: older age)
| Tariff Plan               | binary (1: Pay as you go, 2: contractual)
| Status                    | binary (1: active, 2: non-active)
| Age                       | age of customer
| Customer Value            | the calculated value of customer
| Churn                     | class label (1: churn, 0: non-churn)

## Installation ⚙️
pip install -r requirements.txt

### Prerequisites 📦
- Python

### Steps 📝
1. Clone the repository: `git clone https://github.com/iamanastasiamg/TelecomCustomerChurn.git`
2. Install dependencies: `npm install`
3. Run the project: `npm start`

## Usage 💻
```bash
node index.js

Example:
```bash
git clone https://github.com/iamanastasiamg/TelecomCustomerChurn.git
cd project-name
npm install
