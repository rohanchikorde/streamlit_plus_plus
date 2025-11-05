"""
Streamlit++ Flexible Widget Positioning Demo

Demonstrates flexible widget positioning - users can place widgets on left, right, top, or bottom.
"""

import streamlit as st
import streamlit_plus as stp
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Flexible Widgets - Streamlit++",
    page_icon="🎛️",
    layout="wide"
)

# Custom theme
theme = stp.custom_theme(colors={
    "primary": "#8b5cf6",
    "secondary": "#06b6d4",
    "success": "#10b981",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "info": "#6366f1"
})
stp.set_theme(theme)

def create_flexible_widgets(left_enabled, right_enabled, top_enabled, bottom_enabled,
                          left_size, right_size, top_size, bottom_size, collapsible):
    """Create widgets in user-selected positions"""

    # Left sidebar widgets
    if left_enabled:
        left_widgets = [
            {
                "title": "🔍 Quick Search",
                "content": lambda: render_search_widget(),
                "expanded": True
            },
            {
                "title": "📊 Filters",
                "content": lambda: render_filter_widget(),
                "expanded": False
            },
            {
                "title": "🎯 Quick Actions",
                "content": lambda: render_actions_widget(),
                "expanded": False
            }
        ]

        stp.create_widget_panel(
            position="left",
            size=f"{left_size}px",
            widgets=left_widgets,
            collapsible=collapsible,
            title="Left Panel"
        )

    # Right sidebar widgets
    if right_enabled:
        right_widgets = [
            {
                "title": "📈 Analytics",
                "content": lambda: render_analytics_widget(),
                "expanded": True
            },
            {
                "title": "🔔 Notifications",
                "content": lambda: render_notifications_widget(),
                "expanded": False
            },
            {
                "title": "👤 User Profile",
                "content": lambda: render_profile_widget(),
                "expanded": False
            }
        ]

        stp.create_widget_panel(
            position="right",
            size=f"{right_size}px",
            widgets=right_widgets,
            collapsible=collapsible,
            title="Right Panel"
        )

    # Top bar widgets
    if top_enabled:
        top_widgets = [
            {
                "title": "🔔 Alerts",
                "content": lambda: render_alerts_widget(),
                "expanded": True
            },
            {
                "title": "🌐 Language",
                "content": lambda: render_language_widget(),
                "expanded": False
            }
        ]

        stp.create_widget_panel(
            position="top",
            size=f"{top_size}px",
            widgets=top_widgets,
            collapsible=collapsible,
            title="Top Bar"
        )

    # Bottom bar widgets
    if bottom_enabled:
        bottom_widgets = [
            {
                "title": "🎵 Media Player",
                "content": lambda: render_media_widget(),
                "expanded": True
            },
            {
                "title": "💬 Chat",
                "content": lambda: render_chat_widget(),
                "expanded": False
            }
        ]

        stp.create_widget_panel(
            position="bottom",
            size=f"{bottom_size}px",
            widgets=bottom_widgets,
            collapsible=collapsible,
            title="Bottom Bar"
        )

def main():
    st.title("🎛️ Flexible Widget Positioning Demo")
    st.markdown("**Choose where to place your widgets:** left, right, top, or bottom!")

    # Widget position selector
    st.subheader("📍 Widget Position Settings")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        left_enabled = st.checkbox("📍 Left Sidebar", value=True, key="left_enabled")
        left_size = st.slider("Width", 200, 500, 300, key="left_size") if left_enabled else 300

    with col2:
        right_enabled = st.checkbox("📍 Right Sidebar", key="right_enabled")
        right_size = st.slider("Width", 200, 500, 300, key="right_size") if right_enabled else 300

    with col3:
        top_enabled = st.checkbox("📍 Top Bar", key="top_enabled")
        top_size = st.slider("Height", 100, 300, 150, key="top_size") if top_enabled else 150

    with col4:
        bottom_enabled = st.checkbox("📍 Bottom Bar", key="bottom_enabled")
        bottom_size = st.slider("Height", 100, 300, 150, key="bottom_size") if bottom_enabled else 150

    # Collapsible settings
    st.subheader("⚙️ Widget Behavior")
    col1, col2 = st.columns(2)

    with col1:
        collapsible = st.checkbox("Collapsible Panels", value=True)
        auto_collapse = st.checkbox("Auto-collapse on mobile", value=True)

    with col2:
        show_toggle_buttons = st.checkbox("Show Toggle Buttons", value=True)
        remember_state = st.checkbox("Remember panel states", value=True)

    # Demo content
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.subheader("📊 Main Content Area")

    # Sample data for demo
    chart_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [1200, 1900, 1500, 2100, 1800, 2400],
        'Users': [450, 520, 480, 610, 550, 680]
    })

    col1, col2 = st.columns(2)

    with col1:
        stp.card("Sales Trend", "Monthly sales performance over time.")
        st.line_chart(chart_data.set_index('Month')['Sales'])

    with col2:
        stp.card("User Growth", "Monthly active users growth.")
        st.bar_chart(chart_data.set_index('Month')['Users'])

    # KPI Cards
    kpis = [
        {"title": "Total Revenue", "value": "$45,231", "delta": 12.5, "icon": "💰"},
        {"title": "Active Users", "value": "2,847", "delta": 8.2, "icon": "👥"},
        {"title": "Conversion Rate", "value": "3.24%", "delta": -2.1, "icon": "📈"},
        {"title": "Avg. Order Value", "value": "$89.50", "delta": 5.7, "icon": "🛒"}
    ]

    stp.kpi_dashboard(kpis, columns=4)

    # Create widgets based on user selection
    create_flexible_widgets(
        left_enabled=left_enabled,
        right_enabled=right_enabled,
        top_enabled=top_enabled,
        bottom_enabled=bottom_enabled,
        left_size=left_size,
        right_size=right_size,
        top_size=top_size,
        bottom_size=bottom_size,
        collapsible=collapsible
    )

# Widget content functions
def render_search_widget():
    """Quick search widget"""
    search_term = st.text_input("Search...", placeholder="Type to search...", key="quick_search")
    if search_term:
        st.info(f"Searching for: **{search_term}**")

    # Recent searches
    st.markdown("**Recent Searches:**")
    recent = ["dashboard", "analytics", "reports", "users"]
    for item in recent:
        if st.button(f"🔍 {item}", key=f"recent_{item}"):
            st.info(f"Selected: {item}")

def render_filter_widget():
    """Filter widget"""
    st.markdown("**Date Range:**")
    start_date, end_date = stp.date_range_picker("Filter Period", key="filter_dates")

    st.markdown("**Categories:**")
    categories = stp.multi_select(
        "Select Categories",
        ["Sales", "Marketing", "Support", "Development"],
        default=["Sales"],
        key="filter_categories"
    )

    st.markdown("**Status:**")
    status = st.radio("Status", ["All", "Active", "Inactive"], key="filter_status")

    if st.button("Apply Filters", key="apply_filters"):
        st.success("Filters applied!")

def render_actions_widget():
    """Quick actions widget"""
    actions = [
        ("➕ New Item", "Create new item"),
        ("📤 Export", "Export data"),
        ("🔄 Refresh", "Refresh data"),
        ("⚙️ Settings", "Open settings")
    ]

    for action, desc in actions:
        if st.button(action, help=desc, key=f"action_{action}", use_container_width=True):
            st.info(f"Action: {desc}")

def render_analytics_widget():
    """Analytics widget"""
    # Mini chart
    data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10).cumsum()
    })
    st.line_chart(data.set_index('x'))

    # Stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Views", "1,234", "+12%")
    with col2:
        st.metric("Clicks", "567", "+8%")

def render_notifications_widget():
    """Notifications widget"""
    notifications = [
        {"title": "New message", "time": "2 min ago", "type": "info"},
        {"title": "Task completed", "time": "1 hour ago", "type": "success"},
        {"title": "Warning alert", "time": "3 hours ago", "type": "warning"}
    ]

    for notif in notifications:
        icon = {"info": "ℹ️", "success": "✅", "warning": "⚠️"}.get(notif["type"], "📢")
        st.markdown(f"{icon} **{notif['title']}** - {notif['time']}")

def render_profile_widget():
    """User profile widget"""
    st.markdown("**Welcome back!** 👋")
    st.markdown("**John Doe**")
    st.markdown("*john.doe@company.com*")

    st.progress(0.75, text="Profile completion: 75%")

    if st.button("View Profile", key="view_profile"):
        st.info("Profile page would open here")

def render_alerts_widget():
    """Alerts widget"""
    alerts = [
        ("🚨 System maintenance tonight", "warning"),
        ("✅ Backup completed", "success"),
        ("📢 New feature released", "info")
    ]

    for alert, type in alerts:
        st.markdown(f"**{alert}**")

def render_language_widget():
    """Language selector widget"""
    languages = ["English", "Spanish", "French", "German", "Chinese"]
    selected_lang = st.selectbox("Language", languages, key="language_selector")

    if selected_lang != "English":
        st.info(f"Language switching to {selected_lang} (demo)")

def render_media_widget():
    """Media player widget"""
    st.markdown("🎵 **Now Playing:** Jazz Classics")

    # Simple controls
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("⏮️", key="prev_track")
    with col2:
        st.button("⏯️", key="play_pause")
    with col3:
        st.button("⏭️", key="next_track")

    # Progress
    st.slider("Progress", 0, 100, 45, key="media_progress")

def render_chat_widget():
    """Chat widget"""
    st.markdown("💬 **Team Chat**")

    # Sample messages
    messages = [
        ("Alice", "Hey team, how's the project going?", "10:30 AM"),
        ("Bob", "Going well! Just finished the new feature.", "10:32 AM"),
        ("You", "Great work everyone! 🚀", "10:35 AM")
    ]

    for sender, msg, time in messages:
        st.markdown(f"**{sender}:** {msg} *{time}*")

    # Message input
    new_msg = st.text_input("Type a message...", key="chat_input")
    if st.button("Send", key="send_msg"):
        st.info("Message sent! (demo)")

if __name__ == "__main__":
    main()