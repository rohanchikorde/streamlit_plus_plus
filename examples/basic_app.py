"""
Basic example demonstrating Streamlit++ features.
"""

import streamlit as st
import streamlit_plus as stp
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Streamlit++ Demo", layout="wide")

# Apply theme
theme = stp.custom_theme(colors={"primary": "#ff6b6b"})
stp.set_theme(theme)

st.title("🚀 Streamlit++ Demo")

# Theme toggle
if st.button("Toggle Dark Mode"):
    stp.toggle_dark_mode()
    st.rerun()

st.markdown("---")

# Layout demo
st.header("Advanced Layout System")

with st.expander("CSS Grid Layout Example"):
    container_id = stp.css_grid_layout("grid-template-areas: 'header header' 'sidebar main' 'footer footer'; grid-template-rows: auto 1fr auto; grid-template-columns: 200px 1fr;")
    stp.grid_item(container_id, "header", lambda: st.markdown("### Header Area"))
    stp.grid_item(container_id, "sidebar", lambda: st.markdown("**Sidebar**\n\n- Menu Item 1\n- Menu Item 2"))
    stp.grid_item(container_id, "main", lambda: st.markdown("## Main Content Area\n\nThis is the main content area with flexible grid layout."))
    stp.grid_item(container_id, "footer", lambda: st.markdown("*Footer content*"))

# Floating panel
with st.expander("Floating Panel"):
    stp.floating_panel(
        lambda: st.write("This is a floating panel that can be positioned anywhere!"),
        position="top-right",
        width="250px",
        height="150px"
    )

st.markdown("---")

# Components demo
st.header("UI Components")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Enhanced Buttons")
    stp.button("Primary Button", variant="filled")
    stp.button("Outlined Button", variant="outlined")
    stp.button("Text Button", variant="text")

with col2:
    st.subheader("Badges & Chips")
    stp.badge("New", variant="success")
    stp.badge("Warning", variant="warning")
    stp.chip("React", variant="filled")
    stp.chip("Vue", variant="outlined")

with col3:
    st.subheader("Progress & Loading")
    stp.progress_bar(0.75, "Progress", color="success")
    stp.loading_spinner(size="small", color="primary")

# Card component
st.subheader("Card Component")
stp.card(
    "Sample Card",
    "This is a customizable card with elevation and actions. It uses CSS variables for theming.",
    actions=[
        {"label": "Action 1", "on_click": lambda: st.success("Action 1 clicked!")},
        {"label": "Action 2", "on_click": lambda: st.info("Action 2 clicked!")}
    ],
    elevation=3
)

# Breadcrumb navigation
st.subheader("Breadcrumb Navigation")
stp.breadcrumb([
    {"label": "Home", "href": "#"},
    {"label": "Products", "href": "#"},
    {"label": "Streamlit++", "active": True}
])

# Modal dialog
st.header("Modal Dialog")
if st.button("Open Modal"):
    stp.modal(
        "Sample Modal",
        "This is a modal dialog with custom content and theming support.",
        is_open=True,
        size="medium"
    )

st.markdown("---")

# Animations demo
st.header("Animations & Transitions")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Fade In Animation")
    stp.fade_in(lambda: st.info("This content fades in smoothly!"), delay=0.5)

with col2:
    st.subheader("Slide In Animation")
    stp.slide_in(lambda: st.success("This content slides in from the side!"), direction="right")

# Loading states
st.subheader("Loading States")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Skeleton Loader:")
    stp.skeleton_loader(width="200px", height="20px")

with col2:
    st.write("Shimmer Effect:")
    stp.shimmer_effect(lambda: st.button("Loading Button..."))

with col3:
    st.write("Spinner:")
    stp.loading_spinner(color="primary")

st.markdown("---")

# Data visualization demo
st.header("Data Visualizations")

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
data = pd.DataFrame({
    'date': dates,
    'sales': np.random.normal(100, 20, 100).cumsum() + 1000,
    'users': np.random.normal(50, 10, 100).cumsum() + 500,
    'revenue': np.random.normal(200, 50, 100).cumsum() + 2000
})

# Metric cards
kpis = [
    {"title": "Total Sales", "value": "12,543", "delta": 12.5, "icon": "💰"},
    {"title": "Active Users", "value": "1,234", "delta": -2.1, "icon": "👥"},
    {"title": "Revenue", "value": "$45,678", "delta": 8.3, "icon": "📈"}
]

stp.kpi_dashboard(kpis, columns=3)

# Interactive chart
st.subheader("Interactive Chart")
try:
    stp.interactive_chart(data, chart_type="line", x_col="date", y_col=["sales", "users", "revenue"],
                         title="Business Metrics Over Time")
except Exception as e:
    st.warning(f"Interactive chart requires plotly: {e}")
    st.line_chart(data.set_index('date')[['sales', 'users', 'revenue']])

# Enhanced data table
st.subheader("Enhanced Data Table")
sample_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 92, 78, 96, 88]
})

stp.data_table(sample_data, sortable=True, filterable=True, pagination=True)

st.markdown("---")
st.info("More advanced features coming soon! This demonstrates the core capabilities of Streamlit++.")