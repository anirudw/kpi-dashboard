# Retail KPI Dashboard

A comprehensive Streamlit-based analytics dashboard for visualizing key performance indicators (KPIs) from retail sales data.

![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.5+-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue)

## Overview

The **Retail KPI Dashboard** provides interactive visualizations of critical business metrics derived from the [Online Retail II Dataset (2010-2011)](https://www.kaggle.com/datasets/fabiendaniels/online-retail-ii-data-set-from-ml-repository). This dashboard enables business analysts and stakeholders to monitor:

- **Revenue Performance** - Monthly revenue trends with month-over-month growth analysis
- **Customer Insights** - Top 10 customers by total revenue
- **Churn Analysis** - Customer retention metrics and churn rate visualization

## Architecture

```txt
kpi-dashboard/
├── app.py                         # Main Streamlit application entry point
├── requirements.txt               # Python dependencies
├── data/                          # Data layer
│   ├── connection.py             # PostgreSQL database connection
│   ├── querries.py               # SQL query definitions
│   ├── processing.py             # Data transformation and processing
│   └── data_loader.py            # Cached data loading utilities
├── loader/                        # Database loader
│   └── db_loader.py              # CSV to PostgreSQL ETL script
└── visualisation/                 # Visualization modules
    ├── month_over_month_vis.py   # MoM revenue growth charts
    ├── churned_comp_vis.py       # Customer churn visualization
    └── top_ten_vis.py             # Top customers bar chart
```

### Visualizations

- **Month-over-Month Growth** - Dual-axis chart showing monthly revenue (bar) and growth percentage (line)
- **Top 10 Customers** - Horizontal bar chart highlighting highest-revenue customers
- **Churn Distribution** - Categorical bar chart showing churned vs. active customers

## 🛠️ Prerequisites

### Required Software

- **Python** 3.10 or higher
- **PostgreSQL** 14 or higher

### Python Dependencies

All dependencies are listed in [`requirements.txt`](requirements.txt):

```txt
streamlit          # Web application framework
pandas             # Data manipulation and analysis
matplotlib         # Plotting library
seaborn            # Statistical data visualization
psycopg2           # PostgreSQL adapter
sqlalchemy         # SQL toolkit and ORM
python-dotenv      # Environment variable management
```

## How to run this?

1. **Clone the repository**

   ```bash

   git clone <repository-url>
   cd kpi-dashboard
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database connection**

   Create a `.env` file in the project root:

   ```env
   DB_USER=your_postgres_user
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=retail_kpi_db
   ```

5. **Initialize the database**

   Ensure your PostgreSQL database contains the required tables (`mom_percent`, `customer_profile`, `customer_churn`). Use the loader script to populate data:

   ```bash
   python loader/db_loader.py
   ```


Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in the default browser at `http://localhost:8501`.

## Acknowledgments

- Dataset originally from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- Built with [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/)
