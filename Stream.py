import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import time

# =========================================
# 1. Page Configuration (Elite UI)
# =========================================
st.set_page_config(
    page_title="Smartphone Addiction Predictor",
    page_icon="📱",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1e293b, #0f172a, #020617); color: #f8fafc; }
    
    /* ستايل البطاقة الزجاجية */
    .premium-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px; padding: 25px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.1);
        backdrop-filter: blur(15px); margin-bottom: 25px;
    }
    
    /* ستايل العنوان داخل البار الزجاجي */
    .card-title {
        color: #38bdf8;
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(56, 189, 248, 0.2);
        padding-bottom: 10px;
        display: block;
    }

    .premium-h1 {
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; font-size: 3.5rem !important; text-align: center;
    }
    
    .chart-desc { color: #94a3b8; font-size: 0.9rem; margin-top: 10px; }
    .legend-item { display: flex; align-items: center; margin-bottom: 5px; font-size: 0.85rem; }
    .dot { height: 10px; width: 10px; border-radius: 50%; display: inline-block; margin-right: 10px; }
    
    .stButton>button {
        width: 100%; background: linear-gradient(45deg, #0ea5e9, #6366f1);
        color: white; border: none; padding: 20px; font-size: 1.5rem;
        font-weight: bold; border-radius: 15px; transition: 0.4s;
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(99, 102, 241, 0.5); }
    </style>
""", unsafe_allow_html=True)

# =========================================
# 2. Asset Loading
# =========================================
@st.cache_resource
def load_assets():
    try:
        model = joblib.load("svm_final.pkl")
        cols = joblib.load("columns.pkl")
        return model, cols
    except: return None, None

model, expected_columns = load_assets()

# =========================================
# 3. Header
# =========================================
st.markdown('<h1 class="premium-h1">Smartphone Addiction Classification</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#94a3b8; font-size:1.1rem; margin-bottom:40px;">Professional AI Diagnostic Dashboard | Mohamed Walid & Nahed Sheta .</p>', unsafe_allow_html=True)

# =========================================
# 4. Input Sections (Titles Inside Glass Cards)
# =========================================
col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    st.markdown('<div class="premium-card"><span class="card-title">👤 Personal Profile</span>', unsafe_allow_html=True)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", 10, 60, 21)
    academic = st.slider("Academic Performance (0-100)", 0, 100, 80)
    parental = st.slider("Parental Control Level", 1, 10, 5)
    family_c = st.slider("Family Communication (Hrs/Week)", 0, 60, 12)
    st.markdown('</div>', unsafe_allow_html=True)

with col_in2:
    st.markdown('<div class="premium-card"><span class="card-title">📲 Usage Patterns</span>', unsafe_allow_html=True)
    daily_h = st.slider("Daily Usage (Hours)", 0.0, 24.0, 7.5)
    weekend_h = st.slider("Weekend Usage (Hours)", 0.0, 24.0, 10.5)
    checks = st.number_input("Phone Checks per Day", 0, 600, 90)
    bed_time = st.slider("Hours used before sleep", 0, 6, 2)
    purposes = st.multiselect("Usage Purposes", ["Social Media", "Gaming", "Educational", "Browsing", "Other"])
    st.markdown('</div>', unsafe_allow_html=True)

with col_in3:
    st.markdown('<div class="premium-card"><span class="card-title">🧠 Health Indicators</span>', unsafe_allow_html=True)
    anxiety = st.slider("Anxiety Level", 1, 10, 6)
    depression = st.slider("Depression Level", 1, 10, 5)
    self_esteem = st.slider("Self Esteem Level", 1, 10, 6)
    sleep_h = st.slider("Daily Sleep Hours", 0, 14, 7)
    exercise_h = st.slider("Exercise (Hours/Week)", 0, 25, 3)
    st.markdown('</div>', unsafe_allow_html=True)

# Time Breakdown Card
st.markdown('<div class="premium-card"><span class="card-title">🕒 Detailed Time Allocation (Live Preview)</span>', unsafe_allow_html=True)
ts1, ts2, ts3 = st.columns(3)
with ts1: s_t = st.number_input("Social Media (Hours)", 0.0, 20.0, 4.5)
with ts2: g_t = st.number_input("Gaming (Hours)", 0.0, 20.0, 2.0)
with ts3: e_t = st.number_input("Education (Hours)", 0.0, 20.0, 1.5)
st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# 5. Visual Analytics (Titles Inside Glass Cards)
# =========================================
st.markdown('<h2 style="text-align:center; color:#38bdf8; margin-top:30px;">📊 Behavioral Analytics</h2>', unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)


color_map = {
    'Social': '#38bdf8',
    'Gaming': '#818cf8',
    'Edu': '#34d399'
}

with v1:
    st.markdown('<div class="premium-card"><span class="card-title">Time Distribution</span>', unsafe_allow_html=True)
    
    fig_pie = px.pie(
        names=list(color_map.keys()), 
        values=[s_t, g_t, e_t], 
        hole=0.7,
        color=list(color_map.keys()), 
        color_discrete_map=color_map   
    )
    
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        font_color="white", 
        height=280, 
        showlegend=False, 
        margin=dict(t=10,b=10)
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)
    
    
    st.markdown(f"""
    <div class="chart-desc">
        <div class="legend-item"><span class="dot" style="background-color: {color_map['Social']};"></span> <b>Social Media:</b> High Dopamine reward.</div>
        <div class="legend-item"><span class="dot" style="background-color: {color_map['Gaming']};"></span> <b>Gaming:</b> Entertainment focus.</div>
        <div class="legend-item"><span class="dot" style="background-color: {color_map['Edu']};"></span> <b>Education:</b> Productive usage.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with v2:
    st.markdown('<div class="premium-card"><span class="card-title">Life Balance Radar</span>', unsafe_allow_html=True)
    cat = ['Anxiety', 'Depression', 'Academic', 'Exercise', 'Sleep']
    val = [anxiety*10, depression*10, academic, (exercise_h/20)*100, (sleep_h/12)*100]
    fig_radar = go.Figure(go.Scatterpolar(r=val, theta=cat, fill='toself', line=dict(color='#c084fc')))
    fig_radar.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=False, range=[0, 100])),
                            paper_bgcolor='rgba(0,0,0,0)', font_color="white", height=280, margin=dict(t=30,b=20))
    st.plotly_chart(fig_radar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with v3:
    st.markdown('<div class="premium-card"><span class="card-title">Weekday vs Weekend</span>', unsafe_allow_html=True)
    fig_bar = go.Figure(data=[
        go.Bar(name='Weekday', x=['Usage'], y=[daily_h], marker_color='#38bdf8'),
        go.Bar(name='Weekend', x=['Usage'], y=[weekend_h], marker_color='#c084fc')
    ])
    fig_bar.update_layout(barmode='group', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                        font_color="white", height=280, margin=dict(t=10,b=10))
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# 6. Model Prediction Logic
# =========================================
if st.button("🚀 ANALYZE ADDICTION LEVEL"):
    if model:
        total_time = s_t + g_t + e_t
        input_data = {
            'Age': [age], 'Daily_Usage_Hours': [daily_h], 'Sleep_Hours': [sleep_h],
            'Academic_Performance': [academic], 'Exercise_Hours': [exercise_h],
            'Anxiety_Level': [anxiety], 'Depression_Level': [depression], 
            'Self_Esteem': [self_esteem], 'Parental_Control': [parental], 
            'Screen_Time_Before_Bed': [bed_time], 'Phone_Checks_Per_Day': [checks], 
            'Time_on_Social_Media': [s_t], 'Time_on_Gaming': [g_t],
            'Time_on_Education': [e_t], 'Family_Communication': [family_c], 
            'Weekend_Usage_Hours': [weekend_h], 'Total_Time': [total_time], 
            'Non_Educational_Time': [s_t+g_t], 'Social_Media_Ratio': [s_t/total_time if total_time > 0 else 0]
        }
        
        df_final = pd.DataFrame(input_data)
        df_final[f"Gender_{gender}"] = 1
        for p in purposes: df_final[f"Phone_Usage_Purpose_{p}"] = 1
        final_input = df_final.reindex(columns=expected_columns, fill_value=0)
        
        with st.spinner("🤖 AI analyzing behavioral patterns..."):
            time.sleep(2)
            res = model.predict(final_input)[0]
        
        if "Strong" in res or "High" in res:
            advice = "Critical: Your phone is controlling your life. We recommend a Digital Detox and strict screen time limits."
            color = "#ef4444" 
            score = 92
        elif "Moderate" in res:
            advice = "Warning: You are entering the danger zone. Try to increase physical activities and family time."
            color = "#f59e0b"
            score = 55
        else:
            advice = "Safe: Your digital habits are well-balanced. Keep maintaining this healthy relationship with your device."
            color = "#10b981" 
            score = 15

        st.markdown("---")
        res_c1, res_c2 = st.columns([1, 1.2])
        with res_c1:
            st.markdown(f'<div class="premium-card" style="border: 2px solid {color}; text-align:center;"><span class="card-title" style="border:none;">Diagnosis Result</span>', unsafe_allow_html=True)
            st.markdown(f'<h1 style="color:{color}; font-size:4rem;">{res}</h1>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size:1.1rem; color:#e2e8f0; line-height:1.6;"><b>AI Insight:</b> {advice}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with res_c2:
            fig_g = go.Figure(go.Indicator(
                mode = "gauge+number", value = score,
                title = {'text': "Addiction Severity Index", 'font': {'size': 20, 'color': 'white'}},
                gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': color},
                         'steps': [{'range': [0, 40], 'color': "rgba(16,185,129,0.15)"},
                                   {'range': [40, 75], 'color': "rgba(245,158,11,0.15)"},
                                   {'range': [75, 100], 'color': "rgba(239,68,68,0.15)"}]}))
            fig_g.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", height=380)
            st.plotly_chart(fig_g, use_container_width=True)
    else: st.error("Model files not found!")

st.markdown('<p style="text-align:center; color:#475569; margin-top:50px;">SMARTPHONE ADDICTION CLASSIFICATION CORE © 2026</p>', unsafe_allow_html=True)