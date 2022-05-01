import streamlit as st
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
import time
import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
#from  PIL import ImageChops
#import plotly.express as px
import webbrowser



st.title('Training and Innovation Coaching Program')
from PIL import Image
logo1 = Image.open("Logos.jpg")
logo2 = Image.open("AMBERO_logo.jpg")
logo3 = Image.open("cinop-logo.png")
logo4 = Image.open("cordaid-logo.png")
image1 = Image.open("Full-Scale-Agri-Entrepreneurship.jpeg")
image2 = Image.open("homepage_agriculture__50.png")
image3 = Image.open("funnel.png")

st.image(logo1,width = 700)

with st.sidebar:
    choose = option_menu("MENU", ["About Program", "What to Know Before Applying","Implementation Process", "Selection Criteria","Contact"],
                         icons=['house', 'question-square','triangle','funnel-fill', 'chat'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "About Program":
#Add the cover image for the cover page. Used a little trick to center the image
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Program</p>', unsafe_allow_html=True)
        
    #with col2:               # To display brand logo
        
        #st.image(image1, width=700)
    st.subheader('GIZ Knowledge transfer for Agribusiness Innovations, Training of Innovation Coaches, International technology networking and Creation of business linkages ')    
    st.write("This innovative and unique project, funded by the European Union and implemented by the GIZ and AMBERO Consulting, aims to attract 25 pioneers in the Agriculture sector in Iraq, both from Academic and Private Sector backgrounds, from Six targeted provinces (Baghdad, Basra, Ninewa, Diyala, Diwaniyah, and Erbil), and engage them in an extensive training program that is tailored for the needs of this sector in Iraq, focused on modern concepts and utilization of technology in establishing new Agribusiness and sustaining existing agripreneurial MSMEs in Iraq.")
    st.image(image1, width=700)
    st.write("In order to meet its goals and achieve the set objective, the project aims to spread the knowledge through Iraqi youth and Agripreneurs using the 25 trained professional (Agrinovative Champions), in order to enable better understanding and exposure to fresh-graduate and unemployed youth in Iraq to start their own agripreneurial projects, as well as providing technical support and guidance to the existing one.")
    st.write("Eventually, the project ultimate goal is to provide a sense of possibility and empowerment for Iraqis to restore their legacy and bright history in Agriculture, both as a business as well as a reliable source of food consumption in Iraq, to achieve some kind of self-reliance in this sector, that will, in its turn, create an additional factor that will contribute in strengthening both the private sector and local economy in Iraq. Which links directly to the main objectives of the GIZ PSD (Private Sector Development) project, that has been carried out in Iraq since 2019.") 
    st.markdown("""---""")
    #st.image(profile, width=700 )

elif choose == "What to Know Before Applying":
    st.write("Once you are selected to join our Training and Coaching of Innovation Coaches program, you’ll receive world-class mentorship and coaching, information and entrepreneurial sessions, subject matter one-on-one sessions, training by local and international experts and a multitude of perks and services.")
    st.image(image2, width=700)
    st.markdown("""---""")

elif choose == "Selection Criteria":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Selection Criteria</p>', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('✅ Academic background in agriculture')
    st.markdown("✅ Knowledge in agriculture projects in private sector")
    st.markdown('✅ Fluency in both English and depending on regions Arabic and Kurdish')
    st.markdown('✅ Targeted ages: between 20 and 45')
    st.markdown('✅ Originally from [or have been based in the following provinces over the last five years]; Baghdad, Basra, Mosul, Erbil, Diwaniyah, and/or Diyala.')            
    st.markdown('✅ Women are encouraged to apply') 
    st.markdown('✅ Leadership and soft skills are preferred') 
    st.markdown('✅ Professional network and connections with entities and individuals engaged with agriculture and agribusiness') 
    st.markdown('✅ Knowledge and experience in the following value-chains; Grains Chain = Central and Southern Iraq, Date-palms = Southern Iraq, Vegetables = across entire Iraq, Fruits = across entire Iraq with focus on central and northern Iraq. As well as any other common and widely consumed corps in Iraq.')
    st.markdown('✅ Knowledge and Experience in Animal Production, Fodder Production, Milk and Dairy production are also included and considered.') 
    st.markdown('✅ Willing to commit during the entire course of the program')
    st.markdown('✅ Willing to spread the word about the program and transfer the knowledge and experience they will gain')
    st.markdown('✅ Willing to undertake a business/learning/exposure trip to one of the to one of the European countries')
    st.markdown("""---""")


elif choose == "Implementation Process":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font"> 1️⃣ Apply</p>', unsafe_allow_html=True)
    
    st.markdown('AMBERO call for applications will be announced on all official communication channels, signaling the eligibility for all interested applicants to apply to the program. To join the Training and Coaching of Innovation Coaches program, interested applicants could apply on the homepage of of the program and fill in a form detailing the basics of their idea or business.')
    
    st.markdown("""---""")
    
    st.markdown('<p class="font"> 2️⃣ Selection</p>', unsafe_allow_html=True)
    st.markdown('The initial target is to obtain at least 200 complete/successful applications before the advertisement campaign is concluded. These 200 applications will be studied and evaluated by our international and local experts, to identify the most promising 100 applicants.The consortium will identify innovation coaches champions through a selection. Based on a funnel approach developed for identifying and selecting champions (see figure), a total of over 200 actors in the agribusiness sector will be contacted regarding their applications. Details of these participants will be available. Data will be gathered regarding their business performance and position they occupy in their respective value chains.')
    st.markdown("The process will be narrowed down the identified champions to identify the best 50 candidates after the first cycle of workshops, and the best 25 candidates for the IC role after the second cycle of workshops. We will develop a pool (i.e., database) for all 50 applicants identified following the application evaluation process. In order to be on the safe side by creating a safety list to go back to in case of any dropouts for any reason, before and during the course of implementation of the first part of the project; training the 25 ICs from all six targeted provinces in Iraq.")
    st.image(image3, width = 750)
    
    
    st.markdown("""---""")
    
    st.markdown('<p class="font"> 3️⃣ Training</p>', unsafe_allow_html=True)
    st.markdown('This program based on international standards will support consultants, experts, researchers, academicians, trainers, and coaches in their outreach activities to support farmers, agribusiness MSMEs, and all other agripreneurs involved in different VCs in Iraq. By going through the different steps of innovation process, the ICs will get familiar with the different processes of innovative projects and agripreneurship activity which are: ')
    
    st.subheader('🔶 Module 0: Starting the training phase')
    st.subheader("🔶 Module 1: Online training on VC concepts")
    st.subheader('🔶 Module 2: Training on innovation process')
    st.subheader('🔶 Module 3: Training on technical and management aspects')
    
    st.markdown("""---""")
    
    st.markdown('<p class="font"> 4️⃣ Coaching</p>', unsafe_allow_html=True)
    st.markdown("The consortium will offer a half year coaching, supervisory and follow-up support phase to the ICs. A virtual coaching and mentoring space titled Community of Practice [CoP] as an advisory platform for the target group will be established. The trained ICs would be available on this platform via appointment and free of charge. This way the sustainability aspect will be covered and the identification of activities for CoP will help in quick wins for innovation promotion.")

    st.markdown("Further, a blended format of group workshops, chat rooms, small group coaching for specific topics, individual coaching (e.g., coffee coaching), mutual coaching, collective thinking etc. will be developed.") 

    st.markdown("During the last three months: a pilot activity will be offered where the IC adopt the learnings be providing consultancy or coaching to at least 2 MSME, entrepreneurs or private sector organizations from the agribusiness sector over a period of 3 months.")
    
    st.markdown("""---""")
    st.markdown('<p class="font"> 5️⃣ Study Tour</p>', unsafe_allow_html=True)
    st.markdown("You might be awarded a trip to Germany, Netherland, or other EU agricultural countries if you made it among the best 25 evaluated Innovation Coaches!")
    st.markdown("""---""")
    
    st.markdown('<p class="font"> 6️⃣ Certification</p>', unsafe_allow_html=True)
    st.markdown("Exams at the end of the training and coaching phase for the ICs. Feedback will be taken from beneficiaries [pilot MSMEs] and the marks would be added to the final exam score of the ICs")

    st.markdown("Evaluating the ToIC program by a survey amongst the ICs, including data from M&E")

    st.markdown("Certificates would be handed out by AMBERO with GIZ with partners on it, e.g., via a MoU with partners")
    
elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Your Email') #Collect user feedback
        Mobilephone= st.text_input(label='Please Enter Your Mobile phone') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')    
    
url = "https://ee.kobotoolbox.org/x/tYuoOA2m" #url is for the platform that we collect data from participants,Kobo or Googleform
#st.sidebar.write("[APPLY NOW](%s)" % url)

if st.sidebar.button('APPLY'):
    webbrowser.open_new_tab(url)
st.sidebar.write("Deadline 17/05/2022")
if st.button('APPLY NOW'):
    webbrowser.open_new_tab(url)
st.write("Deadline 17/05/2022")

#st.markdown("check out this [link](%s)" % url)

st.sidebar.image(logo2, width = 150)
st.sidebar.image(logo3, width = 150)
st.sidebar.image(logo4, width = 150)
