"""
Advanced Theme Engine for Streamlit++

Provides comprehensive theming with light/dark modes, custom palettes, and design tokens.
"""

import streamlit as st
from typing import Dict, Any, Optional


class Theme:
    """Theme configuration class."""

    def __init__(self, name: str = "default", mode: str = "light"):
        self.name = name
        self.mode = mode
        self.colors = self._get_default_colors()
        self.typography = self._get_default_typography()
        self.spacing = self._get_default_spacing()

    def _get_default_colors(self) -> Dict[str, str]:
        if self.mode == "dark":
            return {
                "primary": "#007bff",
                "secondary": "#6c757d",
                "success": "#28a745",
                "danger": "#dc3545",
                "warning": "#ffc107",
                "info": "#17a2b8",
                "background": "#121212",
                "surface": "#1e1e1e",
                "text": "#ffffff",
                "text_secondary": "#b0b0b0"
            }
        else:
            return {
                "primary": "#007bff",
                "secondary": "#6c757d",
                "success": "#28a745",
                "danger": "#dc3545",
                "warning": "#ffc107",
                "info": "#17a2b8",
                "background": "#ffffff",
                "surface": "#f8f9fa",
                "text": "#212529",
                "text_secondary": "#6c757d"
            }

    def _get_default_typography(self) -> Dict[str, str]:
        return {
            "font_family": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
            "h1": "2.5rem",
            "h2": "2rem",
            "h3": "1.75rem",
            "h4": "1.5rem",
            "h5": "1.25rem",
            "h6": "1rem",
            "body": "1rem",
            "small": "0.875rem"
        }

    def _get_default_spacing(self) -> Dict[str, str]:
        return {
            "xs": "0.25rem",
            "sm": "0.5rem",
            "md": "1rem",
            "lg": "1.5rem",
            "xl": "3rem"
        }

    def apply(self):
        """Apply the theme to the Streamlit app."""
        css = f"""
        <style>
        :root {{
            --primary-color: {self.colors['primary']};
            --secondary-color: {self.colors['secondary']};
            --success-color: {self.colors['success']};
            --danger-color: {self.colors['danger']};
            --warning-color: {self.colors['warning']};
            --info-color: {self.colors['info']};
            --background-color: {self.colors['background']};
            --surface-color: {self.colors['surface']};
            --text-color: {self.colors['text']};
            --text-secondary-color: {self.colors['text_secondary']};
            --font-family: {self.typography['font_family']};
        }}

        body {{
            background-color: var(--background-color) !important;
            color: var(--text-color) !important;
            font-family: var(--font-family) !important;
        }}

        .stButton > button {{
            background-color: var(--primary-color) !important;
            color: white !important;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)


# Global theme instance
_current_theme = Theme()


def set_theme(theme: Theme):
    """Set the current theme."""
    global _current_theme
    _current_theme = theme
    _current_theme.apply()


def get_theme() -> Theme:
    """Get the current theme."""
    return _current_theme


def toggle_dark_mode():
    """Toggle between light and dark mode."""
    global _current_theme
    new_mode = "dark" if _current_theme.mode == "light" else "light"
    _current_theme = Theme(_current_theme.name, new_mode)
    _current_theme.apply()


def custom_theme(colors: Optional[Dict[str, str]] = None,
                typography: Optional[Dict[str, str]] = None,
                spacing: Optional[Dict[str, str]] = None) -> Theme:
    """
    Create a custom theme.

    Args:
        colors: Custom color palette
        typography: Custom typography settings
        spacing: Custom spacing settings

    Returns:
        Custom Theme instance
    """
    theme = Theme("custom", _current_theme.mode)
    if colors:
        theme.colors.update(colors)
    if typography:
        theme.typography.update(typography)
    if spacing:
        theme.spacing.update(spacing)
    return theme