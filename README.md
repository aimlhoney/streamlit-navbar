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
<img width="1057" alt="Screenshot 2025-02-16 at 2 21 04 PM" src="https://github.com/user-attachments/assets/781bc23d-eaa9-4186-873c-990c7965ea40" />

### Demo


https://github.com/user-attachments/assets/f4380287-9700-4d5f-af95-8f9b7558114a

