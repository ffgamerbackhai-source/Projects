
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
print(df)

print(df.info())
print(df.isnull().sum())
print(df.describe())
cols_with_zero = ['Sugar','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome']
df[cols_with_zero] = df[cols_with_zero].replace(0,pd.NA)

praks = df[(df['Sugar'].notna()) & (df['Glucose'].notna())]
print(praks)
pranks = df[(df['BloodPressure'].notna()) &  (df['SkinThickness'].notna())]
print(pranks)
park = df[(df['Outcome'].notna()) & (df['BMI'].notna())]
print(park)
clean_data = df.dropna(subset=['Sugar','Glucose'])
print(clean_data)

clean_data = df.dropna(subset=['Sugar','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome','Age','Outcome'])
print(clean_data)

df_clean = clean_data.sort_values(by=['Sugar','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome','Age','Outcome'],ascending=True)
print(df_clean)

plt.scatter(clean_data['Sugar'] , clean_data['BMI'],color = 'red')
plt.xlabel('Sugar')
plt.ylabel('Glucose')
plt.show()