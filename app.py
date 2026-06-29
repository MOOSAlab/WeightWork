import streamlit as st

st.set_page_config(
    page_title="WeightWork",
    page_icon='H.png',
    layout='centered'
)

st.title("WeightWork - Workout helper")   

st.divider()

namee = st.text_input("What's your name?")
if namee:
    st.success(f"Success - Hello, {namee}! 👋")

st.write("Warm-Up")
st.write("15 Jumping-Jacks")
st.write("1:00min Cobra pose")
st.write("2:00min Run")

st.divider()

st.write("Monday")
a=st.checkbox("25 Squats")
aa=st.checkbox("10 Right-Leg Lunges")
b=st.checkbox("10 Left-Leg Lunges")
bb=st.checkbox("15 Right-Leg RoundHouse kicks")
ab=st.checkbox("15 Left-Leg RoundHouse kicks")
ba=st.checkbox("30 Calf-Raises")
if a and aa and b and bb and ab and ba:
    st.info(f"Congratulation {namee} - You have completed Monday's plan")

st.divider()

st.write("Tuesday")
c=st.checkbox("25 Incline-Pushups")
cc=st.checkbox("10 Right-Hand Dummbell-Curls")
d=st.checkbox("10 Left-Hand Dumbell-Curls")
dd=st.checkbox("15 Jab Punches")
dc=st.checkbox("15 Cross Punches")
cd=st.checkbox("15 Hand-Raise [+weight]")
dcd=st.checkbox("1:00min DeadHang")
cdc=st.checkbox("10 Uppercut Punches")
ddc=st.checkbox("10 Hook Punches")
ccd=st.checkbox("15 Right-Wrisk Curls")
ccc=st.checkbox("15 Left-Wrisk Curls")
if c and cc and d and dd and dc and cd and dcd and cdc and ddc and ccd and ccc:
    st.info(f"Congratulation {namee} - You have completed Tuesday's plan")

st.divider()

st.write("Wednesday")
e=st.checkbox("2:00min plank")
ee=st.checkbox("10 Pushups")
f=st.checkbox("10 Leg-Raises")
ff=st.checkbox("15 Russian-Dips")
fe=st.checkbox("15 Mountain Climbers")
ef=st.checkbox("30 Bicycle-Crunches")
if e and ee and f and ff and fe and ef:
    st.info(f"Congratulation {namee} - You have completed Wednesday's plan")

st.divider()

st.write("Thursday - Cardio💪Time🕐")
g=st.checkbox("5:00min Sprinting")
gg=st.checkbox("1:00min High Knees")
h=st.checkbox("25 Jump-Rope")
if g and gg and h:
    st.info(f"Congratulation {namee} - You have completed Cardio")

st.divider()

st.write("Friday - To-do Goal Time🕘")
st.write("To-do List")

name = st.text_input("What are your goals [1/3]", key='Que')
nam = st.text_input("What are your goals [2/3]", key='Ones')
ame = st.text_input("What are your goals [3/3]", key='more')

if name and nam and ame:
    st.checkbox(name, key="Goque")
    st.checkbox(nam, key="Raplaque")
    st.checkbox(ame, key="Dolerdolem")

st.divider()

st.write("Rest on Sundays and complete your To-do Deadline : Saturday-8:00PM")
st.write("Remember, You are not Exercising for Mucles, You are exercising for your streanth and your fitness,Be consistant")

st.divider()

st.write("BodyMass Calculator")
x = st.text_input("Enter name of the person", key="bmi_name")
a_bmi = st.number_input(f"{x}, Enter your weight [Kg]", min_value=0.0, key="weight")
b_bmi = st.number_input(f"{x}, Enter your height [ft]", min_value=0.0, key="height")
z = b_bmi * 0.3048

if a_bmi and z:
    st.success("Input received, wait some time")
    bmi = a_bmi / (z ** 2)  
    if st.button("Calculate"):
        st.info(f"{x}'s Body Mass Index = {bmi:.2f}")
    if bmi >= 25:
        st.write("Overweight")
    elif bmi >= 18.5:
        st.write("Normal")
    elif bmi < 18.5: 
        st.write("Underweight")

st.divider()

st.write("Baseline Energy Needs[BMR]")
w = st.selectbox('Gender', ['Male', 'Female']) 

if w == 'Male':
    waitmen = st.number_input("Enter your weight[kg]", min_value=0.0, key="mweight") 
    hietmen = st.number_input("Enter height[ft]", min_value=0.0, key="mheight")
    agemen = st.number_input("Enter your age", min_value=0, key="mage")
    hatmen = hietmen * 0.3048 * 100 
    manbmr = (10 * waitmen) + (6.25 * hatmen) - (5 * agemen) + 5
    if waitmen and hatmen and agemen:
     st.success(f"Your BMR is {manbmr:.2f}")

if w == 'Female':
    waitwomen = st.number_input("Enter your weight[kg]", min_value=0.0, key="fweight") 
    hietwomen = st.number_input("Enter height[ft]", min_value=0.0, key="fheight")
    agewomen = st.number_input("Enter your age", min_value=0, key="fage")
    hatwomen = hietwomen * 0.3048 * 100 
    womanbmr = (10 * waitwomen) + (6.25 * hatwomen) - (5 * agewomen) - 161
    if waitwomen and hatwomen and agewomen:
     st.success(f"Your BMR is {womanbmr:.2f}")

st.divider()

mood = st.radio(
    "How are you feeling?",
    ["😊 Happy","😴 Sleepy","😎 Cool","😢 Sad","😡 Angry","😖 Stressed"]
)
if mood=="😊 Happy":
    st.code("If you are happy, make others happy as its a Good-deed")
elif mood=="😴 Sleepy":
    st.code("You know that laziness is like a rust for humans, be consistant and work even if you dont want to because consistancy leads to success")
elif mood=="😎 Cool":
    st.code("One thing everyone does in this mood,Pride,When your proud of yourself dont feel Pride,Pride is like a drug which make you feel better but hurts your social interactions and relationships")
elif mood=="😢 Sad":
    st.code("If your feeling sad,thats ok,but being sad is an action,even the strong one cries but they move on,So never give up")
elif mood=="😡 Angry":
    st.code("Anger is normal,but not controlling it isn't,When you feel angry take a deep breath 10 times and dont talk to anyone because in anger you can cross any limit")
elif mood=="😖 Stressed":
    st.code("If you feel stressed than think about it,your stressed about Work,any kind of work,If you can do it then why worry about it,and if you cant then find a path to do it")
else:
    st.error("Invailid input")