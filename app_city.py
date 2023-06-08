### New App For City Estimator  ###
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split, cross_val_score

import streamlit as st

#### Page Config ###
st.set_page_config(
    page_title="European City Estimator",
    page_icon="https://img.freepik.com/free-vector/illustration-european-union-flag_53876-27018.jpg?w=360",
    menu_items={
        "Get help": "mailto:hikmetemreguler@gmail.com",
        "About": "For More Information\n" + "https://github.com/HikmetEmre/City_Estimator"
    }
)

### Title of Project ###
st.title("**:red[European City Estimator: Personalized Recommendations for Your Ideal City to Live.]** ")

### Markdown ###
st.markdown("**Introducing a remarkable :blue[European City Estimator] An innovative recommendation system project that unveils the perfect city to embrace the European lifestyle!**.")

### Adding Image ###
st.image("https://raw.githubusercontent.com/HikmetEmre/City_Estimator/main/image%20first.jpg")

st.markdown("**The :blue[European City Estimator] is a recommendation system that suggests European cities to users based on their preferences and requirements. It collects real-life data through web scraping from local websites, including information on rent, deposit, average salary, job opportunities, weather, city conditions, population, entertainment, traffic, and more.**")
st.markdown("**For this project, I collected 50,805 rental houses data from local websites using web scraping techniques and analysed the average rent prices across 16 European cities.**")
st.markdown("**Using this data, the system calculates similarity scores between user input and existing cities, allowing it to recommend cities that closely match the user's preferences.**")
st.markdown("**Overall, the system assists users in making informed decisions about which :yellow[European City] to live in.**")
st.markdown("*Alright, Let's Have A Trip To Europe!*")

st.image("https://raw.githubusercontent.com/HikmetEmre/City_Estimator/main/second%20imagee.jpg")

#### Header and definition of columns ###
st.header("**META DATA**")

st.markdown("- **Rent**: Renting Cost of Flat in Euros.")
st.markdown("- **Deposit**: Safety Deposit Cost of Flat in Euros.")
st.markdown("- **Avg_Salary**: Monthly Payment of Software Engineer in Euros.")
st.markdown("- **Job_Opp**: Number of Open Jobs For Software Engineer Position.")
st.markdown("- **Weather**: Year-round Weather Conditions for the City.")
st.markdown("- **City_Cond**: Overall ambiance and environment of the cities, ranging from peaceful havens to bustling urban centers.")
st.markdown("- **People**: Reflects the sociability and demeanor of the inhabitants, spanning from friendly communities to a more neutral social atmosphere.")
st.markdown("- **Entertainment**: The availability and level of recreational activities, with options ranging from moderate offerings to abundant high-quality entertainment.")
st.markdown("- **Traffic**: Represents the congestion and flow of vehicular movement in the cities, encompassing varying levels from manageable traffic to high-density conditions.")
st.markdown("- **Population**: Indicates the size and density of residents in the cities, encompassing a range from low population areas to high-density urban centers.")
st.markdown("- **City**: Name of The City.")



st.image('https://previews.123rf.com/images/muchmaniavector/muchmaniavector1909/muchmaniavector190900058/130990193-europe-countries-landmarks-silhouette-famous-place-and-historical-buildings-travel-and-tourist.jpg')


### Example DF ON STREAMLIT PAGE ###
df=pd.read_csv("streamlit_app.csv")


### Example TABLE ###
st.table(df.sample(5, random_state=17))


#---------------------------------------------------------------------------------------------------------------------

### Sidebar Markdown ###
st.sidebar.markdown("**INPUT** Your **:red[Preferences]**  **for Choosing a City to Live In**")

### Define Sidebar Input's ###
Rent = st.sidebar.number_input("**Your expected rent cost in Euros.**", min_value=0)
Deposit = st.sidebar.number_input("**Your expected safety deposit cost in Euros..**", min_value=0)
Exp_Salary = st.sidebar.number_input("**Your expected salary in Euros.**", min_value=0)
Job_Opp = st.sidebar.text_input("**Job Oppurtunities :green[High] ,:blue[Moderate], :red[Low]**")
Weather = st.sidebar.text_input("**Weather Condition :green[Good] ,:blue[Moderate], :red[Bad]**")
City_Cond = st.sidebar.text_input("**Ambiance and Environment :green[Peaceful] or :red[Crowded]**")
People = st.sidebar.text_input("Attitude of Local People :green[Friendly] or blue[Neutral]**")
Entertainment = st.sidebar.text_input("** Availablitiy of Activities And Level :green[High] ,:blue[Moderate]**")
Traffic = st.sidebar.text_input("**Traffic Condition :green[Good], :blue[Moderate], :red[Bad]**")
Population = st.sidebar.text_input("** Density of residents in city :red[High] or :blue[Low]**")


#---------------------------------------------------------------------------------------------------------------------


user_input = pd.DataFrame({
    'Rent': [Rent],
    'Deposit': [Deposit],
    'Avg_Salary': [Exp_Salary] ,
    'Job_Opp': [Job_Opp],
    'Weather': [Weather],
    'City_Cond': [City_Cond],
    'People': [People],
    'Entertainment': [Entertainment],
    'Traffic': [Traffic],
    'Population': [Population],
  })
    
# Check if user input is empty
if user_input.empty:
    st.write("Please fill in the required information.")
else:
    # Concatenate user input with the original DataFrame
    combined_df = pd.concat([df, user_input], ignore_index=True)

    # Perform one-hot encoding on categorical features
    combined_df_encoded = pd.get_dummies(combined_df, drop_first=True)

    # Calculate cosine similarity between user input and cities
    similarity_matrix = cosine_similarity(combined_df_encoded)

    # Get the similarity scores for the user input
    user_similarity_scores = similarity_matrix[-1, :-1]

    # Sort the cities based on similarity scores
    similar_cities_indices = user_similarity_scores.argsort()[::-1][:3]
    similar_cities = df.iloc[similar_cities_indices]['City']


recommended_cities = []
for city in similar_cities:
    recommended_cities.append(city)

result = recommended_cities





#---------------------------------------------------------------------------------------------------------------------

st.header("Results")

### Result Screen ###
if st.sidebar.button("Submit"):

    ### Info message ###
    st.info("You can find the result below.")

    ### Inquiry Time Info ###
    from datetime import date, datetime

    today = date.today()
    time = datetime.now().strftime("%H:%M:%S")

    ### For showing results create a df ###
    results_df = pd.DataFrame({
    'Date': [today],
    'Time': [time],
    'Rent': [Rent],
    'Deposit': [Deposit],
    'Avg_Salary': [Exp_Salary] ,
    'Job_Opp': [Job_Opp],
    'Weather': [Weather],
    'City_Cond': [City_Cond],
    'People': [People],
    'Entertainment': [Entertainment],
    'Traffic': [Traffic],
    'Population': [Population],
    'Recomemnded Cities' : [result]
  })
   


    st.table(result)

if result is not None:
    st.table(result)
    st.image('https://raw.githubusercontent.com/HikmetEmre/City_Estimator/main/last%20image!.jpg')
else:
    st.markdown("Please click the **Submit Button!**")

