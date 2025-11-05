"""
Comprehensive Design System Components for Streamlit++

Provides a library of polished UI components including modals, tooltips, cards, etc.
"""

import streamlit as st
from typing import Optional, List, Dict, Any, Callable
import uuid


def card(title: str, content: Any, actions: Optional[List[Dict]] = None, elevation: int = 1, **kwargs):
    """
    Create a customizable card component.

    Args:
        title: Card title
        content: Card content
        actions: List of action buttons [{'label': 'Action', 'on_click': func}]
        elevation: Shadow elevation level (1-5)
        **kwargs: Additional styling
    """
    shadow_levels = {
        1: "0 1px 3px rgba(0,0,0,0.12)",
        2: "0 3px 6px rgba(0,0,0,0.16)",
        3: "0 10px 20px rgba(0,0,0,0.19)",
        4: "0 14px 28px rgba(0,0,0,0.25)",
        5: "0 19px 38px rgba(0,0,0,0.30)"
    }

    st.markdown(f"""
    <div style="
        background: var(--surface-color, white);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: {shadow_levels.get(elevation, shadow_levels[1])};
        border: 1px solid var(--text-secondary-color, #e0e0e0);
    ">
        <h3 style="margin-top: 0; color: var(--text-color, #212529);">{title}</h3>
        <div style="color: var(--text-color, #212529);">{content}</div>
    </div>
    """, unsafe_allow_html=True)

    if actions:
        cols = st.columns(len(actions))
        for i, action in enumerate(actions):
            if cols[i].button(action['label']):
                action.get('on_click', lambda: None)()


def button(label: str, variant: str = "filled", size: str = "medium", on_click: Optional[Callable] = None, **kwargs):
    """
    Enhanced button with variants and sizes.

    Args:
        label: Button label
        variant: 'filled', 'outlined', 'text'
        size: 'small', 'medium', 'large'
        on_click: Click handler
        **kwargs: Additional properties
    """
    sizes = {
        "small": "padding: 0.5rem 1rem; font-size: 0.875rem;",
        "medium": "padding: 0.75rem 1.5rem; font-size: 1rem;",
        "large": "padding: 1rem 2rem; font-size: 1.125rem;"
    }

    variants = {
        "filled": "background: var(--primary-color, #007bff); color: white; border: none;",
        "outlined": "background: transparent; color: var(--primary-color, #007bff); border: 1px solid var(--primary-color, #007bff);",
        "text": "background: transparent; color: var(--primary-color, #007bff); border: none;"
    }

    button_id = f"btn-{uuid.uuid4().hex[:8]}"
    style = f"""
    <style>
    #{button_id} {{
        {sizes.get(size, sizes['medium'])}
        {variants.get(variant, variants['filled'])}
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.2s;
        font-family: inherit;
    }}
    #{button_id}:hover {{
        opacity: 0.8;
        transform: translateY(-1px);
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    if st.button(label, key=button_id, **kwargs):
        if on_click:
            on_click()


def modal(title: str, content: Any, is_open: bool = False, size: str = "medium", **kwargs):
    """
    Create a modal dialog.

    Args:
        title: Modal title
        content: Modal content
        is_open: Whether modal is open
        size: 'small', 'medium', 'large', 'fullscreen'
        **kwargs: Additional options
    """
    if is_open:
        sizes = {
            "small": "width: 300px; height: 200px;",
            "medium": "width: 500px; height: 400px;",
            "large": "width: 800px; height: 600px;",
            "fullscreen": "width: 100vw; height: 100vh;"
        }

        modal_id = f"modal-{uuid.uuid4().hex[:8]}"
        overlay_id = f"modal-overlay-{uuid.uuid4().hex[:8]}"

        st.markdown(f"""
        <style>
        #{overlay_id} {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        }}
        #{modal_id} {{
            background: var(--surface-color, white);
            {sizes.get(size, sizes['medium'])}
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            color: var(--text-color, #212529);
        }}
        </style>
        <div id="{overlay_id}">
            <div id="{modal_id}">
                <h2 style="margin-top: 0;">{title}</h2>
                <div>{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def tooltip(text: str, content: Any, position: str = "top", **kwargs):
    """
    Add a tooltip to content.

    Args:
        text: Tooltip text
        content: Content to wrap
        position: 'top', 'bottom', 'left', 'right'
        **kwargs: Additional styling
    """
    # For now, use a simple approach with help on a placeholder
    # TODO: Implement custom tooltip with HTML/CSS
    placeholder = st.empty()
    with placeholder:
        if callable(content):
            content()
        else:
            st.write(content)
    # Add help to a hidden element or use custom implementation
    st.markdown(f'<span title="{text}">{content}</span>', unsafe_allow_html=True)


def badge(text: str, variant: str = "primary", size: str = "medium", **kwargs):
    """
    Create a badge component.

    Args:
        text: Badge text
        variant: 'primary', 'secondary', 'success', 'danger', 'warning', 'info'
        size: 'small', 'medium', 'large'
        **kwargs: Additional styling
    """
    colors = {
        "primary": "var(--primary-color, #007bff)",
        "secondary": "var(--secondary-color, #6c757d)",
        "success": "var(--success-color, #28a745)",
        "danger": "var(--danger-color, #dc3545)",
        "warning": "var(--warning-color, #ffc107)",
        "info": "var(--info-color, #17a2b8)"
    }

    sizes = {
        "small": "padding: 0.25rem 0.5rem; font-size: 0.75rem;",
        "medium": "padding: 0.375rem 0.75rem; font-size: 0.875rem;",
        "large": "padding: 0.5rem 1rem; font-size: 1rem;"
    }

    badge_id = f"badge-{uuid.uuid4().hex[:8]}"
    style = f"""
    <style>
    #{badge_id} {{
        {sizes.get(size, sizes['medium'])}
        background: {colors.get(variant, colors['primary'])};
        color: white;
        border-radius: 12px;
        display: inline-block;
        font-weight: 500;
        text-align: center;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<span id="{badge_id}">{text}</span>', unsafe_allow_html=True)


def breadcrumb(items: List[Dict[str, Any]], separator: str = "/", **kwargs):
    """
    Create a breadcrumb navigation.

    Args:
        items: List of breadcrumb items [{'label': 'Home', 'href': '#', 'active': False}]
        separator: Separator between items
        **kwargs: Additional styling
    """
    breadcrumb_id = f"breadcrumb-{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{breadcrumb_id} {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 0;
        color: var(--text-secondary-color, #6c757d);
    }}
    #{breadcrumb_id} a {{
        color: var(--primary-color, #007bff);
        text-decoration: none;
    }}
    #{breadcrumb_id} a:hover {{
        text-decoration: underline;
    }}
    #{breadcrumb_id} .active {{
        color: var(--text-color, #212529);
        font-weight: 500;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    breadcrumb_html = f'<nav id="{breadcrumb_id}" aria-label="breadcrumb">'
    for i, item in enumerate(items):
        if i > 0:
            breadcrumb_html += f'<span>{separator}</span>'
        if item.get('active', False):
            breadcrumb_html += f'<span class="active">{item["label"]}</span>'
        else:
            href = item.get('href', '#')
            breadcrumb_html += f'<a href="{href}">{item["label"]}</a>'
    breadcrumb_html += '</nav>'

    st.markdown(breadcrumb_html, unsafe_allow_html=True)


def chip(label: str, variant: str = "outlined", size: str = "medium", removable: bool = False, on_remove: Optional[Callable] = None, **kwargs):
    """
    Create a chip component.

    Args:
        label: Chip label
        variant: 'filled', 'outlined'
        size: 'small', 'medium', 'large'
        removable: Whether chip can be removed
        on_remove: Callback when remove button is clicked
        **kwargs: Additional styling
    """
    sizes = {
        "small": "padding: 0.25rem 0.75rem; font-size: 0.75rem;",
        "medium": "padding: 0.375rem 1rem; font-size: 0.875rem;",
        "large": "padding: 0.5rem 1.25rem; font-size: 1rem;"
    }

    chip_id = f"chip-{uuid.uuid4().hex[:8]}"
    bg_color = "var(--primary-color, #007bff)" if variant == "filled" else "transparent"
    text_color = "white" if variant == "filled" else "var(--primary-color, #007bff)"
    border = "none" if variant == "filled" else f"1px solid var(--primary-color, #007bff)"

    style = f"""
    <style>
    #{chip_id} {{
        {sizes.get(size, sizes['medium'])}
        background: {bg_color};
        color: {text_color};
        border: {border};
        border-radius: 16px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 500;
        cursor: default;
    }}
    #{chip_id} .remove-btn {{
        background: none;
        border: none;
        color: inherit;
        cursor: pointer;
        padding: 0;
        margin-left: 0.25rem;
        font-size: 1.2em;
        line-height: 1;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    remove_html = ""
    if removable:
        remove_btn_id = f"remove-{chip_id}"
        remove_html = f'<button class="remove-btn" id="{remove_btn_id}">×</button>'
        # Note: In a real implementation, you'd need JavaScript for the remove functionality

    st.markdown(f'<span id="{chip_id}">{label}{remove_html}</span>', unsafe_allow_html=True)


def progress_bar(value: float, label: Optional[str] = None, color: str = "primary", size: str = "medium", **kwargs):
    """
    Create a progress bar.

    Args:
        value: Progress value (0-1)
        label: Optional label
        color: Progress color
        size: Bar size
        **kwargs: Additional styling
    """
    colors = {
        "primary": "var(--primary-color, #007bff)",
        "success": "var(--success-color, #28a745)",
        "warning": "var(--warning-color, #ffc107)",
        "danger": "var(--danger-color, #dc3545)"
    }

    sizes = {
        "small": "height: 4px;",
        "medium": "height: 8px;",
        "large": "height: 12px;"
    }

    progress_id = f"progress-{uuid.uuid4().hex[:8]}"
    percentage = min(max(value * 100, 0), 100)

    style = f"""
    <style>
    #{progress_id} {{
        width: 100%;
        {sizes.get(size, sizes['medium'])}
        background: var(--text-secondary-color, #e0e0e0);
        border-radius: 4px;
        overflow: hidden;
    }}
    #{progress_id} .progress-fill {{
        height: 100%;
        width: {percentage}%;
        background: {colors.get(color, colors['primary'])};
        transition: width 0.3s ease;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    if label:
        st.markdown(f"**{label}**")

    st.markdown(f"""
    <div id="{progress_id}">
        <div class="progress-fill"></div>
    </div>
    """, unsafe_allow_html=True)


def tabs(tabs_data: List[Dict[str, Any]], default_active: int = 0, **kwargs):
    """
    Create enhanced tabs with icons.

    Args:
        tabs_data: List of tab data [{'label': 'Tab 1', 'icon': '📊', 'content': func}]
        default_active: Default active tab index
        **kwargs: Additional styling
    """
    tab_labels = [f"{tab.get('icon', '')} {tab['label']}" for tab in tabs_data]

    active_tab = st.radio(
        "Select tab",
        options=range(len(tabs_data)),
        format_func=lambda i: tab_labels[i],
        index=default_active,
        key=f"tabs-{uuid.uuid4().hex[:8]}",
        label_visibility="collapsed"
    )

    if active_tab is not None and tabs_data[active_tab].get('content'):
        tabs_data[active_tab]['content']()


def notification(message: str, type: str = "info", duration: Optional[int] = None, **kwargs):
    """
    Show a notification toast.

    Args:
        message: Notification message
        type: 'info', 'success', 'warning', 'error'
        duration: Auto-dismiss duration in seconds
        **kwargs: Additional options
    """
    icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌"
    }

    if type == "success":
        st.success(f"{icons[type]} {message}")
    elif type == "warning":
        st.warning(f"{icons[type]} {message}")
    elif type == "error":
        st.error(f"{icons[type]} {message}")
    else:
        st.info(f"{icons[type]} {message}")