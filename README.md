# Streamlit++

A Python framework to make Streamlit UI much better with advanced features for modern web applications.

For a UI-focused advanced Streamlit version, you should prioritize visual sophistication, modern design patterns, and rich interactivity that goes beyond Streamlit's current simple vertical layout.

## Features

### Advanced Layout System

**Flexible Widget Positioning**: Place widgets anywhere on the screen - left, right, top, or bottom sidebars with customizable sizes and collapsible behavior. Break free from Streamlit's traditional left-sidebar limitation.

**Flexible Grid System**: Implement a comprehensive grid-based layout with drag-and-drop positioning, allowing components to be placed anywhere on the canvas. Move beyond the limited vertical flow and basic columns to support complex multi-column grids, nested layouts, and responsive breakpoints.

**Component Positioning**: Add absolute, relative, and fixed positioning options with z-index control for layering elements. Include floating panels, sidebars that can be pinned/unpinned, and collapsible sections for better space utilization.

**Dashboard Templates**: Provide pre-built layout templates for common use cases (analytics dashboards, admin panels, data explorers) that users can customize.

### Comprehensive Design System

**Component Library**: Build an extensive library similar to Material UI or Ant Design with 50+ polished components including advanced elements like modals, tooltips, popovers, breadcrumbs, badges, chips, steppers, timelines, and carousels.

**Modern UI Controls**: Include sophisticated input components like multi-select with search, tag inputs, date/time range pickers with presets, color pickers, file upload with drag-drop and preview, rich text editors, and slider ranges.

**Card-Based Design**: Offer customizable card components with headers, footers, actions, images, and various elevation levels for depth.

**Navigation Components**: Add tabs with icons, nested navigation, breadcrumbs, pagination, infinite scroll, and hamburger/meatballs menus for mobile-friendly navigation.

### Theming and Styling

**Advanced Theme Engine**: Implement comprehensive theming with light/dark mode toggle, custom color palettes, typography scales, spacing systems, and shadow/elevation presets.

**Full CSS Control**: Allow inline CSS, external stylesheets, and CSS-in-JS approaches without hacks or workarounds. Support CSS variables for dynamic theming and modern CSS features like Grid and Flexbox layouts.

**Design Tokens**: Use design tokens for consistent styling across components with support for brand customization.

**Component Variants**: Provide multiple variants for each component (outlined, filled, text, sizes: small/medium/large) to match different design needs.

### Animations and Transitions

**Micro-interactions**: Add smooth hover effects, button ripples, loading animations, and feedback animations for user actions.

**Page Transitions**: Implement view transition animations between pages/sections with fade, slide, scale, and custom easing functions.

**Element Animations**: Support entrance animations (fade-in, slide-in, bounce), exit animations, and scroll-triggered animations for data reveals.

**Motion Principles**: Follow modern animation principles with appropriate duration (200-400ms for most transitions), consistent directionality, and physics-based easing curves.

**Loading States**: Create skeleton screens, shimmer effects, progress bars, and spinners for better perceived performance.

### Interactive Data Visualization

**Advanced Charts**: Integrate interactive charting libraries with zoom, pan, brush selection, crosshairs, and synchronized multi-chart interactions.

**Dynamic Tooltips**: Show contextual information on hover with rich content including images, mini-charts, and formatted data.

**Drill-Down Capabilities**: Enable clicking on chart elements to reveal detailed views or filter related visualizations.

**Animated Data**: Support animated transitions when data updates, number counters that count up, and time-series playback controls.

**3D Visualizations**: Include 3D charts, globe visualizations, and AR-inspired graphics for immersive data exploration.

### Responsive Design

**Mobile-First Approach**: Build components that work seamlessly on mobile with touch-friendly interactions, swipe gestures, and appropriate sizing.

**Adaptive Layouts**: Automatically reorganize layouts for different screen sizes with customizable breakpoints.

**Progressive Disclosure**: Use accordions, expandable sections, and bottom sheets for mobile to manage screen real estate.

### Advanced UI Components

**Data Tables**: Rich tables with inline editing, column sorting/filtering, row selection, virtual scrolling for large datasets, and export functionality.

**Forms**: Multi-step wizards, field validation with real-time feedback, conditional fields, and auto-save functionality.

**Notifications System**: Toast notifications, snackbars, alerts with actions, and notification centers with history.

**Modals and Dialogs**: Customizable modals with different sizes, fullscreen mode, stacked modals, and confirmation dialogs.

**Media Components**: Image galleries with lightbox, video players with controls, audio waveforms, and carousel sliders.

### Visual Hierarchy

**Clear Information Architecture**: Implement proper visual hierarchy using size, color, contrast, and spacing to guide user attention to important elements.

**Whitespace Management**: Use generous whitespace to separate sections and prevent visual clutter.

**Color Psychology**: Apply color meaningfully for status indicators (success/warning/error), data categories, and visual grouping.

### Accessibility Features

**WCAG Compliance**: Ensure all components meet WCAG 2.1 AA standards with proper contrast ratios, keyboard navigation, and screen reader support.

**Focus Management**: Clear focus indicators, logical tab order, and skip-to-content links.

**Keyboard Shortcuts**: Global and contextual keyboard shortcuts for power users.

## Installation

```bash
pip install streamlit-plus
```

## Quick Start

```python
import streamlit as st
import streamlit_plus as stp

# Set up the app
st.set_page_config(page_title="My App", layout="wide")

# Apply a custom theme
theme = stp.custom_theme(colors={
    "primary": "#6366f1",
    "secondary": "#06b6d4",
    "success": "#10b981"
})
stp.set_theme(theme)

st.title("Welcome to Streamlit++")
```

## Detailed Usage Guide

### 1. Flexible Widget Positioning

The flexible widget positioning system allows you to place interactive panels anywhere on the screen, breaking free from Streamlit's traditional left-sidebar limitation.

#### Basic Usage

```python
import streamlit as st
import streamlit_plus as stp

# Define widgets as a list of dictionaries
widgets = [
    {
        "title": "🔍 Quick Search",
        "content": lambda: st.text_input("Search...", placeholder="Type to search..."),
        "expanded": True
    },
    {
        "title": "📊 Filters",
        "content": lambda: st.multiselect("Categories", ["Sales", "Marketing", "Support"]),
        "expanded": False
    }
]

# Create panels in different positions
stp.create_widget_panel(
    position="left",
    size="300px",
    widgets=widgets,
    collapsible=True,
    title="Left Panel"
)
```

#### Position Options

- `"left"`: Left sidebar (traditional position)
- `"right"`: Right sidebar
- `"top"`: Top bar/header area
- `"bottom"`: Bottom bar/footer area

#### Configuration Parameters

```python
stp.create_widget_panel(
    position="left",           # "left", "right", "top", "bottom"
    size="300px",             # Width for sidebars, height for top/bottom
    widgets=widgets,          # List of widget dictionaries
    collapsible=True,         # Whether panels can be collapsed
    title="Panel Title",      # Optional panel title
    default_expanded=True     # Whether panel starts expanded
)
```

#### Widget Dictionary Structure

Each widget in the `widgets` list should be a dictionary with:

```python
{
    "title": "Widget Title",           # Display title with optional emoji
    "content": lambda: st.write("Content"),  # Function that renders the widget
    "expanded": True                   # Whether this specific widget starts expanded
}
```

#### Complete Example

```python
import streamlit as st
import streamlit_plus as stp
import pandas as pd

# Page configuration
st.set_page_config(page_title="Flexible Widgets Demo", layout="wide")

# Custom theme
theme = stp.custom_theme(colors={"primary": "#8b5cf6"})
stp.set_theme(theme)

st.title("🎛️ Flexible Widget Positioning Demo")

# Interactive controls
col1, col2, col3, col4 = st.columns(4)

with col1:
    left_enabled = st.checkbox("📍 Left Sidebar", value=True)
    left_size = st.slider("Width", 200, 500, 300) if left_enabled else 300

with col2:
    right_enabled = st.checkbox("📍 Right Sidebar")
    right_size = st.slider("Width", 200, 500, 300) if right_enabled else 300

with col3:
    top_enabled = st.checkbox("📍 Top Bar")
    top_size = st.slider("Height", 100, 300, 150) if top_enabled else 150

with col4:
    bottom_enabled = st.checkbox("📍 Bottom Bar")
    bottom_size = st.slider("Height", 100, 300, 150) if bottom_enabled else 150

# Collapsible settings
collapsible = st.checkbox("Collapsible Panels", value=True)

# Define widget content functions
def search_widget():
    query = st.text_input("Search", placeholder="Search...")
    if query:
        st.info(f"Searching for: {query}")

def filter_widget():
    categories = st.multiselect("Categories", ["A", "B", "C"], default=["A"])
    date_range = stp.date_range_picker("Date Range")
    return categories, date_range

def analytics_widget():
    st.metric("Revenue", "$45,231", "+12%")
    st.metric("Users", "2,847", "+8%")

# Create panels conditionally
if left_enabled:
    left_widgets = [
        {"title": "🔍 Search", "content": search_widget, "expanded": True},
        {"title": "📊 Filters", "content": filter_widget, "expanded": False}
    ]
    stp.create_widget_panel("left", f"{left_size}px", left_widgets, collapsible)

if right_enabled:
    right_widgets = [
        {"title": "📈 Analytics", "content": analytics_widget, "expanded": True}
    ]
    stp.create_widget_panel("right", f"{right_size}px", right_widgets, collapsible)

if top_enabled:
    top_widgets = [
        {"title": "🔔 Alerts", "content": lambda: st.warning("System maintenance tonight"), "expanded": True}
    ]
    stp.create_widget_panel("top", f"{top_size}px", top_widgets, collapsible)

if bottom_enabled:
    bottom_widgets = [
        {"title": "🎵 Media Player", "content": lambda: st.audio("sample.mp3"), "expanded": True}
    ]
    stp.create_widget_panel("bottom", f"{bottom_size}px", bottom_widgets, collapsible)

# Main content area
st.markdown("---")
st.header("📊 Main Content")

# Your main app content here
st.write("This is the main content area. Widgets are positioned around it.")
```

### 2. Advanced Layout System

#### CSS Grid Layout

```python
# Create a custom grid layout
container_id = stp.css_grid_layout("""
    grid-template-areas:
        'header header sidebar'
        'main main sidebar'
        'footer footer footer';
    grid-template-rows: auto 1fr auto;
    grid-template-columns: 1fr 1fr 300px;
    gap: 20px;
""")

# Add content to grid areas
stp.grid_item(container_id, "header",
    lambda: st.markdown("### My App Header"))

stp.grid_item(container_id, "sidebar",
    lambda: st.sidebar.markdown("## Sidebar Content"))

stp.grid_item(container_id, "main",
    lambda: st.write("Main content area"))

stp.grid_item(container_id, "footer",
    lambda: st.markdown("*Footer content*"))
```

#### Floating Panels

```python
# Create a floating panel
stp.floating_panel(
    content=lambda: st.write("This panel floats anywhere!"),
    position="top-right",
    width="250px",
    height="150px",
    draggable=True
)
```

### 3. Enhanced Components

#### Advanced Form Controls

```python
# Date range picker with presets
start_date, end_date = stp.date_range_picker(
    "Select Date Range",
    presets=["Last 7 days", "Last 30 days", "This month"],
    key="date_range"
)

# Multi-select with search
selected_items = stp.multi_select(
    "Choose items",
    options=["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    default=["Apple"],
    searchable=True,
    key="multi_select"
)

# Enhanced slider with range
min_val, max_val = stp.range_slider(
    "Price Range",
    min_value=0,
    max_value=1000,
    value=(100, 500),
    step=10
)
```

#### Card Components

```python
# Basic card
stp.card(
    title="Sales Performance",
    content="Monthly sales have increased by 12%",
    icon="📈"
)

# Advanced card with actions
with stp.card(header="Product Details", elevation=2):
    st.image("product.jpg")
    st.write("**Product Name**")
    st.write("$29.99")

    # Card actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Add to Cart"):
            st.success("Added!")
    with col2:
        if st.button("View Details"):
            st.info("Details page")
```

#### KPI Dashboard

```python
# Create KPI cards
kpis = [
    {
        "title": "Total Revenue",
        "value": "$45,231",
        "delta": 12.5,
        "icon": "💰",
        "color": "success"
    },
    {
        "title": "Active Users",
        "value": "2,847",
        "delta": 8.2,
        "icon": "👥",
        "color": "info"
    },
    {
        "title": "Conversion Rate",
        "value": "3.24%",
        "delta": -2.1,
        "icon": "📈",
        "color": "warning"
    }
]

stp.kpi_dashboard(kpis, columns=3)
```

### 4. Theming and Styling

#### Custom Themes

```python
# Define a custom theme
theme = stp.custom_theme(
    colors={
        "primary": "#6366f1",
        "secondary": "#06b6d4",
        "success": "#10b981",
        "danger": "#ef4444",
        "warning": "#f59e0b",
        "info": "#3b82f6",
        "light": "#f8fafc",
        "dark": "#1e293b"
    },
    fonts={
        "primary": "Inter, sans-serif",
        "mono": "JetBrains Mono, monospace"
    }
)

# Apply the theme
stp.set_theme(theme)

# Toggle dark mode
if st.button("Toggle Dark Mode"):
    stp.toggle_dark_mode()
    st.rerun()
```

#### CSS Variables and Custom Styles

```python
# Inject custom CSS
custom_css = """
:root {
    --custom-primary: #8b5cf6;
    --custom-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.custom-card {
    border: 1px solid var(--custom-primary);
    border-radius: 8px;
    box-shadow: var(--custom-shadow);
    padding: 16px;
}
"""

st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)
```

### 5. Animations and Transitions

#### Loading States

```python
# Skeleton loading
with stp.skeleton_loader():
    st.write("Loading content...")
    time.sleep(2)  # Simulate loading

# Progress indicators
with stp.progress_indicator("Processing data..."):
    for i in range(100):
        time.sleep(0.01)
        st.progress(i + 1)
```

#### Animated Transitions

```python
# Fade in content
with stp.fade_in():
    st.header("Welcome!")
    st.write("This content fades in smoothly")

# Slide transitions
if st.button("Next Page"):
    with stp.slide_left():
        st.header("Next Page")
        st.write("Content slides in from the right")
```

### 6. Data Visualization Enhancements

#### Interactive Charts

```python
import plotly.express as px

# Create enhanced chart
fig = px.line(df, x="date", y="value", title="Sales Trend")

# Add interactive features
enhanced_fig = stp.enhance_chart(
    fig,
    zoom=True,
    pan=True,
    brush_selection=True,
    crosshairs=True
)

st.plotly_chart(enhanced_fig)
```

#### Drill-Down Capabilities

```python
# Chart with drill-down
chart_data = stp.drill_down_chart(
    data=df,
    dimensions=["region", "category", "product"],
    measures=["sales", "profit"],
    initial_level=0
)

st.plotly_chart(chart_data["chart"])

# Show drill-down controls
if chart_data["selected"]:
    st.subheader(f"Details for {chart_data['selected']}")
    # Show detailed view
```

### 7. Responsive Design

#### Mobile-First Components

```python
# Responsive columns that stack on mobile
with stp.responsive_columns([1, 1, 1], breakpoints={"md": [1, 1], "sm": [1]}):
    st.write("Column 1")
    st.write("Column 2")
    st.write("Column 3")

# Mobile-friendly navigation
nav_items = [
    {"label": "Home", "icon": "🏠", "href": "/"},
    {"label": "Dashboard", "icon": "📊", "href": "/dashboard"},
    {"label": "Settings", "icon": "⚙️", "href": "/settings"}
]

stp.mobile_navigation(nav_items, position="bottom")
```

### 8. Advanced UI Components

#### Data Tables

```python
# Enhanced data table
table_config = {
    "sortable": True,
    "filterable": True,
    "editable": True,
    "pagination": True,
    "page_size": 10,
    "exportable": True
}

stp.data_table(df, config=table_config)
```

#### Modals and Dialogs

```python
# Confirmation dialog
if st.button("Delete Item"):
    confirmed = stp.confirm_dialog(
        title="Confirm Deletion",
        message="Are you sure you want to delete this item?",
        confirm_text="Delete",
        cancel_text="Cancel"
    )

    if confirmed:
        # Delete the item
        st.success("Item deleted!")

# Custom modal
with stp.modal("Edit Profile", size="large"):
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Save"):
        st.success("Profile updated!")
        stp.close_modal()
```

#### Notifications

```python
# Toast notifications
if st.button("Show Success"):
    stp.toast("Operation completed successfully!", type="success")

if st.button("Show Error"):
    stp.toast("An error occurred!", type="error")

# Notification center
notifications = [
    {"title": "New message", "message": "You have a new message", "time": "2 min ago"},
    {"title": "Task completed", "message": "Your export is ready", "time": "1 hour ago"}
]

stp.notification_center(notifications)
```

## API Reference

### Layout Functions

#### `create_widget_panel(position, size, widgets, collapsible=True, title=None)`

Creates a flexible widget panel at the specified position.

**Parameters:**
- `position` (str): Panel position ("left", "right", "top", "bottom")
- `size` (str): Panel size (e.g., "300px", "150px")
- `widgets` (list): List of widget dictionaries
- `collapsible` (bool): Whether panel can be collapsed
- `title` (str): Optional panel title

#### `css_grid_layout(css_template)`

Creates a CSS Grid layout container.

**Parameters:**
- `css_template` (str): CSS grid template string

#### `grid_item(container_id, area_name, content_func)`

Adds content to a specific grid area.

**Parameters:**
- `container_id` (str): Grid container ID
- `area_name` (str): Grid area name
- `content_func` (callable): Function that renders content

#### `floating_panel(content, position="top-right", width="250px", height="150px", draggable=True)`

Creates a floating panel.

**Parameters:**
- `content` (callable): Content rendering function
- `position` (str): Panel position
- `width` (str): Panel width
- `height` (str): Panel height
- `draggable` (bool): Whether panel is draggable

### Component Functions

#### `card(title=None, content=None, icon=None, elevation=1, actions=None)`

Creates a card component.

**Parameters:**
- `title` (str): Card title
- `content` (str): Card content
- `icon` (str): Card icon
- `elevation` (int): Card elevation level
- `actions` (list): List of action buttons

#### `kpi_dashboard(kpis, columns=4)`

Creates a KPI dashboard.

**Parameters:**
- `kpis` (list): List of KPI dictionaries
- `columns` (int): Number of columns

#### `date_range_picker(label, presets=None, key=None)`

Creates a date range picker.

**Parameters:**
- `label` (str): Picker label
- `presets` (list): List of preset options
- `key` (str): Unique key

#### `multi_select(label, options, default=None, searchable=True, key=None)`

Creates an enhanced multi-select component.

**Parameters:**
- `label` (str): Component label
- `options` (list): Available options
- `default` (list): Default selected values
- `searchable` (bool): Whether options are searchable
- `key` (str): Unique key

### Theming Functions

#### `custom_theme(colors=None, fonts=None, spacing=None)`

Creates a custom theme.

**Parameters:**
- `colors` (dict): Color palette
- `fonts` (dict): Font definitions
- `spacing` (dict): Spacing scale

#### `set_theme(theme)`

Applies a theme to the application.

**Parameters:**
- `theme` (dict): Theme configuration

#### `toggle_dark_mode()`

Toggles between light and dark mode.

### Animation Functions

#### `fade_in(duration=300)`

Creates a fade-in animation wrapper.

**Parameters:**
- `duration` (int): Animation duration in milliseconds

#### `slide_left(duration=300)`

Creates a slide-left animation wrapper.

**Parameters:**
- `duration` (int): Animation duration in milliseconds

#### `skeleton_loader()`

Creates a skeleton loading animation wrapper.

#### `progress_indicator(message="Loading...")`

Creates a progress indicator wrapper.

**Parameters:**
- `message` (str): Loading message

### Utility Functions

#### `toast(message, type="info", duration=3000)`

Shows a toast notification.

**Parameters:**
- `message` (str): Toast message
- `type` (str): Toast type ("info", "success", "warning", "error")
- `duration` (int): Display duration in milliseconds

#### `confirm_dialog(title, message, confirm_text="OK", cancel_text="Cancel")`

Shows a confirmation dialog.

**Parameters:**
- `title` (str): Dialog title
- `message` (str): Dialog message
- `confirm_text` (str): Confirm button text
- `cancel_text` (str): Cancel button text

## Best Practices

### Layout Design

1. **Use flexible positioning sparingly** - Too many panels can overwhelm users
2. **Consider mobile users** - Test layouts on different screen sizes
3. **Maintain visual hierarchy** - Use appropriate panel sizes and positioning
4. **Group related widgets** - Place similar functionality together

### Performance

1. **Lazy load content** - Only render visible panels initially
2. **Use collapsible panels** - Reduce visual clutter
3. **Optimize animations** - Keep animation durations reasonable (200-400ms)
4. **Cache expensive operations** - Use Streamlit's caching for data processing

### Accessibility

1. **Keyboard navigation** - Ensure all interactive elements are keyboard accessible
2. **Screen readers** - Add appropriate ARIA labels and descriptions
3. **Color contrast** - Maintain WCAG AA compliance
4. **Focus management** - Provide clear focus indicators

### Theming

1. **Consistent color palette** - Use a cohesive color scheme
2. **Meaningful colors** - Use colors purposefully (red for errors, green for success)
3. **Dark mode support** - Test themes in both light and dark modes
4. **Brand alignment** - Match your organization's brand guidelines

## Troubleshooting

### Common Issues

**Widgets not appearing**: Check that the `content` functions are properly defined as lambdas or function references.

**Layout conflicts**: Ensure panel sizes don't overlap with main content. Use the `main-content` CSS class for proper margins.

**Theme not applying**: Call `stp.set_theme()` before rendering components.

**Animations not working**: Make sure you're using the animation wrappers correctly.

**Mobile responsiveness**: Test on actual mobile devices, not just browser dev tools.

### Debug Mode

Enable debug mode for additional logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

- **Documentation**: Check this README for detailed usage examples
- **Examples**: Run the demo apps in the `examples/` directory
- **Issues**: Report bugs on GitHub with minimal reproduction code
- **Discussions**: Join community discussions for tips and best practices

## Examples

Check out the `examples/` directory for complete working examples:

- `basic_app.py` - Basic Streamlit++ features
- `flexible_widgets.py` - Flexible widget positioning demo
- `analytics_dashboard.py` - Advanced dashboard with KPIs and charts
- `data_explorer.py` - Data exploration with enhanced tables
- `advanced_forms.py` - Complex form handling

Run any example with:

```bash
streamlit run examples/flexible_widgets.py
```

## Contributing

Contributions are welcome! Please see the contributing guidelines.

## License

MIT License