import pandas as pd
import pdf_report as pr
import numpy as np

# Read csv file
dataFrame = pd.read_csv("propertydata.csv", index_col=0)

dataFrame = dataFrame.reset_index()

# Avarage Price and Square Footage in location

cols_location_price_sf = ['Price', 'SquareFootage']
avg_location_price = dataFrame.groupby('Location')[cols_location_price_sf].mean()
avg_location_df = avg_location_price.reset_index()
avg_location_df = np.round(avg_location_df, 2)
avg_location_df = avg_location_df.values.tolist()
avg_location_df.insert(0, ['Location', 'Price', 'Square Footage'])
avg_location_pdf = 'avg_location.pdf'
avg_location_heading = 'Avarage Price and Square Footage in location'
pr.pdf_write_output(avg_location_df, avg_location_pdf, avg_location_heading)

# Average Price and Square Footage in proerty type

cols_property_bedroom_bathroom = ['Bedrooms', 'Bathrooms']
avg_location_bedroom_bathroom = dataFrame.groupby('Proerty')[cols_property_bedroom_bathroom].mean()
avg_proerty_df = avg_location_price.reset_index()
avg_proerty_df = np.round(avg_proerty_df, decimals = 2)
avg_proerty_df = avg_proerty_df.values.tolist()
avg_proerty_df.insert(0, ['Proerty', 'Bedrooms', 'Bathrooms'])
avg_proerty_pdf = 'avg_property.pdf'
avg_proerty_heading = 'Avarage Price and Square Footage in proerty'
pr.pdf_write_output(avg_proerty_df, avg_proerty_pdf, avg_proerty_heading)

# Summarizes in Location and property type

cols_to_summarize = ['Price', 'Bathrooms', 'Bedrooms', 'SquareFootage']
summary = dataFrame.groupby(['Location', 'Proerty'])[cols_to_summarize].mean()
summary_df = summary.reset_index()
summary_df = summary_df.round(2)
summary_df = np.round(summary_df, 2)
summary_df = summary_df.values.tolist()
summary_df.insert(0, ['Location', 'Proerty', 'Price', 'Bedrooms', 'Bathrooms', 'Square Footage'])
summary_pdf = 'summary_location_property.pdf'
summary_heading = 'Summarizes in Location and property type'
pr.pdf_write_output(summary_df, summary_pdf, summary_heading)