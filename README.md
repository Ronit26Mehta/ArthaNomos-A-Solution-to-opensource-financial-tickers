
# ArthaNomos: A Scalable Open-Source Financial Ticker API

ArthaNomos is a groundbreaking open-source solution that fetches and processes over **350,000 financial tickers** across seven asset classes for public use. The system integrates data from sources such as Yahoo Finance, dramatically reducing data acquisition time from 24 hours to under 45 minutes through innovative optimizations, parallelization, and asynchronous processing.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture and Design](#system-architecture-and-design)
- [Optimization Strategies](#optimization-strategies)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Research Paper](#research-paper)
- [Performance Metrics](#performance-metrics)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

ArthaNomos is designed to provide comprehensive and fast access to a vast dataset of financial tickers. By leveraging the [yfinance](https://github.com/ranaroussi/yfinance) library along with custom pagination and asynchronous techniques, the system efficiently processes tickers across equities, mutual funds, cryptocurrencies, currencies, indices, futures, and ETFs. The solution is publicly available via a web portal and API endpoints, empowering researchers, traders, and developers with extensive financial data.

---

## Features

- **Massive Data Coverage:** Aggregates over 350k financial tickers.
- **Multi-Asset Support:** Equities, Mutual Funds, Cryptocurrencies, Currencies, Indices, Futures, and ETFs.
- **Optimized Performance:** Reduced data acquisition time from 24 hours to 45 minutes.
- **RESTful API Endpoints:** Each asset class is accessible through dedicated API routes.
- **Responsive Web Interface:** Built with Flask and Bootstrap for an engaging user experience.
- **Detailed Logging and Monitoring:** Tracks successful and failed ticker fetches.
- **Scalable Design:** Modular system architecture supports future enhancements and integration of additional data sources.

---

## System Architecture and Design

The system is built around the **yfinance** library and employs a paginated data fetching mechanism. Its core components include:

1. **Data Acquisition Module:** Uses a modified screener to request data for each exchange with pagination.
2. **Data Aggregation and Storage:** Aggregates ticker data and saves it to CSV files (or a database) per asset class.
3. **Performance Monitoring:** Measures execution time and logs unique, successful, and failed tickers.
4. **API Gateway and Front-End UI:** Provides public access via RESTful API endpoints and a responsive web interface.

### High-Level System Architecture

Below is a vertically arranged, compact system architecture diagram (generated using TikZ in the research paper):

_For a detailed TikZ diagram, please refer to the LaTeX source in the research paper._

---

## Optimization Strategies

ArthaNomos evolved through several optimization phases:

1. **Initial Approach (24 Hours):** Synchronous data retrieval across exchanges.
2. **Phase I Optimization (4 Hours):** Improved pagination logic reduced redundant API calls.
3. **Phase II Optimization (45 Minutes):** Implemented asynchronous processing, parallel data fetching, and enhanced caching to minimize runtime.

### Pseudo Code Outline

```latex
Procedure FetchData(exchanges, page_size, max_offset):
    Initialize total_symbols as an empty set
    For each exchange in exchanges:
        offset ← 0
        zeroCount ← 0
        While offset < max_offset:
            Build requestBody with current exchange and offset
            response ← AsyncFetch(requestBody)
            If response is empty:
                Break
            For each symbol in response.quotes:
                If symbol not in total_symbols:
                    Add symbol to total_symbols
                    zeroCount ← 0
                Else:
                    Increment zeroCount
            offset ← offset + page_size
            If zeroCount ≥ threshold:
                Break
        Save detailed data to CSV for exchange
    Save total_symbols summary
End Procedure
```

---

## Installation and Setup

### Prerequisites

- Python 3.11 or higher
- [pip](https://pip.pypa.io/)
- Virtual environment tool (e.g., `venv`)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/arthanomos.git
   cd arthanomos
   ```

2. **Create and Activate a Virtual Environment**

   On macOS/Linux:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
   On Windows:
   ```cmd
   py -3.11 -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables (if needed)**

   Create a `.env` file with your configurations.

5. **Run the Application**

   ```bash
   python app.py
   ```

6. **Access the Web Interface**

   Open your browser and navigate to: [https://arthanomos-a-solution-to-opensource.onrender.com](https://arthanomos-a-solution-to-opensource.onrender.com)

---

## Usage

The system offers both a web UI and RESTful API endpoints for accessing financial ticker data.

- **Web Interface:** Provides a multi-page UI for equities, mutual funds, cryptocurrencies, currencies, indices, futures, ETFs, and a research paper download page.
- **API Endpoints:** Use endpoints such as `/api/equity`, `/api/mutualfund`, `/api/crypto`, `/api/currency`, `/api/indices`, `/api/futures`, and `/api/etf` to retrieve JSON data.

Example API call:
```bash
curl "https://arthanomos-a-solution-to-opensource.onrender.com/api/equity?exchange=NASDAQ"
```

---

## Research Paper

For a detailed discussion on system design, optimization methodologies, performance metrics, and future enhancements, please refer to the research paper available at:

[https://arthanomos-a-solution-to-opensource.onrender.com/research](https://arthanomos-a-solution-to-opensource.onrender.com/research)

---

## Performance Metrics

The system performance improved dramatically through iterative optimizations:

| **Method**              | **Runtime**  | **Unique Symbols** | **Failure Rate** |
|-------------------------|--------------|--------------------|------------------|
| Initial Approach        | 24 hours     | 350k+              | High             |
| Phase I Optimization    | 4 hours      | 350k+              | Medium           |
| Phase II Optimization   | 45 minutes   | 350k+              | Low              |

A sample runtime improvement chart is included in the research paper.

---

## Future Enhancements

Potential improvements to the system include:
- **Enhanced Parallelism:** Using distributed computing frameworks (e.g., Apache Spark).
- **Data Enrichment:** Integrating additional financial and fundamental data sources.
- **Robust Caching:** Implementing advanced caching strategies for near real-time updates.
- **API Gateway Improvements:** Designing a more secure and scalable public API.
- **User Feedback Integration:** Gathering user input for continuous improvement.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

For any major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

We thank the financial data research community and the contributors to open-source libraries such as [yfinance](https://github.com/ranaroussi/yfinance) and [pandas](https://github.com/pandas-dev/pandas) for making this project possible.

---

**ArthaNomos** aims to provide a reliable, scalable, and fast access to financial ticker data for both academic research and practical applications, paving the way for further innovation in financial data systems.
```

