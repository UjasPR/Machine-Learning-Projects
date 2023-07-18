import streamlit as st
import pickle
import pandas as pd

st.title('Car Price Prediction')

company = ['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford', 'Hindustan', 'Honda', 'Hyundai', 'Jaguar',  'Jeep', 'Land', 'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']
fuel_type = ['Diesel', 'LPG', 'Petrol']
car_model = ['Santro Xing', 'Jeep CL550', 'Grand i10', 'EcoSport Titanium', 'Figo', 'Eon', 'EcoSport Ambiente', 'Suzuki Alto', 'Fabia Classic', 'Suzuki Stingray', 'Elite i20', 'Scorpio SLE', 'A8', 'Q7', 'Scorpio S10', 'i20 Sportz', 'Suzuki Vitara', 'Bolero DI', 'Suzuki Swift', 'Suzuki Wagon', 'Innova 2.0', 'Lodgy 85', 'Yeti Ambition', 'Suzuki Baleno', 'Duster 110', 'Duster 85', 'City 1.5', 'Suzuki Dzire', 'Amaze', 'Amaze 1.5', 'City', 'Redi GO', 'Suzuki SX4', 'Pajero Sport', 'City ZX', 'Indigo eCS', 'Polo Highline', 'Spark LS', 'Duster 110PS', 'Cooper S', 'Fabia 1.2L', 'Duster', 'Scorpio S4', 'Scorpio VLX', 'Quanto C8', 'EcoSport', 'Brio', 'Vento Highline', 'i20 Magna', 'Corolla Altis', 'Verna Transform', '3 Series', 'Suzuki A', 'Etios GD', 'Figo Diesel', 'Beat LT', '7 Series', 'XUV500 W8', 'i10 Magna', 'Verna Fluidic', 'Suzuki Ertiga', 'Amaze 1.2', 'i20 Asta', 'Suzuki Eeco', 'Suzuki Esteem', 'Suzuki Ritz', 'Etios Liva', 'Spark', 'Micra XV', 'Beat', 'EcoSport Trend', 'Indica V2', 'Motors Ambassador', 'Innova 2.5', 'Jetta Highline', 'Polo Comfortline', 'Polo', 'Scorpio', 'Sunny', 'Kwid', 'Spark LT', 'Punto Emotion', 'i10 Sportz', 'Beat LS', 'Indigo CS', 'Eon Era', 'XUV500', 'Fiesta', 'i20', 'Fluidic Verna', 'Petra ELX', 'Suzuki Ciaz', 'Suzuki Zen', 'Creta 1.6', 'Scorpio SLX', 'Nano Cx', 'Sumo Victa', 'Passat Diesel', 'Scala RxL', 'i20 Active', 'Xylo E4', 'Jeep MM', 'Bolero SLE', 'Motors Force', 'Etios', 'City VX', 'Thar CRDe', 'A4 1.8', 'Benz GLA', 'Rover Freelander', 'Kwid RXT', 'Aria Pleasure', 'Benz B', 'GO T', 'Jazz VX', 'Tavera Neo', 'Eon Sportz', 'Sumo Gold', 'Enjoy 1.4', 'Terrano XL', 'Suzuki Maruti', 'Kwid 1.0', 'Accent GLX', 'TUV300 T4', 'Accord', 'Scorpio 2.6', 'Mobilio', 'Laura', 'Manza Aura', 'Sail UVA', 'A4 2.0', 'Elantra SX', 'KUV100 K8', 'i10', 'Accent', 'Verna', 'Fortuner', 'Bolero Power', 'Rapid Elegance', 'Vista Quadrajet', 'Beat Diesel', 'Verna 1.4', 'Suzuki Versa', 'Indigo LX', 'Vento Konekt', 'Benz C', 'Suzuki Omni', 'Sonata Transform', 'Jazz S', 'Scorpio W', 'Brio V', 'TUV300 T8', 'X Trail', 'Ikon 1.3', 'Fortuner 3.0', 'Manza ELAN', 'Benz A', 'Indigo LS', 'Verna 1.6', '5 Series', 'Superb 1.8', 'Q3 2.0', 'Figo Duratorq', 'Logan Diesel', 'Nano GenX', 'City SV', 'Figo Petrol', 'Corolla H2', 'Xcent Base', 'Accent Executive', 'Zest XE', 'XUV500 W6', 'Tigor Revotron', 'Suzuki 800', 'Mobilio S', 'Indica', 'Brio VX', 'Nano Lx', 'XE XE', 'Eon Magna', 'Eon D', 'Suzuki Estilo', 'Scorpio Vlx', 'Lancer 1.8', 'Fiesta SXi', 'A6 2.0', 'Getz Prime', 'Santro', 'Beat PS', 'X1 xDrive20d', 'Nano', 'Cruze LTZ', 'XUV500 W10', 'Accent GLE', 'Motors One', 'Spark 1.0', 'Duster 85PS', 'Enjoy', 'Wrangler Unlimited', 'Verna VGT', 'Suzuki Celerio', 'Zest Quadrajet', 'i10 Era', 'Indigo Marina', 'Xcent SX', 'Nano LX', 'Xylo E8', 'Manza Aqua', 'Venture EX', 'Octavia Classic', 'Ikon 1.6', 'Sunny XL', 'Polo Trendline', 'Elantra 1.8', 'Indica eV2', 'XF 2.2', 'Q5 2.0', 'X1 sDrive20d', 'Suzuki S', 'Vento Comfortline', 'KUV100', 'Jetta Comfortline', 'S80 Summum', 'X1', 'Duster RxL', 'WR V', 'Scorpio LX', 'A3 Cabriolet', 'Santro AE', 'Xylo D2', 'Getz GLE', 'Micra XL', 'Tavera LS', 'Tiago Revotron', 'Tiago Revotorq', 'Fusion 1.4', 'Linea Emotion', 'Corolla', 'Sumo Grande', 'Polo Highline1.2L', 'Creta', 'Bolt XM', 'Go Plus', 'Endeavor 4x4', 'Logan', 'Sail 1.2', 'Manza', 'Etios G', 'Qualis', 'Quanto C4', 'i20 Select', 'Getz', 'Fabia', 'Zest XM']

file = open('model.pkl','rb')
model = pickle.load(file)

col1 , col2, col3 = st.columns(3)

with col1:
    company_name = st.selectbox('Select the Company', sorted(company))

with col2:
    car_model_2 = st.selectbox('Select Model of Car', sorted(car_model))

with col3:
    fuel = st.selectbox('Select Fuel type', sorted(fuel_type))

year = st.number_input('Enter Year')
kms_driven = st.number_input('Enter KM driven')

if st.button('Predict'):
    input_df = pd.DataFrame({'company': [company_name], 'year': [year], 'kms_driven': [kms_driven], 'fuel_type': [fuel],
                             'model': [car_model_2]})
    
    result = model.predict(input_df)
    if year == 0.00 or kms_driven == 0.00:        
        st.header("Please type Valid Year and Km Driven")
    else:
        st.header("₹" + str(result[0]))
