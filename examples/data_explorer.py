"""
Streamlit++ Sample Project - Data Explorer

An interactive data exploration application demonstrating advanced UI components,
forms, and data visualization capabilities.
"""

import streamlit as st
import streamlit_plus as stp
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import time

# Page configuration
st.set_page_config(
    page_title="Data Explorer - Streamlit++",
    page_icon="🔍",
    layout="wide"
)

# Custom theme
theme = stp.custom_theme(colors={
    "primary": "#059669",
    "secondary": "#7c3aed",
    "success": "#10b981",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "info": "#06b6d4"
})
stp.set_theme(theme)

# Generate sample datasets
@st.cache_data
def load_datasets():
    np.random.seed(42)

    # E-commerce dataset
    customers = pd.DataFrame({
        'customer_id': range(1, 1001),
        'name': [f'Customer {i}' for i in range(1, 1001)],
        'email': [f'customer{i}@example.com' for i in range(1, 1001)],
        'age': np.random.normal(35, 12, 1000).astype(int),
        'gender': np.random.choice(['Male', 'Female', 'Other'], 1000),
        'location': np.random.choice(['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix', 'Seattle'], 1000),
        'signup_date': pd.date_range('2020-01-01', periods=1000, freq='D'),
        'total_spent': np.random.exponential(500, 1000).round(2),
        'orders_count': np.random.poisson(5, 1000),
        'loyalty_tier': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 1000, p=[0.5, 0.3, 0.15, 0.05])
    })

    # Product dataset
    products = pd.DataFrame({
        'product_id': range(1, 201),
        'name': [f'Product {i}' for i in range(1, 201)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Beauty'], 200),
        'brand': np.random.choice(['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E'], 200),
        'price': np.random.uniform(10, 1000, 200).round(2),
        'rating': np.random.uniform(1, 5, 200).round(1),
        'reviews_count': np.random.poisson(50, 200),
        'stock_quantity': np.random.randint(0, 500, 200),
        'is_available': np.random.choice([True, False], 200, p=[0.9, 0.1])
    })

    # Sales transactions
    dates = pd.date_range('2024-01-01', periods=365, freq='D')
    transactions = pd.DataFrame({
        'transaction_id': range(1, 5001),
        'customer_id': np.random.choice(customers['customer_id'], 5000),
        'product_id': np.random.choice(products['product_id'], 5000),
        'date': np.random.choice(dates, 5000),
        'quantity': np.random.poisson(2, 5000),
        'unit_price': np.random.uniform(10, 1000, 5000).round(2),
        'total_amount': lambda x: x['quantity'] * x['unit_price'],
        'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer', 'Cash'], 5000),
        'status': np.random.choice(['Completed', 'Pending', 'Cancelled'], 5000, p=[0.85, 0.1, 0.05])
    })
    transactions['total_amount'] = transactions['quantity'] * transactions['unit_price']

    return customers, products, transactions

# Advanced filter form
def advanced_filters():
    st.sidebar.header("🔍 Advanced Filters")

    with st.sidebar.expander("Customer Filters", expanded=True):
        age_range = st.slider("Age Range", 18, 80, (25, 55))
        gender_filter = st.multiselect("Gender", ['Male', 'Female', 'Other'], default=['Male', 'Female'])
        location_filter = st.multiselect("Location", ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix', 'Seattle'])
        loyalty_filter = st.multiselect("Loyalty Tier", ['Bronze', 'Silver', 'Gold', 'Platinum'])

    with st.sidebar.expander("Product Filters"):
        category_filter = st.multiselect("Category", ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Beauty'])
        price_range = st.slider("Price Range", 0.0, 1000.0, (0.0, 500.0))
        rating_filter = st.slider("Minimum Rating", 1.0, 5.0, 3.0)
        brand_filter = st.multiselect("Brand", ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E'])

    with st.sidebar.expander("Transaction Filters"):
        date_range = st.date_input("Date Range", [datetime.now() - timedelta(days=90), datetime.now()])
        amount_range = st.slider("Transaction Amount", 0.0, 5000.0, (0.0, 1000.0))
        status_filter = st.multiselect("Status", ['Completed', 'Pending', 'Cancelled'], default=['Completed'])
        payment_filter = st.multiselect("Payment Method", ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash'])

    return {
        'age_range': age_range,
        'gender_filter': gender_filter,
        'location_filter': location_filter,
        'loyalty_filter': loyalty_filter,
        'category_filter': category_filter,
        'price_range': price_range,
        'rating_filter': rating_filter,
        'brand_filter': brand_filter,
        'date_range': date_range,
        'amount_range': amount_range,
        'status_filter': status_filter,
        'payment_filter': payment_filter
    }

# Data overview dashboard
def data_overview(customers, products, transactions, filters):
    st.title("📊 Data Explorer Dashboard")

    # Apply filters
    filtered_customers = customers[
        (customers['age'].between(*filters['age_range'])) &
        (customers['gender'].isin(filters['gender_filter'])) &
        (customers['location'].isin(filters['location_filter']) if filters['location_filter'] else True) &
        (customers['loyalty_tier'].isin(filters['loyalty_filter']) if filters['loyalty_filter'] else True)
    ]

    filtered_products = products[
        (products['category'].isin(filters['category_filter']) if filters['category_filter'] else True) &
        (products['price'].between(*filters['price_range'])) &
        (products['rating'] >= filters['rating_filter']) &
        (products['brand'].isin(filters['brand_filter']) if filters['brand_filter'] else True)
    ]

    filtered_transactions = transactions[
        (transactions['date'].between(*filters['date_range'])) &
        (transactions['total_amount'].between(*filters['amount_range'])) &
        (transactions['status'].isin(filters['status_filter'])) &
        (transactions['payment_method'].isin(filters['payment_filter']))
    ]

    # KPI Cards
    kpis = [
        {
            "title": "Total Customers",
            "value": f"{len(filtered_customers):,}",
            "delta": 8.2,
            "icon": "👥"
        },
        {
            "title": "Active Products",
            "value": f"{len(filtered_products):,}",
            "delta": 3.1,
            "icon": "📦"
        },
        {
            "title": "Total Transactions",
            "value": f"{len(filtered_transactions):,}",
            "delta": 12.5,
            "icon": "💳"
        },
        {
            "title": "Revenue",
            "value": f"${filtered_transactions['total_amount'].sum():,.0f}",
            "delta": 15.3,
            "icon": "💰"
        }
    ]

    stp.kpi_dashboard(kpis, columns=4)

    # Main content grid
    container_id = stp.css_grid_layout("""
        grid-template-areas:
            'summary charts'
            'details details';
        grid-template-columns: 400px 1fr;
        grid-template-rows: 300px 400px;
        gap: 2rem;
    """)

    # Summary statistics
    stp.grid_item(container_id, "summary", lambda: (
        st.subheader("📈 Summary Statistics"),
        summary_data := pd.DataFrame({
            'Metric': ['Avg Customer Age', 'Avg Product Price', 'Avg Transaction Value', 'Total Revenue'],
            'Value': [
                f"{filtered_customers['age'].mean():.1f} years",
                f"${filtered_products['price'].mean():.2f}",
                f"${filtered_transactions['total_amount'].mean():.2f}",
                f"${filtered_transactions['total_amount'].sum():,.0f}"
            ]
        }),
        st.dataframe(summary_data, use_container_width=True)
    ))

    # Charts area
    def charts_content():
        col1, col2 = st.columns(2)
        col1.subheader("Customer Distribution")
        customer_dist = filtered_customers['loyalty_tier'].value_counts().reset_index()
        customer_dist.columns = ['Tier', 'Count']
        col1.bar_chart(customer_dist.set_index('Tier'))
        col2.subheader("Transaction Status")
        status_dist = filtered_transactions['status'].value_counts().reset_index()
        status_dist.columns = ['Status', 'Count']
        col2.pie_chart(status_dist.set_index('Status'))

    stp.grid_item(container_id, "charts", charts_content)

    # Detailed data tables
    def details_content():
        tab1, tab2, tab3 = st.tabs(["👥 Customers", "📦 Products", "💳 Transactions"])
        with tab1:
            tab1.subheader("Customer Details")
            stp.data_table(filtered_customers.head(50), sortable=True, pagination=True)
        with tab2:
            tab2.subheader("Product Catalog")
            stp.data_table(filtered_products.head(50), sortable=True, pagination=True)
        with tab3:
            tab3.subheader("Transaction History")
            stp.data_table(filtered_transactions.head(50), sortable=True, pagination=True)

    stp.grid_item(container_id, "details", details_content)

# Interactive data exploration
def data_exploration(customers, products, transactions):
    st.title("🔍 Interactive Data Exploration")

    # Exploration tabs
    tab_data = [
        {"label": "Customer Analysis", "icon": "👥", "content": lambda: customer_analysis(customers)},
        {"label": "Product Insights", "icon": "📦", "content": lambda: product_insights(products)},
        {"label": "Sales Analytics", "icon": "📊", "content": lambda: sales_analytics(transactions)},
        {"label": "Custom Queries", "icon": "🔧", "content": lambda: custom_queries(customers, products, transactions)}
    ]

    stp.tabs(tab_data)

def customer_analysis(customers):
    st.subheader("Customer Segmentation & Analysis")

    col1, col2 = st.columns(2)

    with col1:
        # Age distribution
        stp.interactive_chart(
            customers,
            chart_type="histogram",
            x_col="age",
            title="Age Distribution"
        )

    with col2:
        # Location distribution
        location_data = customers['location'].value_counts().reset_index()
        location_data.columns = ['Location', 'Count']
        stp.interactive_chart(
            location_data,
            chart_type="bar",
            x_col="Location",
            y_col="Count",
            title="Customers by Location"
        )

    # Customer spending analysis
    st.subheader("Customer Spending Analysis")
    spending_analysis = customers.groupby('loyalty_tier')['total_spent'].agg(['mean', 'sum', 'count']).round(2)
    st.dataframe(spending_analysis)

def product_insights(products):
    st.subheader("Product Performance & Insights")

    # Price vs Rating scatter plot
    stp.interactive_chart(
        products,
        chart_type="scatter",
        x_col="price",
        y_col="rating",
        title="Price vs Customer Rating"
    )

    # Category analysis
    col1, col2 = st.columns(2)

    with col1:
        category_stats = products.groupby('category').agg({
            'price': 'mean',
            'rating': 'mean',
            'reviews_count': 'sum'
        }).round(2)
        st.dataframe(category_stats)

    with col2:
        # Stock analysis
        stock_status = pd.DataFrame({
            'Status': ['In Stock', 'Out of Stock'],
            'Count': [
                products[products['stock_quantity'] > 0].shape[0],
                products[products['stock_quantity'] == 0].shape[0]
            ]
        })
        stp.interactive_chart(
            stock_status,
            chart_type="bar",
            x_col="Status",
            y_col="Count",
            title="Stock Status"
        )

def sales_analytics(transactions):
    st.subheader("Sales Performance Analytics")

    # Time series analysis
    daily_sales = transactions.groupby('date')['total_amount'].sum().reset_index()
    stp.interactive_chart(
        daily_sales,
        chart_type="line",
        x_col="date",
        y_col="total_amount",
        title="Daily Sales Trend"
    )

    # Payment method analysis
    col1, col2 = st.columns(2)

    with col1:
        payment_analysis = transactions.groupby('payment_method')['total_amount'].sum().reset_index()
        stp.interactive_chart(
            payment_analysis,
            chart_type="bar",
            x_col="payment_method",
            y_col="total_amount",
            title="Revenue by Payment Method"
        )

    with col2:
        # Transaction status
        status_analysis = transactions['status'].value_counts().reset_index()
        status_analysis.columns = ['Status', 'Count']
        stp.interactive_chart(
            status_analysis,
            chart_type="pie",
            x_col="Status",
            y_col="Count",
            title="Transaction Status Distribution"
        )

def custom_queries(customers, products, transactions):
    st.subheader("Custom Query Builder")

    # Query builder interface
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Query Parameters")

        dataset = st.selectbox("Dataset", ["Customers", "Products", "Transactions"])

        if dataset == "Customers":
            df = customers
            columns = df.columns.tolist()
        elif dataset == "Products":
            df = products
            columns = df.columns.tolist()
        else:
            df = transactions
            columns = df.columns.tolist()

        selected_columns = st.multiselect("Columns to Display", columns, default=columns[:5])

        # Simple filter builder
        filter_col = st.selectbox("Filter Column", columns)
        filter_op = st.selectbox("Operation", ["equals", "contains", "greater than", "less than"])
        filter_value = st.text_input("Filter Value")

    with col2:
        st.markdown("### Query Results")

        # Apply filters
        result_df = df[selected_columns].copy()

        if filter_value:
            if filter_op == "equals":
                result_df = result_df[result_df[filter_col] == filter_value]
            elif filter_op == "contains":
                result_df = result_df[result_df[filter_col].astype(str).str.contains(filter_value, case=False)]
            elif filter_op == "greater than":
                try:
                    result_df = result_df[result_df[filter_col] > float(filter_value)]
                except:
                    st.error("Invalid filter value for numeric comparison")
            elif filter_op == "less than":
                try:
                    result_df = result_df[result_df[filter_col] < float(filter_value)]
                except:
                    st.error("Invalid filter value for numeric comparison")

        stp.data_table(result_df.head(100), sortable=True, pagination=True)

# Data export functionality
def data_export(customers, products, transactions):
    st.title("📤 Data Export")

    st.markdown("Export your filtered and analyzed data in various formats.")

    col1, col2 = st.columns(2)

    with col1:
        stp.card("Export Options", """
        Choose your preferred format:
        - CSV: Comma-separated values
        - Excel: Spreadsheet format
        - JSON: JavaScript Object Notation
        - Parquet: Columnar storage format
        """)

        export_format = st.selectbox("Export Format", ["CSV", "Excel", "JSON", "Parquet"])
        dataset_choice = st.selectbox("Dataset", ["Customers", "Products", "Transactions"])

    with col2:
        stp.card("Export Settings", """
        Configure your export:
        - Date range filtering
        - Column selection
        - Compression options
        - File naming
        """)

        include_all_columns = st.checkbox("Include all columns", value=True)
        compress_file = st.checkbox("Compress file (ZIP)", value=False)

    # Export button with animation
    if st.button("🚀 Generate Export", type="primary"):
        with st.spinner("Preparing your data export..."):
            time.sleep(2)  # Simulate processing

        stp.notification(f"Export completed! Your {dataset_choice} data has been prepared in {export_format} format.", "success")

        # Mock download button
        st.download_button(
            label="📥 Download File",
            data=b"Mock export data",
            file_name=f"{dataset_choice.lower()}_export.{export_format.lower()}",
            mime="application/octet-stream"
        )

# Main app
def main():
    # Load data
    customers, products, transactions = load_datasets()

    # Sidebar filters
    filters = advanced_filters()

    # Navigation
    st.sidebar.markdown("---")
    pages = {
        "📊 Overview": "overview",
        "🔍 Exploration": "exploration",
        "📤 Export": "export"
    }

    selected_page = st.sidebar.radio("Navigate", options=list(pages.keys()))

    # Page routing
    if pages[selected_page] == "overview":
        data_overview(customers, products, transactions, filters)
    elif pages[selected_page] == "exploration":
        data_exploration(customers, products, transactions)
    elif pages[selected_page] == "export":
        data_export(customers, products, transactions)

    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit++ - Advanced Data Exploration Framework*")

if __name__ == "__main__":
    main()