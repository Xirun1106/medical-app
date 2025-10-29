# import needed packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


st.set_page_config(page_title="Health Manager", page_icon="🏥", layout="wide")


st.markdown("""
<style>
    .main-header {
        font-size: 4.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 2.2rem;
        color: #A23B72;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        font-family: 'Verdana', sans-serif;
        font-weight: bold;
    }
    .section-header {
        font-size: 4rem;
        color: #F18F01;
        margin-top: 2;
        margin-bottom: 2;
        font-family: 'Georgia', serif;
        border-bottom: 3px solid #F18F01;
        padding-bottom: 1rem;
        font-weight: bold;
        line-height: 1;
    }
    .stMarkdown {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #FF9A8B, #FF6A88, #FF99AC, #FFB6C1, #FFDAC1);
    }
    .stRadio > div {
        background-color: #F8F9FA;
        padding: 10px;
        border-radius: 10px;
    }
    .stRadio > div > label {
        color: #495057;
        font-weight: 500;
    }
    .dataframe {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background-color: #F8F9FA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.8rem; color: #2E86AB; text-align: center; margin-bottom: 2rem; font-family: Arial Rounded MT Bold, sans-serif;padding: 20px; ">🏥 Your Personal Health Manager 📊</h1>', unsafe_allow_html=True)

# load the data
@st.cache_data
def load_data():
    df = pd.read_csv('insurance.csv')
    return df
df = load_data()


st.markdown('<p class="sub-header">👤 Age Filter</p>', unsafe_allow_html=True)
age_filter = st.slider('Select Age Range:', 0, 100, 50, key="age_slider")

with st.sidebar:
    st.markdown("## 🔧 Filters")
    st.markdown("---")
    
    # Region filter
    st.markdown('### 🌍 Region Filter')
    region_filter = st.multiselect(
        'Select Regions:',
        df.region.unique(),
        df.region.unique(),
        key="region_select"
    )
    
    st.markdown("---")
    
    # BMI filter in sidebar
    st.markdown('### 📊 BMI Filter')
    bmi = st.radio(
        'Choose BMI Range:',
        ['all', '<18.5', '18.5-24.9', '>24.9'],
        key="bmi_radio"
    )


filtered_df = df[df.age <= age_filter]
filtered_df = filtered_df[filtered_df.region.isin(region_filter)]


st.markdown('<p class="sub-header">📋 Medical Expenses Breakdown</p>', unsafe_allow_html=True)
styled_df = filtered_df[['sex','bmi','children','smoker','charges']].style.background_gradient(cmap='Blues')
st.write(styled_df)

# ---------------------- Question One ----------------------
st.markdown('<div style="margin-top: 20px; margin-bottom: 10px;">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size: 2.2rem; color: #F18F01; margin-top: 0; margin-bottom: 0; font-family: Georgia, serif; border-bottom: 3px solid #F18F01; padding-bottom: 0.8rem; font-weight: bold;">📈 Question 1: Analyze relationship between BMI and Medical Insurance Charges</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('''
### 🎯 Understanding the BMI-Insurance Cost Relationship

Body Mass Index (BMI) is a key indicator of health status and has a significant impact on medical insurance costs. 
This analysis explores how different BMI ranges correlate with healthcare expenses, providing insights for both 
individuals and insurance providers.

#### 💡 Why BMI Matters:
- **Health Risks**: Higher BMI is associated with increased risk of chronic diseases like diabetes, heart disease, and hypertension
- **Insurance Pricing**: Insurance companies use BMI as a factor in premium calculations
- **Preventive Care**: Understanding this relationship helps in proactive health management

#### 🔍 Key Insights:
- Optimal BMI range (18.5-24.9) typically correlates with lower medical costs
- Underweight individuals (BMI < 18.5) may have specific health concerns
- Overweight and obesity categories show progressively higher medical expenses
''')

st.markdown('<p class="sub-header">🎯 Suitable BMI has great significance for reducing medical expenses</p>', unsafe_allow_html=True)

# Filter data according to BMI ranges from sidebar
if bmi == '<18.5':
    bmi_filtered_df = df[df.bmi < 18.5]
    color_palette = ['#FFD700']  # Gold for underweight
elif bmi == '18.5-24.9':
    bmi_filtered_df = df[(df.bmi >= 18.5) & (df.bmi < 24.9)]
    color_palette = ['#32CD32']  # Lime green for healthy
elif bmi == '>24.9':
    bmi_filtered_df = df[df.bmi > 24.9]
    color_palette = ['#FF4500']  # Orange red for overweight
else:
    bmi_filtered_df = df
    color_palette = ['#1E90FF', '#FF69B4']  # Blue and pink for all data

# Apply additional filters (age and region) to BMI filtered data
bmi_filtered_df = bmi_filtered_df[bmi_filtered_df.age <= age_filter]
bmi_filtered_df = bmi_filtered_df[bmi_filtered_df.region.isin(region_filter)]
    
# Create a line chart - plot after sorting by BMI
fig, ax = plt.subplots(figsize=(12, 6))
    
# Sort by BMI to ensure that the line graph is connected correctly
sorted_df = bmi_filtered_df.sort_values('bmi')
    
# Draw a scatter plot with enhanced colors
sns.scatterplot(data=bmi_filtered_df, x='bmi', y='charges', 
                hue='smoker', palette={'yes': '#FF6B6B', 'no': '#4ECDC4'},
                alpha=0.7, s=60, ax=ax)
    
# Set chart titles and labels with custom styling
ax.set_title(f'BMI vs Medical Insurance Charges (BMI Range: {bmi})', 
             fontsize=14, fontweight='bold', color='#2C3E50')
ax.set_xlabel('BMI', fontsize=12, fontweight='bold', color='#34495E')
ax.set_ylabel('Charges ($)', fontsize=12, fontweight='bold', color='#34495E')
ax.grid(True, alpha=0.3)
ax.set_facecolor('#F8F9FA')
    
# Display the chart
st.pyplot(fig)

st.markdown('''
### Conclusions and Recommendations:

#### 👤 For Individuals:
- **Maintain Healthy BMI**: Aim for BMI between 18.5-24.9 to minimize health risks and insurance costs
- **Regular Monitoring**: Track BMI changes and take preventive measures
- **Lifestyle Choices**: Combine healthy BMI with non-smoking habits for optimal cost savings

#### 🏢 For Insurance Providers:
- **Risk Assessment**: Use BMI as an important factor in risk evaluation
- **Preventive Programs**: Offer incentives for maintaining healthy BMI
- **Educational Initiatives**: Provide resources on BMI management and its impact on health costs

#### 🏛️ For Healthcare Policy:
- **Public Health Campaigns**: Promote awareness about BMI and health outcomes
- **Preventive Care**: Emphasize the economic benefits of maintaining healthy weight
- **Research Support**: Continue studying the relationship between BMI and healthcare utilization
''')

# ---------------------- Question Two ----------------------
# set title
st.markdown('<div style="margin-top: 20px; margin-bottom: 10px;">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size: 2.1rem; color: #F18F01; margin-top: 0; margin-bottom: 0; font-family: Georgia, serif; border-bottom: 3px solid #F18F01; padding-bottom: 0.8rem; font-weight: bold;">👩‍👧‍👦 Question 2: Analysis of the Relationship Between Women\'s Medical Expenses and the Number of Children Born</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# markdown part 1
st.markdown('''
In this problem, we aim to conduct an in-depth study on the impact of childbearing on women's medical expenses.
            
From the perspective of "quantitative consumption" of medical needs, the data intuitively presents the influence of childbearing behavior on women's medical health, providing data support for the optimization of medical services, health management, and the design of insurance products.

In the process of data analysis, we excluded the influences of factors such as body mass index, smoking status, and region to ensure the rigor of the single-factor experiment, focusing only on the impact of different numbers of childbirths on women's medical expenses within specific age groups.
''')

# Get female info only from filtered data
female_df = filtered_df[filtered_df['sex'] == 'female']

# Group by the number of children and get average medical expenses
avg_charges = female_df.groupby('children')['charges'].mean().reset_index()

# Demonstrate the data analysis info
st.markdown('<p class="sub-header">Women\'s Average Medical Expenses by Number of Children</p>', unsafe_allow_html=True)
styled_avg_charges = avg_charges.style.background_gradient(cmap='Purples')
st.write(styled_avg_charges)

# markdown part 2
st.markdown('#### 📈According to the results of data analysis, women\'s medical expenses show a trend of first increasing, then slightly fluctuating, and finally decreasing as the number of children they give birth to increases. This trend reflects the differences in health needs at different reproductive stages. ')
st.markdown('''

**In the childless stage**, women's health needs mainly focus on regular physical examinations and basic disease management, and medical consumption is relatively stable. 
            
**In the process of having 1 to 4 children**, women need to go through multiple stages such as pregnancy, childbirth, and postnatal recovery. The needs for prenatal check-ups, childbirth medical services, and other services during these stages will directly push up medical expenses. 
            
**When having 5 children**, the expenses decrease, which may reflect that some families with multiple children tend to choose basic and economical medical services due to economic or health factors.
''')

# bar chart part with enhanced styling
fig, ax = plt.subplots(figsize=(20,13))
colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA']
bars = ax.bar(avg_charges['children'], avg_charges['charges'], color=colors[:len(avg_charges)], edgecolor='black', linewidth=1.2)
ax.set_title('Female Medical Expenses vs. Number of Children', fontsize=30, fontweight='bold', color='#8E44AD', pad=20)
ax.set_xlabel('Number of Children', fontsize=25, fontweight='bold', color='#2C3E50')
ax.set_ylabel('Average Medical Expenses ($)', fontsize=25, fontweight='bold', color='#2C3E50')
ax.tick_params(axis='both', labelsize=23, colors='#34495E')
ax.set_xticks(avg_charges['children'])
ax.grid(axis='y', alpha=0.3)
ax.set_facecolor('#F8F9FA')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 100,
            f'${height:,.0f}', ha='center', va='bottom', fontsize=18, fontweight='bold')

st.pyplot(fig)

# markdown part 3
st.markdown('<p class="sub-header">💡 Implications for the medical and insurance fields</p>', unsafe_allow_html=True)
st.markdown('''
**📋 Recommendations:**
- For women planning to have multiple children, it is advisable to undergo comprehensive pre-pregnancy check-ups before preparing for pregnancy. After childbirth, they should pay attention to their own recovery and reduce medical risks and costs through standardized management.

**💼 Commercial value:**
- Medical institutions can optimize integrated pregnancy and childbirth services for the group of women with "1 to 4 children" to meet the high demands of this stage.
- Insurance companies can design specialized pregnancy and childbirth insurance products for the group of women with "1 to 4 children" based on this data, achieving precise matching of risks and services.
''')


# ---------------------- Question Three ----------------------
st.markdown('<div style="margin-top: 20px; margin-bottom: 10px;">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size: 2.2rem; color: #F18F01; margin-top: 0; margin-bottom: 0; font-family: Georgia, serif; border-bottom: 3px solid #F18F01; padding-bottom: 0.8rem; font-weight: bold;">🚭 Question 3: The impact of smoking on physical health</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Show the plot
st.markdown('<h2 style="font-size: 1.2rem; color: #A23B72; margin-top: 1rem; margin-bottom: 1rem; font-family: Verdana, sans-serif; font-weight: bold;">Does smoking have a greater impact on medical expenses for men or women?</h2>', unsafe_allow_html=True)

fig, ax = plt.subplots(2, 2, figsize=(20, 15))
fig.suptitle('Impact of Smoking on Medical Expenses by Gender', fontsize=24, fontweight='bold', color='#C0392B')

# Define colors for the plots
smoker_colors = ['#E74C3C', '#3498DB']  # Red for smokers, Blue for non-smokers

# Female smokers
df_female_1 = df[(df['sex']=='female') & (df['smoker']=='yes')]
box1 = ax[0,0].boxplot(df_female_1.charges, patch_artist=True)
box1['boxes'][0].set_facecolor(smoker_colors[0])
box1['medians'][0].set_color('white')
box1['medians'][0].set_linewidth(3)
ax[0,0].set_xlabel('Female Smokers', fontsize=14, fontweight='bold', color='#C0392B')
ax[0,0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
ax[0,0].set_facecolor('#FDEDEC')

# Male smokers
df_male_1 = df[(df['sex']=='male') & (df['smoker']=='yes')]
box2 = ax[0,1].boxplot(df_male_1.charges, patch_artist=True)
box2['boxes'][0].set_facecolor(smoker_colors[0])
box2['medians'][0].set_color('white')
box2['medians'][0].set_linewidth(3)
ax[0,1].set_xlabel('Male Smokers', fontsize=14, fontweight='bold', color='#C0392B')
ax[0,1].set_facecolor('#FDEDEC')

# Female non-smokers
df_female_0 = df[(df['sex']=='female') & (df['smoker']=='no')]
box3 = ax[1,0].boxplot(df_female_0.charges, patch_artist=True)
box3['boxes'][0].set_facecolor(smoker_colors[1])
box3['medians'][0].set_color('white')
box3['medians'][0].set_linewidth(3)
ax[1,0].set_xlabel('Female Non-Smokers', fontsize=14, fontweight='bold', color='#2980B9')
ax[1,0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
ax[1,0].set_facecolor('#EBF5FB')

# Male non-smokers
df_male_0 = df[(df['sex']=='male') & (df['smoker']=='no')]
box4 = ax[1,1].boxplot(df_male_0.charges, patch_artist=True)
box4['boxes'][0].set_facecolor(smoker_colors[1])
box4['medians'][0].set_color('white')
box4['medians'][0].set_linewidth(3)
ax[1,1].set_xlabel('Male Non-Smokers', fontsize=14, fontweight='bold', color='#2980B9')
ax[1,1].set_facecolor('#EBF5FB')

# Add some padding between subplots
plt.tight_layout(pad=4.0)

st.markdown('''
From the graphs, it's evident that for both genders, the median medical expenses are significantly higher for smokers compared to non-smokers. This indicates a strong correlation between smoking and increased healthcare costs, reflecting the detrimental effects of smoking on health. Specifically:
- 🔴 For female smokers, the median expenses of medical treatment are around 30,000 dollars, whereas for non-smokers, they are below $10,000.
- 🔴 For male smokers, the median expenses of medical treatment are around 38,000 dollars, while for non-smokers, they are below $10,000.
''')

st.pyplot(fig)

st.markdown('<p class="sub-header">🎯 The conclusion is clear:</p>', unsafe_allow_html=True)
st.markdown('''
- smoking poses significant health risks, with the impact being more severe for men. 
- This could be due to differences in how smoking affects male and female physiology, or it might be related to men tending to smoke more heavily or for longer periods.
- Therefore, to safeguard health and reduce healthcare costs, quitting smoking is essential. Society should enhance awareness campaigns about the dangers of smoking and provide more resources and support to help individuals quit this harmful habit.
''')

# Add a footer

st.markdown("<p style='text-align: center; color: #7F8C8D;'>---------- Your Personal Health Manager ----------</p>", unsafe_allow_html=True)