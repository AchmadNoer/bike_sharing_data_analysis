import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

sns.set(style='white')

bike_data = pd.read_csv("./streamlit/hour.csv")

bike_data.drop(['instant', 'dteday', 'atemp'], axis=1, inplace=True)
bike_data.columns = ['season', 'year', 'month', 'hour', 'is_holiday', 'day', 'is_workingday',
                     'weather', 'temperature', 'humidity', 'wind_speed', 'user_casual', 'user_registered', 'user_count']
bike_data = bike_data.reindex(columns=['hour', 'day', 'month', 'year', 'is_holiday', 'is_workingday', 'season',
                              'weather', 'temperature', 'humidity', 'wind_speed', 'user_casual', 'user_registered', 'user_count'])

bike_data["is_holiday"] = bike_data["is_holiday"].astype("boolean")
bike_data["is_workingday"] = bike_data["is_workingday"].astype("boolean")

bike_data["day"].replace({0: "Sun", 1: "Mon", 2: "Tue",
                         3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}, inplace=True)
bike_data["month"].replace({1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                           7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}, inplace=True)
bike_data["year"].replace({0: "2011", 1: "2012"}, inplace=True)
bike_data["season"].replace(
    {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}, inplace=True)
bike_data["weather"].replace(
    {1: "Clear", 2: "Cloudy", 3: "Light Rain", 4: "Heavy Rain"}, inplace=True)

bike_data["day"] = pd.Categorical(bike_data["day"], categories=[
                                  "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], ordered=True)
bike_data["month"] = pd.Categorical(bike_data["month"], categories=[
                                    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ordered=True)
bike_data["year"] = pd.Categorical(bike_data["year"], categories=[
                                   "2011", "2012"], ordered=True)

st.header("Bike Sharing Data")
st.subheader("Average Bike User")

tab_user_hourly, tab_user_daily, tab_user_monthly, tab_user_yearly = st.tabs(
    ["Hourly", "Daily", "Monthly", "Yearly"])

with tab_user_hourly:
    plt.figure(figsize=(10, 5))
    sns.barplot(data=bike_data, x='hour', y='user_count')
    plt.ylabel('')
    plt.xlabel("Hour")
    st.pyplot(plt)

with tab_user_daily:
    plt.figure(figsize=(10, 5))
    sns.barplot(data=bike_data, x='day', y='user_count')
    plt.ylabel('')
    plt.xlabel("Day")
    st.pyplot(plt)

with tab_user_monthly:
    plt.figure(figsize=(10, 5))
    sns.barplot(data=bike_data, x='month', y='user_count')
    plt.ylabel('')
    plt.xlabel("Month")
    st.pyplot(plt)

with tab_user_yearly:
    plt.figure(figsize=(10, 5))
    sns.barplot(data=bike_data, x='year', y='user_count')
    plt.ylabel('')
    plt.xlabel("Year")
    st.pyplot(plt)

st.subheader("Number of Bike Users by Category")

tab_usertype_hourly, tab_usertype_daily, tab_usertype_monthly, tab_usertype_yearly = st.tabs(
    ["Hourly", "Daily", "Monthly", "Yearly"])

with tab_usertype_hourly:

    col_max_hourly, col_min_hourly, col_avg_hourly = st.columns(3)

    with col_max_hourly:
        max_hourly = bike_data.groupby(by="hour").user_count.sum().max()
        st.metric("Max User:", f"{max_hourly:n}")

    with col_min_hourly:
        min_hourly = bike_data.groupby(by="hour").user_count.sum().min()
        st.metric("Min User:", f"{min_hourly:n}")

    with col_avg_hourly:
        avg_hourly = bike_data.groupby(
            by="hour").user_count.sum().mean().astype("int64")
        st.metric("Avg User:", f"{avg_hourly:n}")

    bike_data.groupby(by="hour")[["user_casual", "user_registered"]].sum().plot(
        kind="bar", stacked=True, color=["blue", "red"], figsize=(10, 5), rot=0).legend(["Casual", "Registered"], loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)
    plt.ylabel('Total User')
    plt.xlabel("Hour")
    st.pyplot(plt)

with tab_usertype_daily:

    col_max_daily, col_min_daily, col_avg_daily = st.columns(3)

    with col_max_daily:
        max_daily = bike_data.groupby(by="day").user_count.sum().max()
        st.metric("Max User:", f"{max_daily:n}")

    with col_min_daily:
        min_daily = bike_data.groupby(by="day").user_count.sum().min()
        st.metric("Min User:", f"{min_daily:n}")

    with col_avg_daily:
        avg_daily = bike_data.groupby(
            by="day").user_count.sum().mean().astype("int64")
        st.metric("Avg User:", f"{avg_daily:n}")

    bike_data.groupby(by="day")[["user_casual", "user_registered"]].sum().plot(
        kind="bar", stacked=True, color=["blue", "red"], figsize=(10, 5), rot=0).legend(["Casual", "Registered"], loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)
    plt.ylabel('Total User')
    plt.xlabel("Day")
    st.pyplot(plt)

with tab_usertype_monthly:

    col_max_monthly, col_min_monthly, col_avg_monthly = st.columns(3)

    with col_max_monthly:
        max_monthly = bike_data.groupby(by="month").user_count.sum().max()
        st.metric("Max User:", f"{max_monthly:n}")

    with col_min_monthly:
        min_monthly = bike_data.groupby(by="month").user_count.sum().min()
        st.metric("Min User:", f"{min_monthly:n}")

    with col_avg_monthly:
        avg_monthly = bike_data.groupby(
            by="month").user_count.sum().mean().astype("int64")
        st.metric("Avg User:", f"{avg_monthly:n}")

    bike_data.groupby(by="month")[["user_casual", "user_registered"]].sum().plot(
        kind="bar", stacked=True, color=["blue", "red"], figsize=(10, 5), rot=0).legend(["Casual", "Registered"], loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)
    plt.ylabel('Total User')
    plt.xlabel("Month")
    st.pyplot(plt)

with tab_usertype_yearly:

    col_max_monthly, col_min_monthly = st.columns(2)

    with col_max_monthly:
        yearly_2011 = bike_data.groupby(by="year").user_count.sum()["2011"]
        st.metric("Users in 2011:", f"{yearly_2011:n}")

    with col_min_monthly:
        yearly_2012 = bike_data.groupby(by="year").user_count.sum()["2012"]
        st.metric("Users in 2012:", f"{yearly_2012:n}")

    bike_data.groupby(by="year")[["user_casual", "user_registered"]].sum().plot(
        kind="bar", stacked=True, color=["blue", "red"], figsize=(10, 5), rot=0).legend(["Casual", "Registered"], loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)
    plt.ylabel('Total User')
    plt.xlabel("Year")
    st.pyplot(plt)

st.subheader("Bike Users to Climatological Conditions")

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))
fig.tight_layout(pad=(5))
sns.histplot(data=bike_data, x="temperature", ax=ax[0], bins=20, kde=True)
ax[0].set_ylabel('')
ax[0].set_xlabel("Temperature")

sns.histplot(data=bike_data, x="humidity", ax=ax[1], bins=20, kde=True)
ax[1].set_ylabel('')
ax[1].set_xlabel("Humidity")

sns.histplot(data=bike_data, x="wind_speed", ax=ax[2], bins=20, kde=True)
ax[2].set_ylabel('')
ax[2].set_xlabel("Wind Speed")

st.pyplot(fig)

with st.sidebar:

    st.header("BIKE SHARING DATA ANALYSIS")
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">🚲🚲</p>', unsafe_allow_html=True)
    st.write("Made by Achmad Noer Aziz")

    link1, link2, link3 = st.columns(3)
    with link1:
        st.write(f"[Kaggle]({'https://www.kaggle.com/achmadnoer'})")
    with link2:
        st.write(f"[Github]({'https://github.com/AchmadNoer'})")
    with link3:
        st.write(
            f"[Dicoding]({'https://www.dicoding.com/users/achmadnoer/academies'})")
