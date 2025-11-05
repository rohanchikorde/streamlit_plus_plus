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


def flexible_sidebar(position: str = "left", width: str = "300px", collapsible: bool = True,
                    title: str = "", content: Any = None, **kwargs):
    """
    Create a flexible sidebar that can be positioned anywhere.

    Args:
        position: Position ('left', 'right', 'top', 'bottom')
        width: Sidebar width (for left/right) or height (for top/bottom)
        collapsible: Whether sidebar can be collapsed
        title: Sidebar title
        content: Content function to render
        **kwargs: Additional styling options
    """
    sidebar_id = f"flex-sidebar-{uuid.uuid4().hex[:8]}"

    # Position-specific styles
    if position == "left":
        position_style = f"""
        position: fixed;
        top: 0;
        left: 0;
        width: {width};
        height: 100vh;
        transform: translateX(0);
        """
        toggle_style = "left: 100%;"
        main_margin = f"margin-left: {width};"
    elif position == "right":
        position_style = f"""
        position: fixed;
        top: 0;
        right: 0;
        width: {width};
        height: 100vh;
        transform: translateX(0);
        """
        toggle_style = "right: 100%;"
        main_margin = f"margin-right: {width};"
    elif position == "top":
        position_style = f"""
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: {width};
        transform: translateY(0);
        """
        toggle_style = "top: 100%; left: 50%; transform: translateX(-50%);"
        main_margin = f"margin-top: {width};"
    elif position == "bottom":
        position_style = f"""
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100vw;
        height: {width};
        transform: translateY(0);
        """
        toggle_style = "bottom: 100%; left: 50%; transform: translateX(-50%);"
        main_margin = f"margin-bottom: {width};"
    else:
        raise ValueError(f"Invalid position: {position}. Use 'left', 'right', 'top', or 'bottom'.")

    # Collapsible functionality
    if collapsible:
        if f"sidebar_collapsed_{sidebar_id}" not in st.session_state:
            st.session_state[f"sidebar_collapsed_{sidebar_id}"] = False

        collapsed = st.session_state[f"sidebar_collapsed_{sidebar_id}"]

        if position in ["left", "right"]:
            transform = "translateX(-100%)" if collapsed else "translateX(0)"
        else:  # top/bottom
            transform = "translateY(-100%)" if collapsed else "translateY(0)"

        position_style = position_style.replace("transform: translateX(0);", f"transform: {transform};")
        position_style = position_style.replace("transform: translateY(0);", f"transform: {transform};")

        if not collapsed:
            main_margin = main_margin
        else:
            main_margin = ""

    # CSS styles
    style = f"""
    <style>
    #{sidebar_id} {{
        {position_style}
        background: var(--surface-color, #ffffff);
        border: 1px solid var(--text-secondary-color, #e0e0e0);
        border-radius: 0;
        padding: 1rem;
        z-index: 999;
        box-shadow: 2px 0 4px rgba(0,0,0,0.1);
        overflow-y: auto;
        transition: transform 0.3s ease;
    }}

    #{sidebar_id} .sidebar-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--text-secondary-color, #e0e0e0);
    }}

    #{sidebar_id} .sidebar-toggle {{
        position: absolute;
        {toggle_style}
        background: var(--primary-color, #6366f1);
        color: white;
        border: none;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        font-size: 16px;
        line-height: 1;
        padding: 0;
        margin: 0;
    }}

    .main-content {{
        transition: margin 0.3s ease;
        padding: 1rem;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    # Handle toggle button click
    if collapsible:
        toggle_key = f"toggle_{sidebar_id}"
        if st.button("", key=toggle_key, help="Toggle sidebar"):
            current_state = st.session_state.get(f"sidebar_collapsed_{sidebar_id}", False)
            st.session_state[f"sidebar_collapsed_{sidebar_id}"] = not current_state
            st.rerun()

    # Sidebar content
    sidebar_html = f'<div id="{sidebar_id}">'

    if collapsible:
        toggle_icon = "▶" if st.session_state.get(f"sidebar_collapsed_{sidebar_id}", False) else "◀" if position == "left" else "◀" if position == "right" else "▼" if position == "top" else "▲"
        sidebar_html += f'''
        <div class="sidebar-toggle">
            {toggle_icon}
        </div>
        '''

    if title:
        sidebar_html += f'<div class="sidebar-header"><h3>{title}</h3>'

        if collapsible:
            close_key = f"close_{sidebar_id}"
            if st.button("✕", key=close_key, help="Close sidebar"):
                st.session_state[f"sidebar_collapsed_{sidebar_id}"] = True
                st.rerun()

        sidebar_html += '</div>'

    sidebar_html += '</div>'  # Close sidebar div

    st.markdown(sidebar_html, unsafe_allow_html=True)

    # Render content inside sidebar using Streamlit components
    if content and not st.session_state.get(f"sidebar_collapsed_{sidebar_id}", False):
        with st.container():
            content()

    return sidebar_id


def create_widget_panel(position: str = "left", size: str = "300px", widgets: List[Dict] = None,
                       collapsible: bool = True, title: str = "Widgets", **kwargs):
    """
    Create a widget panel with multiple widgets that can be positioned flexibly.

    Args:
        position: Position ('left', 'right', 'top', 'bottom')
        size: Panel size (width for left/right, height for top/bottom)
        widgets: List of widget dictionaries with 'title', 'content', and 'expanded' keys
        collapsible: Whether panel can be collapsed
        title: Panel title
        **kwargs: Additional options
    """
    if widgets is None:
        widgets = []

    def render_widgets():
        for i, widget in enumerate(widgets):
            with st.expander(widget.get('title', f'Widget {i+1}'),
                           expanded=widget.get('expanded', False)):
                widget_content = widget.get('content')
                if widget_content:
                    if callable(widget_content):
                        widget_content()
                    else:
                        st.write(widget_content)

    return flexible_sidebar(
        position=position,
        width=size,
        collapsible=collapsible,
        title=title,
        content=render_widgets,
        **kwargs
    )


def responsive_layout(mobile_breakpoint: int = 768):
    """
    Create a responsive layout system that adapts to screen size.

    Args:
        mobile_breakpoint: Screen width breakpoint for mobile layout

    Returns:
        Layout configuration dictionary
    """
    # This would typically use JavaScript to detect screen size
    # For now, return a basic configuration
    return {
        "mobile_breakpoint": mobile_breakpoint,
        "sidebar_position": "top" if mobile_breakpoint > 768 else "left",
        "sidebar_size": "200px",
        "main_margin": "auto"
    }


def overlay_panel(content: Any, trigger_element: str = None, position: str = "center",
                 width: str = "500px", height: str = "auto", modal: bool = True, **kwargs):
    """
    Create an overlay panel that appears over content.

    Args:
        content: Content to display in overlay
        trigger_element: Element that triggers the overlay
        position: Position ('center', 'top', 'bottom', 'left', 'right')
        width: Panel width
        height: Panel height
        modal: Whether to show as modal (blocks background)
        **kwargs: Additional styling
    """
    overlay_id = f"overlay-panel-{uuid.uuid4().hex[:8]}"

    # Position styles
    position_styles = {
        "center": "top: 50%; left: 50%; transform: translate(-50%, -50%);",
        "top": "top: 10%; left: 50%; transform: translateX(-50%);",
        "bottom": "bottom: 10%; left: 50%; transform: translateX(-50%);",
        "left": "top: 50%; left: 10%; transform: translateY(-50%);",
        "right": "top: 50%; right: 10%; transform: translateY(-50%);"
    }

    backdrop_style = "backdrop-filter: blur(4px); background: rgba(0,0,0,0.5);" if modal else ""

    style = f"""
    <style>
    #{overlay_id} {{
        position: fixed;
        {position_styles.get(position, position_styles['center'])}
        width: {width};
        height: {height};
        background: var(--surface-color, white);
        border: 1px solid var(--text-secondary-color, #ddd);
        border-radius: 8px;
        padding: 1.5rem;
        z-index: 10000;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        max-height: 90vh;
        overflow-y: auto;
    }}

    #{overlay_id}-backdrop {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 9999;
        {backdrop_style}
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    # Backdrop for modal
    if modal:
        st.markdown(f'<div id="{overlay_id}-backdrop"></div>', unsafe_allow_html=True)

    # Overlay content
    st.markdown(f'<div id="{overlay_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)

    return overlay_id