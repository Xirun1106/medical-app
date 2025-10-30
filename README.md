# Your personal health manager

**Group member:** Li Sichen & Liu Yimeng & Li Xirun

**Dataset:** [https://www.kaggle.com/datasets/mirichoi0218/insurance](https://www.kaggle.com/datasets/mirichoi0218/insurance)

### Why we chose this dataset:

We selected the medical insurance charges dataset because it provides comprehensive health-related information including age, BMI, smoking status, region, number of children, and medical expenses. This dataset is particularly valuable for analyzing healthcare patterns and cost drivers across different demographic groups. The inclusion of reproductive data (number of children) makes it especially relevant for studying women's health economics, allowing us to examine how various life factors influence medical expenditures. The dataset's structured format and diverse variables enable robust statistical analysis and meaningful insights into healthcare consumption patterns.

![Dataset Overview](/Users/xrli/Desktop/misy225/repo/medical-app)

## Question 1: Analysis of the Relationship Between BMI and Medical Charges

### 1. Why this question:

Understanding the correlation between BMI and medical expenses is crucial for several reasons. With rising global obesity rates and increasing healthcare costs, identifying how body weight status impacts medical expenditures can help in developing targeted health interventions. This analysis provides valuable insights for insurance companies in risk assessment, helps healthcare providers allocate resources more efficiently, and supports public health initiatives aimed at weight management.

### 2. How we analyze:

We conducted a systematic analysis by：

- Categorizing BMI values into standard classifications: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), and Obese (≥30)
- Calculating average medical charges for each BMI category
- Performing correlation analysis between continuous BMI values and medical charges
- Creating scatter plots with trend lines to visualize the relationship
- Conducting subgroup analysis while controlling for other variables like smoking status and age

### 3. Result:

Our analysis reveals a significant positive correlation between BMI and medical charges. The data shows that individuals in the Obese category (BMI ≥30) have the highest average medical expenses, approximately 40% higher than those in the Normal weight category. The relationship appears to be non-linear, with medical costs increasing more rapidly as BMI enters the obese range.

![BMI vs Medical Charges](/Users/xrli/Desktop/misy225/repo/medical-app)

### 4. Deep explanation:

The strong relationship between BMI and medical charges can be explained by several factors：

- Higher BMI is associated with increased risk of chronic conditions such as diabetes, hypertension, and cardiovascular diseases
- Obese individuals often require more frequent medical consultations, medications, and specialized treatment
- Weight-related conditions may lead to more complex and expensive medical procedures
- The correlation may be partially mediated by other factors like physical activity levels and dietary habits

### 5. Commercial value:

- Health insurance companies can use these findings to develop more accurate risk-based pricing models and create incentivized wellness programs for weight management.
- Employers can implement workplace health initiatives focused on weight control to reduce overall healthcare costs.
- Healthcare providers can develop targeted prevention programs for high-BMI individuals to mitigate future medical expenses.
- Public health organizations can use this data to advocate for obesity prevention programs and justify investments in weight management initiatives.

## Question 2: Analysis of the Relationship Between Women's Medical Expenses and the Number of Children Born

### 1. Why this question:

In this problem, we aim to conduct an in-depth study on the impact of childbearing on women's medical expenses. From the perspective of "quantitative consumption" of medical needs, the data intuitively presents the influence of childbearing behavior on women's medical health, providing data support for the optimization of medical services, health management, and the design of insurance products.

### 2. How we analyze:

In the process of data analysis, we excluded the influences of factors such as body mass index, smoking status, and region to ensure the rigor of the single-factor experiment, focusing only on the impact of different numbers of childbirths on women's medical expenses within specific age groups.

### 3. Result:

Women's medical expenses show a trend of first increasing, then slightly fluctuating, and finally decreasing as the number of children they give birth to increases. This trend reflects the differences in health needs at different reproductive stages.

![Women's Medical Expenses vs Children](/Users/xrli/Desktop/misy225/repo/medical-app)

### 4. Deep explanation:

- In the childless stage, women's health needs mainly focus on regular physical examinations and basic disease management, and medical consumption is relatively stable.
- In the process of having 1 to 4 children, women need to go through multiple stages such as pregnancy, childbirth, and postnatal recovery. The needs for prenatal check-ups, childbirth medical services, and other services during these stages will directly push up medical expenses.
- When having 5 children, the expenses decrease, which may reflect that some families with multiple children tend to choose basic and economical medical services due to economic or health factors.

### 5. Commercial value:

- Medical institutions can optimize integrated pregnancy and childbirth services for the group of women with "1 to 4 children" to meet the high demands of this stage.
- Insurance companies can design specialized pregnancy and childbirth insurance products for the group of women with "1 to 4 children" based on this data, achieving precise matching of risks and services.

## Question 3: The impact of smoking on physical health

### 1. Why this question:

Smoking is a widespread and serious social issue. We chose this topic with the aim of quantifying and visualizing the problems caused by smoking, providing mutual recommendations for both smokers and insurance companies. Our goal is to help everyone recognize the dangers of smoking and genuinely influence lifestyle choices for a healthier future.

### 2. How we analyze:

During the data analysis, I divided the data into four categories based on two indicators: smoking status and gender, and produced four box-charts to compare the differences in medical expenses between smokers and non-smokers, as well as between male and female smokers.

### 3. Result:

![Smoking Impact Analysis](/Users/xrli/Desktop/misy225/repo/medical-app)
- For female smokers, the median expenses of medical treatment are around 30,000 dollars, whereas for non-smokers, they are below $10,000.
- For male smokers, the median expenses of medical treatment are around 38,000 dollars, while for non-smokers, they are below $10,000.
- We can clearly see that the charges of non-smokers are less than one fourth of smokers, while the charge of smokers are very high.
- Besides, The charges of male smokers were significantly higher than female smokers. The reasons may include differences in smoking intensity and physiological structure.

### 4. Deep explanation:

In this analysis, we focused on the difference in median costs between the two groups, but we should also pay attention to how tightly the data cluster.

As the box-charts show, smokers' expenses are far more spread out than those of non-smokers. Non-smokers' costs are concentrated in the 5000–10000 dollars band, whereas smokers' costs are clustered across the 20000–40000 dollars range. This indicates that the physical harm of smoking varies from person to person, yet for the vast majority it is extremely severe—on average roughly four times the expense incurred by non-smokers.

### 5. Commercial value:

This finding carries significant implications for both insurance companies and the general public.

- For insurance companies, the pronounced difference in medical expenditures between smokers and non-smokers provides robust empirical support for risk-based premium stratification, enabling more accurate pricing models and better alignment of premiums with underlying risk profiles.
- For residents, the four-fold increase in median costs serves as a powerful, quantifiable reminder of the long-term health consequences of smoking, thereby encouraging individuals to reconsider their behavioral choices and adopt healthier lifestyles that reduce both personal health risks and future financial burdens.