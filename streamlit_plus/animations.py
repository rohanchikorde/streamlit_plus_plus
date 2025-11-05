"""
Animations and Transitions for Streamlit++

Provides micro-interactions, page transitions, element animations, and loading states.
"""

import streamlit as st
from typing import Optional, List, Dict, Any, Callable
import time
import uuid


def fade_in(content: Any, duration: float = 0.5, delay: float = 0, **kwargs):
    """
    Apply fade-in animation to content.

    Args:
        content: Content to animate
        duration: Animation duration in seconds
        delay: Animation delay in seconds
        **kwargs: Additional styling
    """
    element_id = f"fade-in-{uuid.uuid4().hex[:8]}"
    anim_name = f"fadeIn{element_id.replace('-', '')}"

    style = f"""
    <style>
    @keyframes {anim_name} {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    #{element_id} {{
        animation: {anim_name} {duration}s ease-in-out {delay}s both;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{element_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def slide_in(content: Any, direction: str = "up", duration: float = 0.5, delay: float = 0, **kwargs):
    """
    Apply slide-in animation to content.

    Args:
        content: Content to animate
        direction: 'up', 'down', 'left', 'right'
        duration: Animation duration in seconds
        delay: Animation delay in seconds
        **kwargs: Additional styling
    """
    element_id = f"slide-in-{uuid.uuid4().hex[:8]}"
    anim_name = f"slideIn{element_id.replace('-', '')}"

    transforms = {
        "up": "translateY(20px)",
        "down": "translateY(-20px)",
        "left": "translateX(20px)",
        "right": "translateX(-20px)"
    }

    style = f"""
    <style>
    @keyframes {anim_name} {{
        from {{
            opacity: 0;
            transform: {transforms.get(direction, transforms['up'])};
        }}
        to {{
            opacity: 1;
            transform: translate(0);
        }}
    }}
    #{element_id} {{
        animation: {anim_name} {duration}s ease-out {delay}s both;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{element_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def bounce_in(content: Any, duration: float = 0.8, delay: float = 0, **kwargs):
    """
    Apply bounce-in animation to content.

    Args:
        content: Content to animate
        duration: Animation duration in seconds
        delay: Animation delay in seconds
        **kwargs: Additional styling
    """
    element_id = f"bounce-in-{uuid.uuid4().hex[:8]}"
    anim_name = f"bounceIn{element_id.replace('-', '')}"

    style = f"""
    <style>
    @keyframes {anim_name} {{
        0% {{
            opacity: 0;
            transform: scale(0.3);
        }}
        50% {{
            opacity: 1;
            transform: scale(1.05);
        }}
        70% {{
            transform: scale(0.9);
        }}
        100% {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    #{element_id} {{
        animation: {anim_name} {duration}s ease-out {delay}s both;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{element_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def pulse(content: Any, duration: float = 2, **kwargs):
    """
    Apply continuous pulse animation to content.

    Args:
        content: Content to animate
        duration: Animation duration in seconds
        **kwargs: Additional styling
    """
    element_id = f"pulse-{uuid.uuid4().hex[:8]}"
    anim_name = f"pulse{element_id.replace('-', '')}"

    style = f"""
    <style>
    @keyframes {anim_name} {{
        0% {{
            transform: scale(1);
        }}
        50% {{
            transform: scale(1.05);
        }}
        100% {{
            transform: scale(1);
        }}
    }}
    #{element_id} {{
        animation: {anim_name} {duration}s ease-in-out infinite;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{element_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def loading_spinner(size: str = "medium", color: str = "primary", **kwargs):
    """
    Create a loading spinner.

    Args:
        size: 'small', 'medium', 'large'
        color: Spinner color
        **kwargs: Additional styling
    """
    sizes = {
        "small": "width: 20px; height: 20px; border-width: 2px;",
        "medium": "width: 40px; height: 40px; border-width: 4px;",
        "large": "width: 60px; height: 60px; border-width: 6px;"
    }

    colors = {
        "primary": "var(--primary-color, #007bff)",
        "secondary": "var(--secondary-color, #6c757d)",
        "success": "var(--success-color, #28a745)",
        "danger": "var(--danger-color, #dc3545)"
    }

    spinner_id = f"spinner-{uuid.uuid4().hex[:8]}"
    anim_name = f"spin{spinner_id.replace('-', '')}"

    style = f"""
    <style>
    #{spinner_id} {{
        {sizes.get(size, sizes['medium'])}
        border: {colors.get(color, colors['primary'])} solid;
        border-top: transparent solid;
        border-radius: 50%;
        animation: {anim_name} 1s linear infinite;
        display: inline-block;
        margin: 1rem;
    }}
    @keyframes {anim_name} {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{spinner_id}"></div>', unsafe_allow_html=True)


def skeleton_loader(width: str = "100%", height: str = "20px", **kwargs):
    """
    Create a skeleton loading placeholder.

    Args:
        width: Skeleton width
        height: Skeleton height
        **kwargs: Additional styling
    """
    skeleton_id = f"skeleton-{uuid.uuid4().hex[:8]}"
    anim_name = f"loading{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{skeleton_id} {{
        width: {width};
        height: {height};
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 200% 100%;
        animation: {anim_name} 1.5s infinite;
        border-radius: 4px;
        margin: 0.5rem 0;
    }}
    @keyframes {anim_name} {{
        0% {{
            background-position: 200% 0;
        }}
        100% {{
            background-position: -200% 0;
        }}
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{skeleton_id}"></div>', unsafe_allow_html=True)


def shimmer_effect(content: Any, **kwargs):
    """
    Apply shimmer loading effect to content.

    Args:
        content: Content to apply shimmer to
        **kwargs: Additional styling
    """
    shimmer_id = f"shimmer-{uuid.uuid4().hex[:8]}"
    anim_name = f"shimmer{uuid.uuid4().hex[:8]}"

    style = f"""
    <style>
    #{shimmer_id} {{
        position: relative;
        overflow: hidden;
    }}
    #{shimmer_id}::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: {anim_name} 1.5s infinite;
    }}
    @keyframes {anim_name} {{
        0% {{
            left: -100%;
        }}
        100% {{
            left: 100%;
        }}
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{shimmer_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def animate_on_scroll(content: Any, animation_type: str = "fade-in", threshold: float = 0.1, **kwargs):
    """
    Animate content when it comes into viewport (simplified version).

    Args:
        content: Content to animate
        animation_type: Type of animation
        threshold: Scroll threshold
        **kwargs: Additional options
    """
    # Note: Full scroll-triggered animation requires JavaScript
    # This is a simplified version that just applies the animation
    if animation_type == "fade-in":
        fade_in(content, **kwargs)
    elif animation_type == "slide-in":
        slide_in(content, **kwargs)
    elif animation_type == "bounce-in":
        bounce_in(content, **kwargs)
    else:
        content()


def page_transition(content: Any, transition_type: str = "fade", duration: float = 0.3, **kwargs):
    """
    Apply page transition effect.

    Args:
        content: Page content
        transition_type: 'fade', 'slide', 'scale'
        duration: Transition duration
        **kwargs: Additional options
    """
    transition_id = f"transition-{uuid.uuid4().hex[:8]}"

    if transition_type == "fade":
        anim_name = f"pageFade{int(duration * 1000)}"
        style = f"""
        <style>
        #{transition_id} {{
            animation: {anim_name} {duration}s ease-in-out;
        }}
        @keyframes {anim_name} {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        </style>
        """
    elif transition_type == "slide":
        anim_name = f"pageSlide{int(duration * 1000)}"
        style = f"""
        <style>
        #{transition_id} {{
            animation: {anim_name} {duration}s ease-out;
        }}
        @keyframes {anim_name} {{
            from {{ transform: translateX(100%); opacity: 0; }}
            to {{ transform: translateX(0); opacity: 1; }}
        }}
        </style>
        """
    elif transition_type == "scale":
        anim_name = f"pageScale{int(duration * 1000)}"
        style = f"""
        <style>
        #{transition_id} {{
            animation: {anim_name} {duration}s ease-out;
        }}
        @keyframes {anim_name} {{
            from {{ transform: scale(0.9); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}
        </style>
        """
    else:
        style = ""

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(f'<div id="{transition_id}">', unsafe_allow_html=True)
    content()
    st.markdown('</div>', unsafe_allow_html=True)


def counter_animation(start: int, end: int, duration: float = 2, prefix: str = "", suffix: str = "", **kwargs):
    """
    Animate a number counter.

    Args:
        start: Starting number
        end: Ending number
        duration: Animation duration in seconds
        prefix: Text prefix
        suffix: Text suffix
        **kwargs: Additional options
    """
    counter_id = f"counter-{uuid.uuid4().hex[:8]}"

    # For simplicity, we'll just display the end value
    # A full implementation would use JavaScript for smooth counting
    st.markdown(f"""
    <div id="{counter_id}" style="
        font-size: 2rem;
        font-weight: bold;
        color: var(--primary-color, #007bff);
        display: inline-block;
    ">
        {prefix}{end}{suffix}
    </div>
    """, unsafe_allow_html=True)