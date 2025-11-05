"""
Data Visualization Components for Streamlit++

Provides interactive charting libraries and advanced visualization features.
"""

import streamlit as st
from typing import Optional, List, Dict, Any, Callable, Union
import pandas as pd
import numpy as np
import uuid


def interactive_chart(data: pd.DataFrame, chart_type: str = "line", x_col: str = None, y_col: str = None,
                     title: str = "", **kwargs):
    """
    Create an interactive chart with zoom, pan, and tooltips.

    Args:
        data: DataFrame with chart data
        chart_type: 'line', 'bar', 'scatter', 'area'
        x_col: Column name for x-axis
        y_col: Column name for y-axis (or list for multiple)
        title: Chart title
        **kwargs: Additional chart options
    """
    try:
        import plotly.express as px
        import plotly.graph_objects as go
    except ImportError:
        st.error("Plotly is required for interactive charts. Install with: pip install plotly")
        return

    if x_col is None:
        x_col = data.columns[0]
    if y_col is None:
        y_cols = [col for col in data.columns if col != x_col][:3]  # Up to 3 y columns
    elif isinstance(y_col, str):
        y_cols = [y_col]
    else:
        y_cols = y_col

    if chart_type == "line":
        fig = px.line(data, x=x_col, y=y_cols, title=title)
    elif chart_type == "bar":
        fig = px.bar(data, x=x_col, y=y_cols, title=title)
    elif chart_type == "scatter":
        fig = px.scatter(data, x=x_col, y=y_cols[0] if y_cols else None, title=title)
    elif chart_type == "area":
        fig = px.area(data, x=x_col, y=y_cols[0] if y_cols else None, title=title)
    else:
        st.error(f"Unsupported chart type: {chart_type}")
        return

    # Add interactive features
    fig.update_layout(
        hovermode='x unified',
        dragmode='zoom',
        showlegend=True
    )

    # Add range slider for time series
    if pd.api.types.is_datetime64_any_dtype(data[x_col]):
        fig.update_xaxes(rangeslider_visible=True)

    st.plotly_chart(fig, use_container_width=True, **kwargs)


def drill_down_chart(data: pd.DataFrame, hierarchy: List[str], value_col: str, **kwargs):
    """
    Create a drill-down chart for hierarchical data exploration.

    Args:
        data: DataFrame with hierarchical data
        hierarchy: List of column names defining the hierarchy
        value_col: Column name for values
        **kwargs: Additional options
    """
    try:
        import plotly.express as px
    except ImportError:
        st.error("Plotly is required for drill-down charts. Install with: pip install plotly")
        return

    # For simplicity, create a sunburst chart
    fig = px.sunburst(
        data,
        path=hierarchy,
        values=value_col,
        title="Drill-down Visualization"
    )

    st.plotly_chart(fig, use_container_width=True)


def animated_data_chart(data: pd.DataFrame, x_col: str, y_col: str, animation_col: str,
                       chart_type: str = "scatter", **kwargs):
    """
    Create an animated chart showing data changes over time.

    Args:
        data: DataFrame with time-series data
        x_col: X-axis column
        y_col: Y-axis column
        animation_col: Column to animate over
        chart_type: Chart type
        **kwargs: Additional options
    """
    try:
        import plotly.express as px
    except ImportError:
        st.error("Plotly is required for animated charts. Install with: pip install plotly")
        return

    if chart_type == "scatter":
        fig = px.scatter(data, x=x_col, y=y_col, animation_frame=animation_col,
                        title="Animated Data Visualization")
    elif chart_type == "bar":
        fig = px.bar(data, x=x_col, y=y_col, animation_frame=animation_col,
                    title="Animated Data Visualization")
    else:
        fig = px.line(data, x=x_col, y=y_col, animation_frame=animation_col,
                     title="Animated Data Visualization")

    st.plotly_chart(fig, use_container_width=True)


def metric_card(title: str, value: Union[int, float, str], delta: Optional[Union[int, float]] = None,
               delta_color: str = "normal", icon: str = "", **kwargs):
    """
    Create an animated metric card.

    Args:
        title: Metric title
        value: Metric value
        delta: Change value
        delta_color: 'normal', 'inverse', 'off'
        icon: Icon emoji or text
        **kwargs: Additional styling
    """
    card_id = f"metric-{uuid.uuid4().hex[:8]}"

    # Format delta
    delta_text = ""
    delta_class = ""
    if delta is not None:
        if delta > 0:
            delta_text = f"↗️ +{delta}"
            delta_class = "positive"
        elif delta < 0:
            delta_text = f"↘️ {delta}"
            delta_class = "negative"
        else:
            delta_text = f"→ {delta}"
            delta_class = "neutral"

    style = f"""
    <style>
    #{card_id} {{
        background: var(--surface-color, white);
        border: 1px solid var(--text-secondary-color, #e0e0e0);
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem;
    }}
    #{card_id} .metric-value {{
        font-size: 2rem;
        font-weight: bold;
        color: var(--primary-color, #007bff);
        margin: 0.5rem 0;
    }}
    #{card_id} .metric-title {{
        font-size: 0.875rem;
        color: var(--text-secondary-color, #6c757d);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    #{card_id} .metric-delta {{
        font-size: 0.75rem;
        margin-top: 0.5rem;
    }}
    #{card_id} .positive {{ color: var(--success-color, #28a745); }}
    #{card_id} .negative {{ color: var(--danger-color, #dc3545); }}
    #{card_id} .neutral {{ color: var(--text-secondary-color, #6c757d); }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    st.markdown(f"""
    <div id="{card_id}">
        <div class="metric-title">{icon} {title}</div>
        <div class="metric-value">{value}</div>
        {f'<div class="metric-delta {delta_class}">{delta_text}</div>' if delta_text else ''}
    </div>
    """, unsafe_allow_html=True)


def data_table(data: pd.DataFrame, sortable: bool = True, filterable: bool = True,
              pagination: bool = True, page_size: int = 10, **kwargs):
    """
    Create an enhanced data table with sorting, filtering, and pagination.

    Args:
        data: DataFrame to display
        sortable: Enable column sorting
        filterable: Enable column filtering
        pagination: Enable pagination
        page_size: Number of rows per page
        **kwargs: Additional options
    """
    try:
        import streamlit.components.v1 as components
    except ImportError:
        st.dataframe(data)
        return

    # For now, use Streamlit's built-in dataframe with some enhancements
    # A full implementation would use a custom component

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        search = st.text_input("Search", key=f"search-{uuid.uuid4().hex[:8]}")

    with col2:
        if sortable:
            sort_by = st.selectbox("Sort by", ["None"] + list(data.columns),
                                 key=f"sort-{uuid.uuid4().hex[:8]}")
        else:
            sort_by = "None"

    with col3:
        if pagination:
            page_size = st.selectbox("Page size", [5, 10, 25, 50, 100],
                                   index=1, key=f"page-size-{uuid.uuid4().hex[:8]}")
        else:
            page_size = len(data)

    # Apply filters
    filtered_data = data.copy()
    if search:
        mask = filtered_data.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
        filtered_data = filtered_data[mask]

    # Apply sorting
    if sort_by != "None":
        filtered_data = filtered_data.sort_values(sort_by)

    # Apply pagination
    if pagination:
        total_pages = len(filtered_data) // page_size + 1
        page = st.number_input("Page", min_value=1, max_value=total_pages, value=1,
                             key=f"page-{uuid.uuid4().hex[:8]}")
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        display_data = filtered_data.iloc[start_idx:end_idx]
    else:
        display_data = filtered_data

    st.dataframe(display_data, use_container_width=True)


def chart_with_controls(data: pd.DataFrame, chart_types: List[str] = None, **kwargs):
    """
    Create a chart with interactive controls.

    Args:
        data: DataFrame with chart data
        chart_types: Available chart types
        **kwargs: Additional options
    """
    if chart_types is None:
        chart_types = ["line", "bar", "scatter", "area"]

    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Controls")
        chart_type = st.selectbox("Chart Type", chart_types,
                                key=f"chart-type-{uuid.uuid4().hex[:8]}")

        # Column selectors
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()

        x_options = data.columns.tolist()
        y_options = numeric_cols

        x_col = st.selectbox("X-axis", x_options, key=f"x-col-{uuid.uuid4().hex[:8]}")
        y_col = st.multiselect("Y-axis", y_options, default=y_options[:1] if y_options else [],
                             key=f"y-col-{uuid.uuid4().hex[:8]}")

        # Additional options
        show_trendline = st.checkbox("Show trendline", key=f"trend-{uuid.uuid4().hex[:8]}")
        show_grid = st.checkbox("Show grid", value=True, key=f"grid-{uuid.uuid4().hex[:8]}")

    with col2:
        if y_col:
            interactive_chart(data, chart_type=chart_type, x_col=x_col, y_col=y_col,
                            title=f"{chart_type.title()} Chart")
        else:
            st.info("Please select at least one Y-axis column")


def kpi_dashboard(kpis: List[Dict[str, Any]], columns: int = 3, **kwargs):
    """
    Create a KPI dashboard with metric cards.

    Args:
        kpis: List of KPI dictionaries with 'title', 'value', 'delta', 'icon' keys
        columns: Number of columns in the grid
        **kwargs: Additional options
    """
    rows = (len(kpis) + columns - 1) // columns

    for row in range(rows):
        cols = st.columns(columns)
        for col in range(columns):
            idx = row * columns + col
            if idx < len(kpis):
                kpi = kpis[idx]
                with cols[col]:
                    metric_card(
                        title=kpi['title'],
                        value=kpi['value'],
                        delta=kpi.get('delta'),
                        delta_color=kpi.get('delta_color', 'normal'),
                        icon=kpi.get('icon', '')
                    )