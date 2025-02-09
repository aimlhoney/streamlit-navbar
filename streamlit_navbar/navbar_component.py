import streamlit.components.v1 as components
import os

frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
_navbar_component = components.declare_component(
    "streamlit_navbar",
    path=frontend_dir
)


def navbar(links, app_name="My App", logo=None, style=None, key=None):
    return _navbar_component(
        links={"links": links, "app_name": {"text": app_name, "href": "/"}, "logo": logo, "style": style or {}},
        key=key
    )