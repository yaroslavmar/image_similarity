import turicreate as tc

# Load images from the downloaded data
reference_data = tc.image_analysis.load_images('./101_ObjectCategories')
reference_data = reference_data.add_row_number()

# Save the SFrame for future use
reference_data.save('./caltech-101.sframe')