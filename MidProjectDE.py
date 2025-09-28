import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"data_mid_project_DE.csv")
st.sidebar.title("RETAIL STORE SALES")

info=st.sidebar.checkbox("Info",False)
describe=st.sidebar.checkbox("Describe",False)
data_show= st.sidebar.checkbox("Show Data",False)
missing_value=st.sidebar.checkbox("Missing Value",False)
edit_missing_value=st.sidebar.checkbox("Handling Missing Value",False)
statistic_outliers=st.sidebar.checkbox("Opreation Statistic Outliers",False)
view_boxplot= st.sidebar.checkbox("Show Box Plot ",False)
edit_outliers=st.sidebar.checkbox("Handling Outliers ")
data_object= st.sidebar.checkbox(" Handling Data Type Object",False)
if st.sidebar.button("SHOW"):
    if info:
        st.subheader("DATA INFO")
        df_info = {
       "Column": data.columns,   # name the columns 
       "Non-Null Count": data.notnull().sum().values,    # data not missing value
       "Dtype": data.dtypes.values  # type the data
           }     # creat data info 
        st.table(pd.DataFrame(df_info))   
        st.table(data.shape) # show row and columns
        
    elif describe:
        st.subheader("DATA DESCRIBE")
        st.table(data.describe())  # show the statistic the data
    elif data_show:
        st.subheader("DISPLAY THE DATA")  
        st.table(data)         #  show data
    elif missing_value:
        st.subheader("MISSING VALUE THE DATA")
        st.table(data.isna().sum())   # count missing value
    elif edit_missing_value:
        st.subheader("HANDLING MISSING VALUE IN THE DATA")
        data["Price Per Unit"].fillna(data["Price Per Unit"].mean(),inplace=True)  # handling in missing value
        data["Quantity"].fillna(data["Quantity"].mean(),inplace=True)
        data["Total Spent"].fillna(data["Total Spent"].mean(),inplace=True)
        data["Discount Applied"].fillna(data["Discount Applied"].mode()[0],inplace=True)
        st.table(data.isna().sum())  # count missing value after handling missing value
        st.table(data)   # show the data after missing value
    elif statistic_outliers:
        st.subheader("OUTLIERS")
        st.subheader("Price Per Unit")
        data["Price Per Unit"].fillna(data["Price Per Unit"].mean(),inplace=True)
        Q1_price_per_unit=data["Price Per Unit"].quantile(0.25)   #calculation  in Q1
        Q3_price_per_unit=data["Price Per Unit"].quantile(0.75)   # calculation  in Q3  
        IQR_price_per_unit= Q3_price_per_unit - Q1_price_per_unit  # calculation in IQR
        upper_bound_price_per_unit = Q3_price_per_unit + ( 1.5 * IQR_price_per_unit )  # calculation  upper bound
        lower_bound_price_per_unit = Q1_price_per_unit - ( 1.5 * IQR_price_per_unit )   #calculation  lower bound
        data_normal_price_per_unit=data[data["Price Per Unit"].between(lower_bound_price_per_unit,upper_bound_price_per_unit)]
        st.table(data_normal_price_per_unit.shape)

        st.subheader("Quantity")
        data["Quantity"].fillna(data["Quantity"].mean(),inplace=True)
        Q1_Quantity=data["Quantity"].quantile(0.25)
        Q3_Quantity=data["Quantity"].quantile(0.75)
        IQR_Quantity= Q3_Quantity - Q1_Quantity
        upper_bound_Quantity = Q3_Quantity +( 1.5 * IQR_Quantity )
        lower_bound_Quantity = Q1_Quantity -( 1.5 * IQR_Quantity )
        data_normal_Quantity=data[data["Quantity"].between(lower_bound_Quantity,upper_bound_Quantity)]
        st.table(data_normal_Quantity.shape)
        
        st.subheader("Total Spent")
        data["Total Spent"].fillna(data["Total Spent"].mean(),inplace=True)
        Q1_Total_Spent=data["Total Spent"].quantile(0.25)
        Q3_Total_Spent=data["Total Spent"].quantile(0.75)
        IQR_Total_Spent= Q3_Total_Spent - Q1_Total_Spent
        lower_bound_Total_Spent= Q1_Total_Spent - ( 1.5 * IQR_Total_Spent )
        upper_bound_Total_Spent= Q3_Total_Spent + ( 1.5 * IQR_Total_Spent )
        data_normal_Total_Spent= data[data["Total Spent"].between(lower_bound_Total_Spent,upper_bound_Total_Spent)]
        st.table(data_normal_Total_Spent.shape)
    elif view_boxplot:
        st.subheader("BOXPLOT")
        data["Total Spent"].fillna(data["Total Spent"].mean(),inplace=True)
        plt.figure(figsize=(10,4))  # size in chart
        sns.boxplot(data["Total Spent"])  # show data in box plot 
        st.pyplot(plt)
        
        data["Quantity"].fillna(data["Quantity"].mean(),inplace=True)
        plt.figure(figsize=(10,4))
        sns.boxplot(data["Quantity"])
        st.pyplot(plt)
        
        data["Price Per Unit"].fillna(data["Price Per Unit"].mean(),inplace=True)
        plt.figure(figsize=(10,4))
        sns.boxplot(data["Price Per Unit"])
        st.pyplot(plt)
        
    elif edit_outliers:
        st.subheader("HANDLING OUTLIERS DATA")
        st.subheader("Total Spent")
        data["Total Spent"].fillna(data["Total Spent"].mean(),inplace=True)
        Q1_Total_Spent=data["Total Spent"].quantile(0.25)
        Q3_Total_Spent=data["Total Spent"].quantile(0.75)
        IQR_Total_Spent= Q3_Total_Spent - Q1_Total_Spent
        lower_bound_Total_Spent= Q1_Total_Spent - ( 1.5 * IQR_Total_Spent )
        upper_bound_Total_Spent= Q3_Total_Spent + ( 1.5 * IQR_Total_Spent )
        # Handling outliers data 
        
        for i  in range(len(data["Total Spent"])):
            if data["Total Spent"][i]> upper_bound_Total_Spent:
                data["Total Spent"][i]=data["Total Spent"].mean()
            elif data["Total Spent"][i]< lower_bound_Total_Spent:
                data["Total Spent"][i]=data["Total Spent"].mean()
        st.table(data["Total Spent"].shape)
        
        
        plt.figure(figsize=(10,4))
        sns.boxplot(data["Total Spent"])
        st.pyplot(plt)
    elif data_object:
        st.subheader("HANDLING DATA TYPE OBJECT")
        # handling in data type object to int 
        data=pd.get_dummies(data,columns=["Payment Method","Location","Discount Applied"],dtype="int")
        st.table(data)
        