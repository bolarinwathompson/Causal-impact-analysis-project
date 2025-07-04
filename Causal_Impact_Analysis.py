####################################
#Causal Impact Analaysis
####################################


# Import required packages
from causalimpact import CausalImpact
import pandas as pd 

# import and create data 



# Import data tables

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name = "campaign_data")

# Aggregate transaction data to customer, date level

customer_daily_sales = transactions.groupby(["customer_id", "transaction_date"]) ["sales_cost"].sum().reset_index()

# Merge on the signup flag

customer_daily_sales = pd.merge(customer_daily_sales, campaign_data, how = "inner", on = "customer_id")

# Pivot the data to aggregate daily sales by Signup
causal_impact_df = customer_daily_sales.pivot_table(index ="transaction_date",
                                                    columns = "signup_flag",
                                                    values = "sales_cost", 
                                                    aggfunc = "mean")

# Provide a frequency for your DtaeTimeIndex (aviod a warning message)

causal_impact_df.index.freq = "D"

# For causal impact we need the impact group in the first column

causal_impact_df = causal_impact_df [[1, 0]] 


# Rename column to something more meaningful
causal_impact_df.columns = ["member", "non-member"]


# Apply causal impact

pre_period = ["2020-04-01", "2020-06-30"]
post_period = ["2020-07-01", "2020-09-30"]
ci = CausalImpact(causal_impact_df, pre_period, post_period)

# Plot the Impact

ci.plot()

# Extract Summary Statistics and Report

print(ci.summary())

print(ci.summary(output ="report"))
