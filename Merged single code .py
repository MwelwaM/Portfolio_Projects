#Import pandas
import pandas as pd
import csv

#Open WA List
WA_list=pd.read_csv('December_Lists _ whatsapp - whatsapp_active_no_app_list1_17Dec.csv')

#B5
#1hour
B5_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B5&B6_1_HOUR.xlsx"))
B5_1hr=B5_1hr.rename(columns={'Customer Email': 'email'})

Joined_B5_1=pd.merge(B5_1hr, WA_list)

Joined_B5_1.to_csv('B5_1HOUR.csv')

#5hour
B5_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B5&B6_5_HOUR.xlsx"))
B5_5hr=B5_5hr.rename(columns={'Customer Email': 'email'})

Joined_B5_5=pd.merge(B5_5hr, WA_list)

Joined_B5_5.to_csv('B5_5HOUR.csv')

#10hour
B5_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B5&B6_10_HOUR.xlsx"))
B5_10hr=B5_10hr.rename(columns={'Customer Email': 'email'})

Joined_B5_10=pd.merge(B5_10hr, WA_list)

Joined_B5_10.to_csv('B5_10HOUR.csv')

#All day
B5_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B5&B6_DAY.xlsx"))
B5_DAY=B5_DAY.rename(columns={'Customer Email': 'email'})

Joined_B5_D=pd.merge(B5_DAY, WA_list)

Joined_B5_D.to_csv('B5_DAY.csv')

#B7
#1hour
B7_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B7&B8_1_HOUR.xlsx"))
B7_1hr=B7_1hr.rename(columns={'Customer Email': 'email'})

Joined_B7_1=pd.merge(B7_1hr, WA_list)

Joined_B7_1.to_csv('B7_1HOUR.csv')

#5hour
B7_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B7&B8_5_HOUR.xlsx"))
B7_5hr=B7_5hr.rename(columns={'Customer Email': 'email'})

Joined_B7_5=pd.merge(B7_5hr, WA_list)

Joined_B7_5.to_csv('B7_5HOUR.csv')


#10hour
B7_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B7&B8_10_HOUR.xlsx"))
B7_10hr=B7_10hr.rename(columns={'Customer Email': 'email'})

Joined_B7_10=pd.merge(B7_10hr, WA_list)

Joined_B7_10.to_csv('B7_10HOUR.csv')


#All day
B7_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B7&B8_DAY.xlsx"))
B7_DAY=B7_DAY.rename(columns={'Customer Email': 'email'})

Joined_B7_D=pd.merge(B7_DAY, WA_list)

Joined_B7_D.to_csv('B7_DAY.csv')

#B9
#1hour
B9_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B9&B10_1_HOUR.xlsx"))
B9_1hr=B9_1hr.rename(columns={'Customer Email': 'email'})

Joined_B9_1=pd.merge(B9_1hr, WA_list)

Joined_B9_1.to_csv('B9_1HOUR.csv')

#5hour
B9_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B9&B10_5_HOUR.xlsx"))
B9_5hr=B9_5hr.rename(columns={'Customer Email': 'email'})

Joined_B9_5=pd.merge(B9_5hr, WA_list)

Joined_B9_5.to_csv('B9_5HOUR.csv')


#10hour
B9_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B9&B10_10_HOUR.xlsx"))
B9_10hr=B9_10hr.rename(columns={'Customer Email': 'email'})

Joined_B9_10=pd.merge(B9_10hr, WA_list)

Joined_B9_10.to_csv('B9_10HOUR.csv')

#All day
B9_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B9&B10_DAY.xlsx"))
B9_DAY=B9_DAY.rename(columns={'Customer Email': 'email'})

Joined_B9_DAY=pd.merge(B9_DAY, WA_list)

Joined_B9_DAY.to_csv('B9_DAY.csv')

#B11
#1hour
B11_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B11&B12_1_HOUR.xlsx"))
B11_1hr=B11_1hr.rename(columns={'Customer Email': 'email'})

Joined_B11_1=pd.merge(B11_1hr, WA_list)

Joined_B11_1.to_csv('B11_1HOUR.csv')

#5hour
B11_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B11&B12_5_HOUR.xlsx"))
B11_5hr=B11_5hr.rename(columns={'Customer Email': 'email'})

Joined_B11_5=pd.merge(B11_5hr, WA_list)

Joined_B11_5.to_csv('B11_5HOUR.csv')


#10hour
B11_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B11&B12_10_HOUR.xlsx"))
B11_10hr=B11_10hr.rename(columns={'Customer Email': 'email'})

Joined_B11_10=pd.merge(B11_10hr, WA_list)

Joined_B11_10.to_csv('B11_10HOUR.csv')

#All day
B11_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B11&B12_1_DAY.xlsx"))
B11_DAY=B11_DAY.rename(columns={'Customer Email': 'email'})

Joined_B11_DAY=pd.merge(B11_DAY, WA_list)

Joined_B11_DAY.to_csv('B11_DAY.csv')

#B13
#1hour
B13_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B13&B14_1_HOUR.xlsx"))
B13_1hr=B13_1hr.rename(columns={'Customer Email': 'email'})

Joined_B13_1=pd.merge(B13_1hr, WA_list)

Joined_B13_1.to_csv('B13_1HOUR.csv')

#5hour
B13_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B13&B14_5_HOUR.xlsx"))
B13_5hr=B13_5hr.rename(columns={'Customer Email': 'email'})

Joined_B13_5=pd.merge(B13_5hr, WA_list)

Joined_B13_5.to_csv('B13_5HOUR.csv')

#10hour
B13_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B13&B14_10_HOUR.xlsx"))
B13_10hr=B13_10hr.rename(columns={'Customer Email': 'email'})

Joined_B13_10=pd.merge(B13_10hr, WA_list)

Joined_B13_10.to_csv('B13_10HOUR.csv')

#All day
B13_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B13&B14_DAY.xlsx"))
B13_DAY=B13_DAY.rename(columns={'Customer Email': 'email'})

Joined_B13_DAY=pd.merge(B13_DAY, WA_list)

Joined_B13_DAY.to_csv('B13_DAY.csv')

#B15
#1hour
B15_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B15&B16_1_HOUR.xlsx"))
B15_1hr=B15_1hr.rename(columns={'Customer Email': 'email'})

Joined_B15_1=pd.merge(B15_1hr, WA_list)

Joined_B15_1.to_csv('B15_1HOUR.csv')

#5hour
B15_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B15&B16_5_HOUR.xlsx"))
B15_5hr=B15_5hr.rename(columns={'Customer Email': 'email'})

Joined_B15_5=pd.merge(B15_5hr, WA_list)

Joined_B15_5.to_csv('B15_5HOUR.csv')



#10hour
B15_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B15&B16_10_HOUR.xlsx"))
B15_10hr=B15_10hr.rename(columns={'Customer Email': 'email'})

Joined_B15_10=pd.merge(B15_10hr, WA_list)

Joined_B15_10.to_csv('B15_10HOUR.csv')


#All day
B15_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B15&B16_DAY.xlsx"))
B15_DAY=B15_DAY.rename(columns={'Customer Email': 'email'})

Joined_B15_DAY=pd.merge(B15_DAY, WA_list)

Joined_B15_DAY.to_csv('B15_DAY.csv')

#B17
#1hour
B17_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B17&B18_1_HOUR.xlsx"))
B17_1hr=B17_1hr.rename(columns={'Customer Email': 'email'})

Joined_B17_1=pd.merge(B17_1hr, WA_list)

Joined_B17_1.to_csv('B17_1HOUR.csv')

#5hour
B17_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B17&B18_5_HOUR.xlsx"))
B17_5hr=B17_5hr.rename(columns={'Customer Email': 'email'})

Joined_B17_5=pd.merge(B17_5hr, WA_list)

Joined_B17_5.to_csv('B17_5HOUR.csv')


#10hour
B17_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B17&B18_10_HOUR.xlsx"))
B17_10hr=B17_10hr.rename(columns={'Customer Email': 'email'})

Joined_B17_10=pd.merge(B17_10hr, WA_list)

Joined_B17_10.to_csv('B17_10HOUR.csv')

#All day
B17_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B17&B18_DAY.xlsx"))
B17_DAY=B17_DAY.rename(columns={'Customer Email': 'email'})

Joined_B17_DAY=pd.merge(B17_DAY, WA_list)

Joined_B17_DAY.to_csv('B17_DAY.csv')


#B19
#1hour
B19_1hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B19&B20_1_HOUR.xlsx"))
B19_1hr=B19_1hr.rename(columns={'Customer Email': 'email'})

Joined_B19_1=pd.merge(B19_1hr, WA_list)

Joined_B19_1.to_csv('B19_1HOUR.csv')

#5hour
B19_5hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B19&B20_5_HOUR.xlsx"))
B19_5hr=B19_1hr.rename(columns={'Customer Email': 'email'})

Joined_B19_5=pd.merge(B19_5hr, WA_list)

Joined_B19_5.to_csv('B19_5HOUR.csv')


#10hour
B19_10hr=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B19&B20_10_HOUR.xlsx"))
B19_10hr=B19_1hr.rename(columns={'Customer Email': 'email'})

Joined_B19_10=pd.merge(B19_10hr, WA_list)

Joined_B19_10.to_csv('B19_10HOUR.csv')

#All day
B19_DAY=pd.DataFrame(pd.read_excel("speed_sale_27_december_2024_non_app_users_B19&B20_DAY.xlsx"))
B19_DAY=B19_DAY.rename(columns={'Customer Email': 'email'})

Joined_B19_DAY=pd.merge(B19_DAY, WA_list)

Joined_B19_DAY.to_csv('B19_DAY.csv')



