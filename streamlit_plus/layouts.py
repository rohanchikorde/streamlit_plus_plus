"""
Advanced Layout System for Streamlit++

Provides flexible grid-based layouts, component positioning, and dashboard templates.
"""

import streamlit as st
from typing import List, Optional, Union, Dict, Any, Tuple
import uuid


def grid_layout(rows: int, cols: int, gap: str = "1rem", **kwargs) -> List[List]:
    """
    Create a flexible grid layout.

    Args:
        rows: Number of rows
        cols: Number of columns
        gap: Gap between grid items
        **kwargs: Additional CSS properties

    Returns:
        List of lists containing column objects
    """
    # For now, use Streamlit's columns
    # TODO: Implement custom CSS Grid layout
    grid = []
    for _ in range(rows):
        row = st.columns(cols)
        grid.append(row)
    return grid


def css_grid_layout(grid_template: str, gap: str = "1rem", height: str = "auto", **kwargs) -> str:
    """
    Create a CSS Grid layout container.

    Args:
        grid_template: CSS grid-template-areas or grid-template-columns/rows
        gap: Gap between grid items
        height: Container height
        **kwargs: Additional CSS properties

    Returns:
        Unique container ID for placing content
    """
    container_id = f"grid-container-{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{container_id} {{
        display: grid;
        {grid_template}
        gap: {gap};
        height: {height};
        width: 100%;
        padding: 1rem;
        box-sizing: border-box;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    return container_id


def grid_item(container_id: str, grid_area: str, content: Any, **kwargs):
    """
    Place content in a specific grid area.

    Args:
        container_id: ID of the grid container
        grid_area: CSS grid-area value
        content: Content to place
        **kwargs: Additional styling
    """
    item_id = f"grid-item-{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{item_id} {{
        grid-area: {grid_area};
        padding: 1rem;
        border-radius: 8px;
        background: var(--surface-color, #f8f9fa);
        border: 1px solid var(--text-secondary-color, #e0e0e0);
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{item_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def dashboard_template(template_type: str = "analytics") -> Dict[str, Any]:
    """
    Get a pre-built dashboard template configuration.

    Args:
        template_type: Type of template ('analytics', 'admin', 'explorer')

    Returns:
        Dictionary with layout configuration
    """
    templates = {
        "analytics": {
            "header": {"height": "10%", "components": ["title", "filters"]},
            "sidebar": {"width": "20%", "components": ["navigation", "settings"]},
            "main": {"width": "80%", "components": ["charts", "metrics"]},
        },
        "admin": {
            "header": {"height": "8%", "components": ["logo", "user_menu"]},
            "sidebar": {"width": "15%", "components": ["menu", "quick_actions"]},
            "content": {"width": "85%", "components": ["dashboard", "tables"]},
        },
        "explorer": {
            "toolbar": {"height": "5%", "components": ["search", "filters"]},
            "content": {"height": "95%", "components": ["data_view", "details"]},
        }
    }
    return templates.get(template_type, templates["analytics"])


def floating_panel(content: Any, position: str = "top-right", width: str = "300px", height: str = "200px", **kwargs):
    """
    Create a floating panel.

    Args:
        content: Content to display in the panel
        position: Position ('top-left', 'top-right', 'bottom-left', 'bottom-right')
        width: Panel width
        height: Panel height
        **kwargs: Additional styling
    """
    panel_id = f"floating-panel-{uuid.uuid4().hex[:8]}"

    position_styles = {
        "top-left": "top: 10px; left: 10px;",
        "top-right": "top: 10px; right: 10px;",
        "bottom-left": "bottom: 10px; left: 10px;",
        "bottom-right": "bottom: 10px; right: 10px;"
    }

    style = f"""
    <style>
    #{panel_id} {{
        position: fixed;
        {position_styles.get(position, position_styles['top-right'])}
        width: {width};
        height: {height};
        background: var(--surface-color, white);
        border: 1px solid var(--text-secondary-color, #ddd);
        border-radius: 8px;
        padding: 1rem;
        z-index: 1000;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        overflow: auto;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{panel_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def absolute_position(content: Any, top: str = "auto", left: str = "auto", right: str = "auto", bottom: str = "auto", z_index: int = 1, **kwargs):
    """
    Position content absolutely.

    Args:
        content: Content to position
        top, left, right, bottom: Position values
        z_index: Z-index for layering
        **kwargs: Additional styling
    """
    element_id = f"abs-position-{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{element_id} {{
        position: absolute;
        top: {top};
        left: {left};
        right: {right};
        bottom: {bottom};
        z-index: {z_index};
        padding: 1rem;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{element_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def collapsible_section(title: str, content: Any, expanded: bool = False, **kwargs):
    """
    Create a collapsible section.

    Args:
        title: Section title
        content: Section content
        expanded: Whether section starts expanded
        **kwargs: Additional options
    """
    with st.expander(title, expanded=expanded):
        content()