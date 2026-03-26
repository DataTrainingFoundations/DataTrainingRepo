#pip install snowflake-connector-python
#pip install streamlit
#pip install pandas

import streamlit as st
import pandas as pd
import snowflake.connector

st.title("Snowflake + Streamlit with Secrets")

# Load Snowflake credentials from Streamlit secrets
sf_creds = st.secrets["snowflake"]

# Optional: let user type query
query = st.text_area("", value="")

if st.button("Run Query"):
    try:
        # Connect to Snowflake using secrets
        conn = snowflake.connector.connect(
            user=sf_creds["user"],
            password=sf_creds["password"],
            account=sf_creds["account"],
            warehouse=sf_creds["warehouse"],
            database=sf_creds["database"],
            schema=sf_creds["schema"]
        )

        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cols = [col[0] for col in cur.description]

        # Display results
        df = pd.DataFrame(data, columns=cols)
        st.dataframe(df)

        # Cleanup
        cur.close()
        conn.close()

    except Exception as e:
        st.error(f"Error: {e}")