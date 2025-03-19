import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit UI
st.title("Dynamic Data Visualization")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data:")
    st.write(df.head())
    
    # Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if categorical_cols and numerical_cols:
        category_col = st.selectbox("Select a Categorical Column", categorical_cols)
        numeric_col = st.selectbox("Select a Numerical Column", numerical_cols)
        
        # Bar Chart
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        sns.barplot(x=df[category_col], y=df[numeric_col], palette='viridis', ax=ax)
        ax.set_xlabel(category_col)
        ax.set_ylabel(numeric_col)
        ax.set_title(f"{numeric_col} per {category_col}")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
        
        # Column Chart
        st.subheader("Column Chart")
        fig, ax = plt.subplots()
        sns.barplot(y=df[numeric_col], x=df[category_col], palette='coolwarm', ax=ax)
        ax.set_xlabel(category_col)
        ax.set_ylabel(numeric_col)
        ax.set_title(f"{numeric_col} per {category_col}")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
        
        # Pie Chart
        st.subheader("Pie Chart")
        fig, ax = plt.subplots()
        colors = sns.color_palette('pastel')
        ax.pie(df[numeric_col], labels=df[category_col], autopct='%1.1f%%', colors=colors, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
        ax.set_title(f"Proportion of {numeric_col} per {category_col}")
        st.pyplot(fig)
        
        # Donut Chart
        st.subheader("Donut Chart")
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(df[numeric_col], labels=df[category_col], autopct='%1.1f%%', colors=sns.color_palette('Set2'), wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig.gca().add_artist(centre_circle)
        ax.set_title(f"Donut Chart of {numeric_col} per {category_col}")
        st.pyplot(fig)
        
    else:
        st.error("Ensure your dataset contains both categorical and numerical columns.")
