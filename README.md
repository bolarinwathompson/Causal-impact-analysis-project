# Causal Impact Analysis for ABC Grocery

## Project Overview:
The **Causal Impact Analysis for ABC Grocery** project utilizes the **CausalImpact** library to measure the effect of a promotional campaign on the sales of ABC Grocery. The project compares the sales data of customers who signed up for the campaign (treatment group) against those who did not (control group) using a **causal inference model**. The analysis helps determine whether the campaign led to a significant change in sales during the promotional period.

## Objective:
The primary goal of this project is to apply **causal impact analysis** to determine the effect of a promotional campaign on sales at ABC Grocery. By comparing **pre-campaign** and **post-campaign** periods for both members (those who signed up for the campaign) and non-members (those who did not sign up), the project provides actionable insights on the effectiveness of the campaign.

## Key Features:
- **Data Preprocessing**: The project aggregates transaction data at a customer and date level, merges it with campaign sign-up data, and reshapes the data for causal analysis.
- **Causal Impact Model**: The **CausalImpact** library is used to estimate the causal effect of the campaign on sales, considering both treatment and control groups.
- **Post-Campaign Analysis**: The model compares the average daily sales for both groups during the pre-period (before the campaign) and post-period (after the campaign).
- **Visualization**: The project visualizes the causal effect using a plot, showing the predicted sales and actual sales during the post-campaign period.

## Methods & Techniques:

### **1. Data Aggregation**:
The transaction data is aggregated by customer and transaction date, calculating the total daily sales for each customer. This data is then merged with campaign data that indicates whether the customer signed up for the promotional campaign.

### **2. Data Pivoting**:
The data is pivoted to create a time series with two columns:
- **Member Sales**: Sales from customers who signed up for the campaign.
- **Non-Member Sales**: Sales from customers who did not sign up for the campaign.

### **3. Causal Impact Analysis**:
The **CausalImpact** model is applied to the pivoted data:
- **Pre-period**: The period before the campaign started, used to establish a baseline for comparison.
- **Post-period**: The period after the campaign, used to observe the impact of the campaign.
- The **CausalImpact** library calculates the causal effect of the campaign by comparing the treatment group (members) to the control group (non-members).

### **4. Results Interpretation**:
- The **summary statistics** of the causal impact are extracted and reported, providing insights into the effectiveness of the campaign.
- The **predicted impact** and **actual impact** are plotted to visually illustrate the difference in sales between the two groups before and after the campaign.

## Technologies Used:
- **Python**: Programming language for implementing the causal impact analysis and data preprocessing.
- **CausalImpact**: Library for performing causal inference and calculating the effect of the promotional campaign.
- **pandas**: For data manipulation, aggregation, and pivoting.
- **matplotlib**: For visualizing the results of the causal impact analysis.

## Key Results & Outcomes:
- The **Causal Impact** analysis helps determine whether the campaign significantly increased sales for members compared to non-members.
- The results are visualized to highlight the impact of the campaign on sales, showing clear changes in the post-period sales trends.
- **Summary statistics** provide a deeper understanding of the magnitude of the effect, with confidence intervals indicating the statistical significance of the results.

## Lessons Learned:
- **Causal Impact Analysis** is a powerful tool for understanding the real effect of marketing campaigns, especially when randomization or controlled experiments are not possible.
- Data preprocessing and proper aggregation are essential to ensuring that the analysis is meaningful and that the results are valid.
- Visualization of the causal impact allows stakeholders to easily interpret the effect and make data-driven decisions about future marketing strategies.

## Future Enhancements:
- **Longer Monitoring Period**: Extend the analysis period to measure long-term effects and assess whether the impact persists beyond the immediate post-campaign period.
- **Segmentation Analysis**: Perform segmentation analysis to assess the impact on different customer groups (e.g., new vs. returning customers, high vs. low spenders).
- **Multi-Channel Analysis**: Integrate data from multiple channels (e.g., online, in-store) to measure the overall effect of the campaign across different customer touchpoints.
