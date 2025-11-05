"""
Tests for Streamlit++ components.
"""

import pytest
from streamlit_plus.components import card, button
from streamlit_plus.themes import Theme


def test_theme_creation():
    """Test theme creation."""
    theme = Theme("test", "light")
    assert theme.name == "test"
    assert theme.mode == "light"
    assert "primary" in theme.colors


def test_custom_theme():
    """Test custom theme creation."""
    from streamlit_plus.themes import custom_theme
    custom = custom_theme(colors={"primary": "#ff0000"})
    assert custom.colors["primary"] == "#ff0000"


# Note: Testing Streamlit components requires special setup
# These are basic unit tests for now