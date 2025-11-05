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


# Advanced Form Controls
def multi_select(label: str, options: List[str], default: Optional[List[str]] = None,
                searchable: bool = True, placeholder: str = "Search...", max_selections: Optional[int] = None,
                key: Optional[str] = None) -> List[str]:
    """
    Enhanced multi-select with search functionality.

    Args:
        label: Field label
        options: List of available options
        default: Default selected values
        searchable: Whether to enable search
        placeholder: Search placeholder text
        max_selections: Maximum number of selections allowed
        key: Unique key for the component

    Returns:
        List of selected values
    """
    if searchable:
        search_term = st.text_input(
            f"🔍 Search {label.lower()}",
            placeholder=placeholder,
            key=f"search_{key or label}"
        )
        filtered_options = [opt for opt in options if search_term.lower() in str(opt).lower()]
    else:
        filtered_options = options

    selected = st.multiselect(
        label,
        filtered_options,
        default=default or [],
        max_selections=max_selections,
        key=key or f"multi_{label}",
        help=f"Select multiple {label.lower()}"
    )
    return selected


def date_range_picker(label: str, default_start: Optional[Any] = None, default_end: Optional[Any] = None,
                     min_date: Optional[Any] = None, max_date: Optional[Any] = None,
                     key: Optional[str] = None):
    """
    Date range picker with presets.

    Args:
        label: Field label
        default_start: Default start date
        default_end: Default end date
        min_date: Minimum selectable date
        max_date: Maximum selectable date
        key: Unique key for the component

    Returns:
        Tuple of (start_date, end_date)
    """
    import streamlit as st
    from datetime import datetime, timedelta

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            f"{label} - Start",
            value=default_start or (datetime.now() - timedelta(days=30)),
            min_value=min_date,
            max_value=max_date,
            key=f"start_{key or label}"
        )

    with col2:
        end_date = st.date_input(
            f"{label} - End",
            value=default_end or datetime.now(),
            min_value=min_date,
            max_value=max_date,
            key=f"end_{key or label}"
        )

    # Preset buttons
    preset_col1, preset_col2, preset_col3, preset_col4 = st.columns(4)
    with preset_col1:
        if st.button("📅 Last 7 days", key=f"preset_7_{key or label}", help="Select last 7 days"):
            start_date = datetime.now() - timedelta(days=7)
            end_date = datetime.now()
            st.rerun()
    with preset_col2:
        if st.button("📅 Last 30 days", key=f"preset_30_{key or label}", help="Select last 30 days"):
            start_date = datetime.now() - timedelta(days=30)
            end_date = datetime.now()
            st.rerun()
    with preset_col3:
        if st.button("📅 Last 90 days", key=f"preset_90_{key or label}", help="Select last 90 days"):
            start_date = datetime.now() - timedelta(days=90)
            end_date = datetime.now()
            st.rerun()
    with preset_col4:
        if st.button("📅 This year", key=f"preset_year_{key or label}", help="Select this year"):
            start_date = datetime(datetime.now().year, 1, 1)
            end_date = datetime.now()
            st.rerun()

    return start_date, end_date


def color_picker(label: str, default_color: str = "#6366f1", key: Optional[str] = None) -> str:
    """
    Color picker component.

    Args:
        label: Field label
        default_color: Default color value
        key: Unique key for the component

    Returns:
        Selected color as hex string
    """
    color = st.color_picker(
        label,
        value=default_color,
        key=key or f"color_{label}"
    )
    return color


def rich_text_editor(label: str, default_value: str = "", height: int = 200,
                    key: Optional[str] = None) -> str:
    """
    Rich text editor component.

    Args:
        label: Field label
        default_value: Default text content
        height: Editor height in pixels
        key: Unique key for the component

    Returns:
        Edited text content
    """
    text = st.text_area(
        label,
        value=default_value,
        height=height,
        key=key or f"rte_{label}",
        help="Supports Markdown formatting"
    )

    # Preview toggle
    if st.checkbox("👁️ Preview", key=f"preview_{key or label}"):
        st.markdown("**Preview:**")
        st.markdown(text)

    return text


def tag_input(label: str, default_tags: Optional[List[str]] = None, placeholder: str = "Add tags...",
             key: Optional[str] = None) -> List[str]:
    """
    Tag input component.

    Args:
        label: Field label
        default_tags: Initial list of tags
        placeholder: Input placeholder text
        key: Unique key for the component

    Returns:
        List of tags
    """
    if default_tags is None:
        default_tags = []

    # Display current tags
    if default_tags:
        tags_html = " ".join([
            f'<span style="background:#e5e7eb;color:#374151;padding:4px 8px;border-radius:4px;margin:2px;display:inline-block;font-size:0.875rem;">{tag} ✕</span>'
            for tag in default_tags
        ])
        st.markdown(f"**{label}:** {tags_html}", unsafe_allow_html=True)

    # Add new tag
    col1, col2 = st.columns([3, 1])
    with col1:
        new_tag = st.text_input(
            f"➕ Add {label.lower()}",
            placeholder=placeholder,
            key=key or f"tag_input_{label}"
        )
    with col2:
        if st.button("Add", key=f"add_tag_{key or label}", use_container_width=True):
            if new_tag and new_tag.strip() and new_tag not in default_tags:
                default_tags.append(new_tag.strip())
                st.rerun()

    return default_tags


def slider_range(label: str, min_value: float = 0, max_value: float = 100,
                default_values: tuple = (25, 75), step: float = 1,
                key: Optional[str] = None) -> tuple:
    """
    Dual-handle slider for range selection.

    Args:
        label: Field label
        min_value: Minimum value
        max_value: Maximum value
        default_values: Default range values (min, max)
        step: Step size
        key: Unique key for the component

    Returns:
        Tuple of (min_value, max_value)
    """
    values = st.slider(
        label,
        min_value=min_value,
        max_value=max_value,
        value=default_values,
        step=step,
        key=key or f"range_{label}"
    )
    return values


# Media Components
def image_gallery(images: List[str], captions: Optional[List[str]] = None,
                 lightbox: bool = True, columns: int = 3):
    """
    Image gallery with lightbox functionality.

    Args:
        images: List of image URLs or file paths
        captions: List of image captions
        lightbox: Whether to enable lightbox on click
        columns: Number of columns in grid
    """
    if captions is None:
        captions = [f"Image {i+1}" for i in range(len(images))]

    cols = st.columns(columns)

    for i, (img, caption) in enumerate(zip(images, captions)):
        with cols[i % columns]:
            if lightbox:
                # In a real implementation, this would open a lightbox
                if st.button(f"🖼️ {caption}", key=f"img_btn_{i}"):
                    st.image(img, caption=caption, use_column_width=True)
            else:
                st.image(img, caption=caption, use_column_width=True)


def video_player(video_url: str, title: str = "", autoplay: bool = False,
                controls: bool = True, width: Optional[str] = None,
                height: int = 400):
    """
    Custom video player component.

    Args:
        video_url: URL to video file
        title: Video title
        autoplay: Whether to autoplay
        controls: Whether to show controls
        width: Video width
        height: Video height
    """
    if title:
        st.subheader(f"🎥 {title}")

    # Custom controls
    if controls:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            autoplay = st.checkbox("▶️ Autoplay", value=autoplay, key=f"autoplay_{title}")
        with col2:
            loop = st.checkbox("🔄 Loop", key=f"loop_{title}")
        with col3:
            muted = st.checkbox("🔇 Muted", key=f"muted_{title}")

    # Video element
    video_html = f"""
    <video width="{width or '100%'}" height="{height}" controls {"autoplay" if autoplay else ""} {"loop" if loop else ""} {"muted" if muted else ""}>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """

    st.markdown(video_html, unsafe_allow_html=True)


def carousel(images: List[str], captions: Optional[List[str]] = None,
            autoplay: bool = True, interval: int = 3000):
    """
    Image carousel component.

    Args:
        images: List of image URLs
        captions: List of image captions
        autoplay: Whether to auto-advance
        interval: Auto-advance interval in milliseconds
    """
    if captions is None:
        captions = ["" for _ in images]

    # Carousel state
    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0

    # Navigation
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("◀", key="prev_carousel", help="Previous image"):
            st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(images)
            st.rerun()

    with col2:
        current_index = st.session_state.carousel_index
        st.image(images[current_index], caption=captions[current_index], use_column_width=True)
        st.markdown(f"<center><small>{current_index + 1} / {len(images)}</small></center>", unsafe_allow_html=True)

    with col3:
        if st.button("▶", key="next_carousel", help="Next image"):
            st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(images)
            st.rerun()

    # Auto-play (simplified - would need JavaScript for real implementation)
    if autoplay and len(images) > 1:
        import time
        time.sleep(interval / 1000)
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(images)
        st.rerun()


# Enhanced Navigation
def advanced_tabs(tabs_data: List[Dict], default_active: int = 0, orientation: str = "horizontal"):
    """
    Advanced tabs with icons, badges, and custom styling.

    Args:
        tabs_data: List of tab data [{'label': 'Tab 1', 'icon': '📊', 'content': func, 'badge': 'New'}]
        default_active: Default active tab index
        orientation: 'horizontal' or 'vertical'
    """
    if orientation == "vertical":
        cols = st.columns([1, 3])
        with cols[0]:
            tab_options = [f"{tab.get('icon', '')} {tab['label']}" for tab in tabs_data]
            selected_tab = st.radio("", tab_options, key="vertical_tabs", index=default_active)
        with cols[1]:
            selected_index = tab_options.index(selected_tab)
            tabs_data[selected_index]["content"]()
    else:
        # Horizontal tabs with enhanced styling
        tab_labels = []
        for tab in tabs_data:
            label = tab.get("label", "")
            icon = tab.get("icon", "")
            badge = tab.get("badge", "")
            badge_color = tab.get("badge_color", "primary")

            if badge:
                badge_html = f'<span style="background:var(--{badge_color});color:white;padding:2px 6px;border-radius:10px;font-size:0.8em;margin-left:8px;">{badge}</span>'
                tab_labels.append(f"{icon} {label} {badge_html}")
            else:
                tab_labels.append(f"{icon} {label}")

        selected_label = st.radio(
            "",
            tab_labels,
            key="advanced_tabs",
            index=default_active,
            label_visibility="collapsed",
            horizontal=True
        )

        # Find selected tab
        selected_index = tab_labels.index(selected_label)
        tabs_data[selected_index]["content"]()


def breadcrumb_navigation(breadcrumbs: List[Dict], separator: str = ">", clickable: bool = True):
    """
    Breadcrumb navigation component.

    Args:
        breadcrumbs: List of breadcrumb items [{'label': 'Home', 'href': '#', 'active': False}]
        separator: Separator between items
        clickable: Whether breadcrumbs are clickable
    """
    breadcrumb_html = ""
    for i, crumb in enumerate(breadcrumbs):
        if i > 0:
            breadcrumb_html += f' <span style="color:#6b7280;margin:0 8px;">{separator}</span> '

        if clickable and i < len(breadcrumbs) - 1:
            if st.button(crumb, key=f"breadcrumb_{i}"):
                # In a real app, this would navigate to the corresponding page
                st.info(f"Navigate to: {crumb}")
        else:
            breadcrumb_html += f'<span style="font-weight:500;">{crumb}</span>'

    if not clickable:
        st.markdown(breadcrumb_html, unsafe_allow_html=True)


def infinite_scroll_container(items: List[Any], items_per_page: int = 20, height: int = 400):
    """
    Infinite scroll container for large lists.

    Args:
        items: List of items to display
        items_per_page: Number of items to load at once
        height: Container height in pixels
    """
    if 'scroll_page' not in st.session_state:
        st.session_state.scroll_page = 0

    # Container with fixed height
    container = st.container(height=height)

    with container:
        start_idx = st.session_state.scroll_page * items_per_page
        end_idx = start_idx + items_per_page

        for item in items[start_idx:end_idx]:
            st.write(item)

        # Load more button
        if end_idx < len(items):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("Load More", key="load_more", use_container_width=True):
                    st.session_state.scroll_page += 1
                    st.rerun()


# Accessibility Features
def skip_to_content_link(target_id: str = "main-content"):
    """Skip to content link for accessibility."""
    skip_html = f"""
    <a href="#{target_id}" style="position:absolute;left:-9999px;top:10px;background:#000;color:#fff;padding:8px;text-decoration:none;z-index:1000;" onfocus="this.style.left='10px'" onblur="this.style.left='-9999px'">
        Skip to main content
    </a>
    """
    st.markdown(skip_html, unsafe_allow_html=True)


def accessible_button(label: str, on_click: Optional[Callable] = None, key: Optional[str] = None,
                     aria_label: Optional[str] = None, keyboard_shortcut: Optional[str] = None):
    """
    Accessible button with ARIA labels and keyboard shortcuts.

    Args:
        label: Button label
        on_click: Click handler
        key: Unique key
        aria_label: ARIA label for screen readers
        keyboard_shortcut: Keyboard shortcut hint
    """
    button_key = key or f"acc_btn_{label}"

    # Add keyboard shortcut handler if provided
    if keyboard_shortcut:
        # This would require JavaScript in a real implementation
        pass

    return st.button(
        label,
        on_click=on_click,
        key=button_key,
        help=aria_label or keyboard_shortcut
    )


def focus_trap(container_id: str, auto_focus: bool = True):
    """
    Focus trap for modals and dialogs.

    Args:
        container_id: ID of container to trap focus in
        auto_focus: Whether to auto-focus first element
    """
    if auto_focus:
        focus_script = f"""
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const container = document.getElementById('{container_id}');
            if (container) {{
                const focusableElements = container.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
                if (focusableElements.length > 0) {{
                    focusableElements[0].focus();
                }}
            }}
        }});
        </script>
        """
        st.markdown(focus_script, unsafe_allow_html=True)


# Enhanced Data Tables
def advanced_data_table(df, editable_columns: Optional[List[str]] = None,
                       virtual_scroll: bool = False, filterable: bool = True,
                       searchable: bool = True, exportable: bool = True,
                       key: Optional[str] = None):
    """
    Advanced data table with editing, virtual scroll, and more.

    Args:
        df: DataFrame to display
        editable_columns: List of columns that can be edited
        virtual_scroll: Whether to use virtual scrolling
        filterable: Whether to enable column filters
        searchable: Whether to enable search
        exportable: Whether to enable export options
        key: Unique key for the component
    """
    table_key = key or "advanced_table"

    # Search functionality
    if searchable:
        search_term = st.text_input("🔍 Search table...", key=f"search_{table_key}")
        if search_term:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    # Column filters
    if filterable:
        with st.expander("🔧 Filters", expanded=False):
            filter_cols = st.columns(min(len(df.columns), 4))
            filters = {}

            for i, col in enumerate(df.columns[:4]):  # Limit to first 4 columns for space
                with filter_cols[i]:
                    if df[col].dtype in ['int64', 'float64']:
                        min_val, max_val = st.slider(
                            f"Filter {col}",
                            float(df[col].min()),
                            float(df[col].max()),
                            (float(df[col].min()), float(df[col].max())),
                            key=f"filter_{col}_{table_key}"
                        )
                        filters[col] = (min_val, max_val)
                    elif df[col].dtype == 'object':
                        unique_vals = df[col].unique()
                        selected = st.multiselect(
                            f"Filter {col}",
                            unique_vals,
                            key=f"filter_{col}_{table_key}"
                        )
                        if selected:
                            filters[col] = selected

    # Apply filters
    for col, filter_val in filters.items():
        if isinstance(filter_val, tuple):  # Numeric range
            df = df[(df[col] >= filter_val[0]) & (df[col] <= filter_val[1])]
        else:  # Categorical filter
            df = df[df[col].isin(filter_val)]

    # Editable columns (demo - changes not persisted)
    if editable_columns:
        st.info("✏️ Double-click cells to edit (demo - changes not persisted)")

    # Export functionality
    if exportable:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col2:
            if st.download_button(
                "📥 CSV",
                df.to_csv(index=False),
                "data.csv",
                "text/csv",
                key=f"csv_{table_key}"
            ):
                st.success("CSV downloaded!")
        with col3:
            if st.download_button(
                "📊 Excel",
                df.to_excel(index=False).getvalue(),
                "data.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key=f"excel_{table_key}"
            ):
                st.success("Excel downloaded!")

    # Display table
    if virtual_scroll and len(df) > 100:
        # Virtual scroll implementation (simplified)
        start_row = st.slider("📏 Scroll to row", 0, len(df)-50, 0, key=f"scroll_{table_key}")
        end_row = min(start_row + 50, len(df))
        st.dataframe(df.iloc[start_row:end_row], use_container_width=True)
        st.text(f"Showing rows {start_row} - {end_row} of {len(df)}")
    else:
        st.dataframe(df, use_container_width=True)