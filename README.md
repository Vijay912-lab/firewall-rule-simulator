#  Firewall Log Analyzer

A lightweight Python project that simulates real-world firewall log analysis. Built as part of a cybersecurity coursework assignment, this tool reads CSV-based firewall logs, parses network events, and detects unusual activity or policy violations.

## Features

- Parses and analyzes CSV firewall log data
- Detects suspicious patterns or blacklisted IPs
- Identifies blocked vs allowed traffic
- Includes unit tests for log analyzer functionality
- Demo video included for visual walkthrough

##  Learning Outcomes

- Gained hands-on experience working with firewall logs
- Learned how to simulate packet inspection and rule enforcement
- Practiced defensive programming and unit testing in Python

##  Project Structure

```bash
Firewall/
├── index.py                  # Main script
├── log_analyzer.py          # Core logic for analyzing logs
├── test_log_analyzer.py     # Unit tests for the analyzer
├── firewall_logs_2022.csv   # Sample log data for testing
└── firewall assignment demo .mov  # Demo walkthrough video

## How to run the project
git clone https://github.com/YOUR_USERNAME/firewall-log-analyzer.git
cd firewall-log-analyzer/Firewall
python3 index.py

## Use these comments to see the results
python3 index.py --filename firewall_logs_2022.csv --action head
python3 index.py --filename firewall_logs_2022.csv --action deny
python3 index.py --filename firewall_logs_2022.csv --action source --country US
python3 index.py --filename firewall_logs_2022.csv --action source --country XX
python3 index.py --filename firewall_logs_2022.csv --action count 
python3 index.py --filename firewall_logs_2022.csv --action parse --month 11

------------------------------------------------------------------------------END------------------------------------------------------------------------------
 
