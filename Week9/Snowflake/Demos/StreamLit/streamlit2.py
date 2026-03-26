import streamlit as st
import pandas as pd
import snowflake.connector


# --Create table
# CREATE OR REPLACE TABLE my_table (
#     id INT,
#     name STRING,
#     created_at TIMESTAMP
# );

# -- Create internal stage
# CREATE OR REPLACE STAGE my_stage;

# -- (Optional) verify
# LIST @my_stage;


st.title("Snowflake + Streamlit (PUT + Query)")

# Load Snowflake credentials from Streamlit secrets
sf_creds = st.secrets["snowflake"]

# File path input (local to where Streamlit runs)
file_path = st.text_input("Local file path", value="./data.csv")

# Query input
query = st.text_area("Query", value="SELECT * FROM my_table")

if st.button("Upload + Load + Query"):
    try:
        conn = snowflake.connector.connect(
            user=sf_creds["user"],
            password=sf_creds["password"],
            account=sf_creds["account"],
            warehouse=sf_creds["warehouse"],
            database=sf_creds["database"],
            schema=sf_creds["schema"]
        )

        cur = conn.cursor()

        # Step 1: PUT file into stage
        put_sql = f"PUT file://{file_path} @my_stage AUTO_COMPRESS=TRUE"
        st.write("Running PUT...")
        cur.execute(put_sql)

        # Step 2: COPY INTO table
        copy_sql = """
        COPY INTO my_table
        FROM @my_stage
        FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1)
        """
        st.write("Running COPY INTO...")
        cur.execute(copy_sql)

        # Step 3: Run user query
        st.write("Running Query...")
        cur.execute(query)

        data = cur.fetchall()
        cols = [col[0] for col in cur.description]

        df = pd.DataFrame(data, columns=cols)
        st.dataframe(df)

        cur.close()
        conn.close()

    except Exception as e:
        st.error(f"Error: {e}")