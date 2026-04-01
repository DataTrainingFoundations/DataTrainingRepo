# Streamlit Interview & Review Questions (Data Engineering Focus)

## 1. What is Streamlit and when would you use it?

**Answer:**\
Streamlit is an open-source Python framework for building interactive
web apps quickly, especially for data applications.\
You'd use it to: - Prototype dashboards - Build internal tools for data
exploration - Expose ML models or pipelines to non-technical users

------------------------------------------------------------------------

## 2. How does Streamlit differ from traditional web frameworks?

**Answer:**\
- No need for HTML/CSS/JS\
- Script runs top-to-bottom on every interaction\
- Built-in UI components\
- Focused on data apps

------------------------------------------------------------------------

## 3. What happens when a user interacts with a widget?

**Answer:**\
Streamlit reruns the entire script from top to bottom.\
State is preserved using session state and caching.

------------------------------------------------------------------------

## 4. What is `st.session_state` and why is it important?

**Answer:**\
It allows you to persist variables across reruns.\
Used for: - Storing user inputs\
- Maintaining app state

------------------------------------------------------------------------

## 5. How do you improve performance in Streamlit apps?

**Answer:**\
Use caching: - `@st.cache_data` - `@st.cache_resource`

------------------------------------------------------------------------

## 6. How would you connect Streamlit to a database?

**Answer:**\
- Use Python connectors\
- Store credentials securely\
- Cache connections

------------------------------------------------------------------------

## 7. How do you handle secrets and credentials?

**Answer:**\
Use `.streamlit/secrets.toml` and access via `st.secrets`.

------------------------------------------------------------------------

## 8. What are common Streamlit widgets?

**Answer:**\
- button\
- selectbox\
- text_input\
- slider\
- file_uploader

------------------------------------------------------------------------

## 9. How would you build a data pipeline UI?

**Answer:**\
- Input\
- Processing trigger\
- Output display\
- Status/logging

------------------------------------------------------------------------

## 10. How does Streamlit integrate with data engineering tools?

**Answer:**\
- Trigger pipelines\
- Query warehouses\
- Visualize outputs

------------------------------------------------------------------------

## 11. What are limitations of Streamlit?

**Answer:**\
- Not ideal for large-scale apps\
- Limited frontend control\
- Rerun inefficiencies

------------------------------------------------------------------------

## 12. How can you deploy a Streamlit app?

**Answer:**\
- Streamlit Cloud\
- Docker\
- AWS/Azure/GCP

------------------------------------------------------------------------

## 13. How would you handle long-running tasks?

**Answer:**\
- Use spinners\
- Offload to background jobs\
- Poll for updates

------------------------------------------------------------------------

## 14. How can you structure a larger app?

**Answer:**\
- Modular code\
- Sidebar navigation\
- Pages directory

------------------------------------------------------------------------

## 15. How does Streamlit compare to BI tools?

**Answer:**\
- Streamlit = code-first, flexible\
- BI tools = drag-and-drop

------------------------------------------------------------------------

## 16. How would you visualize large datasets efficiently?

**Answer:**\
- Aggregate or sample\
- Cache results\
- Paginate tables

------------------------------------------------------------------------

## 17. What is Streamlit's role in data engineering?

**Answer:**\
- Presentation layer\
- Pipeline validation\
- Internal tooling

