### data source: https://github.com/alexeygrigorev/clothing-dataset-small

from images_similarity.image_similarity import ImageSimilarity
path_images = './data/clothing-dataset-small-master/train'

sim_clothing = ImageSimilarity(path_images)
sim_clothing.create_similarity_model()

similarities_100 = sim_clothing.find_similarity_for_id(100)
similarities_100.explore()

similarities_600 = sim_clothing.find_similarity_for_id(600)
similarities_600.explore()

similarities_2500 = sim_clothing.find_similarity_for_id(2500)
similarities_2500.explore()
