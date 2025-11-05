"""
Streamlit++ Sample Project - Analytics Dashboard

A comprehensive example demonstrating Streamlit++ features in a real-world analytics dashboard.
"""

import streamlit as st
import streamlit_plus as stp
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="Analytics Dashboard - Streamlit++",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom theme
theme = stp.custom_theme(colors={
    "primary": "#6366f1",
    "secondary": "#8b5cf6",
    "success": "#10b981",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "info": "#06b6d4"
})
stp.set_theme(theme)

# Sidebar navigation
def sidebar_navigation():
    st.sidebar.title("📊 Analytics Dashboard")

    # Theme toggle
    if st.sidebar.button("🌙 Toggle Dark Mode", use_container_width=True):
        stp.toggle_dark_mode()
        st.rerun()

    st.sidebar.markdown("---")

    # Navigation menu
    pages = {
        "🏠 Overview": "overview",
        "📈 Analytics": "analytics",
        "👥 Users": "users",
        "💰 Revenue": "revenue",
        "⚙️ Settings": "settings"
    }

    selected_page = st.sidebar.radio(
        "Navigate",
        options=list(pages.keys()),
        key="nav_radio"
    )

    return pages[selected_page]

# Generate sample data
@st.cache_data
def generate_sample_data():
    np.random.seed(42)

    # Time series data
    dates = pd.date_range('2024-01-01', periods=365, freq='D')

    # User metrics
    users = pd.DataFrame({
        'date': dates,
        'new_users': np.random.poisson(50, 365),
        'active_users': np.random.normal(1000, 200, 365).astype(int),
        'churned_users': np.random.poisson(20, 365)
    })

    # Revenue data
    revenue = pd.DataFrame({
        'date': dates,
        'subscription_revenue': np.random.normal(5000, 1000, 365),
        'one_time_purchases': np.random.normal(2000, 500, 365),
        'total_revenue': np.random.normal(7000, 1500, 365)
    })

    # Product data
    products = pd.DataFrame({
        'product_id': range(1, 21),
        'name': [f'Product {i}' for i in range(1, 21)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], 20),
        'price': np.random.uniform(10, 500, 20).round(2),
        'stock': np.random.randint(0, 1000, 20),
        'rating': np.random.uniform(1, 5, 20).round(1)
    })

    return users, revenue, products

# Overview page
def overview_page(users_df, revenue_df, products_df):
    st.title("📊 Dashboard Overview")

    # KPI Cards
    kpis = [
        {
            "title": "Total Users",
            "value": f"{users_df['active_users'].iloc[-1]:,}",
            "delta": 12.5,
            "icon": "👥"
        },
        {
            "title": "Monthly Revenue",
            "value": f"${revenue_df['total_revenue'].iloc[-30:].sum():,.0f}",
            "delta": 8.3,
            "icon": "💰"
        },
        {
            "title": "Active Products",
            "value": str(len(products_df)),
            "delta": 2.1,
            "icon": "📦"
        },
        {
            "title": "Avg Rating",
            "value": f"{products_df['rating'].mean():.1f}⭐",
            "delta": -0.2,
            "icon": "⭐"
        }
    ]

    stp.kpi_dashboard(kpis, columns=4)

    # Main dashboard layout
    container_id = stp.css_grid_layout("""
        grid-template-areas:
            'chart1 chart2'
            'chart3 table1';
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 400px 400px;
        gap: 2rem;
    """)

    # Chart 1: User growth
    stp.grid_item(container_id, "chart1", lambda: (
        st.subheader("👥 User Growth Trend"),
        stp.interactive_chart(
            users_df.tail(90),
            chart_type="line",
            x_col="date",
            y_col=["new_users", "active_users"],
            title=""
        )
    ))

    # Chart 2: Revenue breakdown
    stp.grid_item(container_id, "chart2", lambda: (
        st.subheader("💰 Revenue Breakdown"),
        stp.interactive_chart(
            revenue_df.tail(90),
            chart_type="area",
            x_col="date",
            y_col=["subscription_revenue", "one_time_purchases"],
            title=""
        )
    ))

    # Chart 3: Product categories
    stp.grid_item(container_id, "chart3", lambda: (
        st.subheader("📦 Product Categories"),
        category_data := products_df.groupby('category').size().reset_index(name='count'),
        stp.interactive_chart(
            category_data,
            chart_type="bar",
            x_col="category",
            y_col="count",
            title=""
        )
    ))

    # Table: Top products
    stp.grid_item(container_id, "table1", lambda: (
        st.subheader("🏆 Top Rated Products"),
        top_products := products_df.nlargest(5, 'rating')[['name', 'category', 'price', 'rating']],
        stp.data_table(top_products, sortable=True, pagination=False)
    ))

# Analytics page
def analytics_page(users_df, revenue_df, products_df):
    st.title("📈 Advanced Analytics")

    # Animated entrance
    stp.fade_in(lambda: st.markdown("### Real-time Analytics with Interactive Visualizations"), delay=0.2)

    tab_data = [
        {"label": "Users", "icon": "👥", "content": lambda: user_analytics(users_df)},
        {"label": "Revenue", "icon": "💰", "content": lambda: revenue_analytics(revenue_df)},
        {"label": "Products", "icon": "📦", "content": lambda: product_analytics(products_df)},
        {"label": "Predictions", "icon": "🔮", "content": lambda: prediction_analytics()}
    ]

    stp.tabs(tab_data)

def user_analytics(users_df):
    col1, col2 = st.columns([2, 1])

    with col1:
        stp.interactive_chart(
            users_df,
            chart_type="line",
            x_col="date",
            y_col=["active_users", "new_users", "churned_users"],
            title="User Metrics Over Time"
        )

    with col2:
        # User stats cards
        stp.card("User Statistics", f"""
        **Total Active Users:** {users_df['active_users'].iloc[-1]:,}
        **New Users (Last 30 days):** {users_df['new_users'].tail(30).sum():,}
        **Churn Rate:** {users_df['churned_users'].tail(30).sum() / users_df['active_users'].tail(30).mean() * 100:.1f}%
        **Growth Rate:** +{((users_df['active_users'].iloc[-1] / users_df['active_users'].iloc[-31]) - 1) * 100:.1f}%
        """)

def revenue_analytics(revenue_df):
    # Revenue trends with drill-down
    stp.interactive_chart(
        revenue_df,
        chart_type="area",
        x_col="date",
        y_col=["subscription_revenue", "one_time_purchases", "total_revenue"],
        title="Revenue Trends"
    )

    # Monthly breakdown
    monthly_revenue = revenue_df.set_index('date').resample('M').sum()
    stp.interactive_chart(
        monthly_revenue.reset_index(),
        chart_type="bar",
        x_col="date",
        y_col="total_revenue",
        title="Monthly Revenue"
    )

def product_analytics(products_df):
    col1, col2 = st.columns(2)

    with col1:
        # Price distribution
        fig_data = products_df.copy()
        stp.interactive_chart(
            fig_data,
            chart_type="scatter",
            x_col="price",
            y_col="rating",
            title="Price vs Rating Correlation"
        )

    with col2:
        # Stock levels
        low_stock = products_df[products_df['stock'] < 100]
        stp.data_table(
            low_stock[['name', 'category', 'stock', 'price']],
            sortable=True,
            pagination=True,
            page_size=5
        )

def prediction_analytics():
    st.info("🔮 Prediction analytics would integrate with ML models here")

    # Mock prediction data
    future_dates = pd.date_range('2025-01-01', periods=30, freq='D')
    predictions = pd.DataFrame({
        'date': future_dates,
        'predicted_users': np.random.normal(1100, 150, 30),
        'predicted_revenue': np.random.normal(7500, 1000, 30)
    })

    stp.interactive_chart(
        predictions,
        chart_type="line",
        x_col="date",
        y_col=["predicted_users", "predicted_revenue"],
        title="Future Predictions (Mock Data)"
    )

# Users page
def users_page(users_df):
    st.title("👥 User Management")

    # User segmentation
    col1, col2 = st.columns(2)

    with col1:
        stp.card("User Segmentation", """
        **New Users:** Growing steadily
        **Returning Users:** 75% retention rate
        **Premium Users:** 15% conversion rate
        **Inactive Users:** 5% churn rate
        """)

    with col2:
        # User activity heatmap (mock)
        activity_data = pd.DataFrame({
            'hour': range(24),
            'activity': np.random.exponential(1, 24)
        })
        stp.interactive_chart(
            activity_data,
            chart_type="bar",
            x_col="hour",
            y_col="activity",
            title="User Activity by Hour"
        )

    # User table with advanced features
    st.subheader("User Directory")
    mock_users = pd.DataFrame({
        'id': range(1, 101),
        'name': [f'User {i}' for i in range(1, 101)],
        'email': [f'user{i}@example.com' for i in range(1, 101)],
        'status': np.random.choice(['Active', 'Inactive', 'Premium'], 100),
        'last_login': pd.date_range('2024-01-01', periods=100, freq='D'),
        'signup_date': pd.date_range('2023-01-01', periods=100, freq='D')
    })

    stp.data_table(mock_users, sortable=True, filterable=True, pagination=True)

# Revenue page
def revenue_page(revenue_df):
    st.title("💰 Revenue Analytics")

    # Revenue metrics with animations
    stp.fade_in(lambda: None, delay=0.1)  # Just for timing

    # Revenue breakdown
    revenue_breakdown = pd.DataFrame({
        'source': ['Subscriptions', 'One-time Purchases', 'Affiliate', 'Other'],
        'amount': [45000, 25000, 5000, 2000],
        'percentage': [60, 33.3, 6.7, 2.7]
    })

    col1, col2 = st.columns(2)

    with col1:
        stp.interactive_chart(
            revenue_breakdown,
            chart_type="bar",
            x_col="source",
            y_col="amount",
            title="Revenue by Source"
        )

    with col2:
        # Revenue goals
        stp.card("Revenue Goals", """
        **Monthly Target:** $100,000
        **Current Progress:** 75%
        **Projected End of Month:** $85,000
        **Growth vs Last Month:** +12.5%
        """)

        # Progress bar
        stp.progress_bar(0.75, "Monthly Goal Progress", color="success")

    # Revenue forecasting
    st.subheader("Revenue Forecasting")
    forecast_data = pd.DataFrame({
        'month': pd.date_range('2024-01-01', periods=12, freq='M'),
        'actual': np.random.normal(70000, 5000, 12),
        'forecast': np.random.normal(75000, 3000, 12)
    })

    stp.interactive_chart(
        forecast_data,
        chart_type="line",
        x_col="month",
        y_col=["actual", "forecast"],
        title="Revenue Forecast vs Actual"
    )

# Settings page
def settings_page():
    st.title("⚙️ Settings")

    # Settings organized in cards
    col1, col2 = st.columns(2)

    with col1:
        stp.card("Theme Settings", """
        Customize the appearance of your dashboard.

        - Color scheme
        - Font preferences
        - Layout options
        """)

        theme_options = ["Light", "Dark", "Auto", "Custom"]
        selected_theme = st.selectbox("Theme", theme_options)

        if st.button("Apply Theme"):
            stp.notification("Theme updated successfully!", "success")

    with col2:
        stp.card("Notification Settings", """
        Configure how you receive updates.

        - Email notifications
        - In-app alerts
        - Report schedules
        """)

        notifications = st.multiselect(
            "Notification Types",
            ["Email", "Push", "SMS", "In-app"],
            default=["Email", "In-app"]
        )

    # Advanced settings in expandable sections
    with st.expander("Advanced Settings"):
        st.subheader("Data Export")
        export_format = st.selectbox("Export Format", ["CSV", "Excel", "JSON", "PDF"])
        date_range = st.date_input("Date Range", [datetime.now() - timedelta(days=30), datetime.now()])

        if st.button("Export Data"):
            stp.notification("Data export started. You'll receive a download link soon.", "info")

    with st.expander("API Configuration"):
        st.code("""
        # API Configuration
        API_KEY = "your-api-key-here"
        BASE_URL = "https://api.example.com"
        TIMEOUT = 30
        """, language="python")

# Main app
def main():
    # Load data
    users_df, revenue_df, products_df = generate_sample_data()

    # Navigation
    current_page = sidebar_navigation()

    # Page routing
    if current_page == "overview":
        overview_page(users_df, revenue_df, products_df)
    elif current_page == "analytics":
        analytics_page(users_df, revenue_df, products_df)
    elif current_page == "users":
        users_page(users_df)
    elif current_page == "revenue":
        revenue_page(revenue_df)
    elif current_page == "settings":
        settings_page()

    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit++ - Advanced UI Framework for Streamlit*")

if __name__ == "__main__":
    main()