## Streamlit Navbar Component
### Import
```python 
from streamlit_navbar.navbar_component import navbar
```
### Implementation
```python
selected_link = navbar(links=[
                {"text": "Home", "href": "/"},
                {"text": "Dashboard", "href": "/dashboard"},
                {"text": "About", "href": "/about"},
                {"text": "Contact", "href": "/contact"}
            ], logo=base64_string, app_name="Dataframe Components", style={
               "background_color":"#cccccc",
               "item_color":"white",
               "app_title_color":"white",
               "logo_height":"40px",
               "menu_size":20,
               "border_radius":"0px",
               "active_menu_color":"blue"
           })
```
### Control menu item click
```python
if selected_link:
  if selected_link == "/":
      st.subheader("Home")
  if selected_link == "/dashboard":
      st.subheader("Dashboard")

  if selected_link == "/about":
      st.subheader("About")
  if selected_link == "/contact":
      st.subheader("Contact")

else:
  st.subheader("Home")
```
### Images

### Demo
