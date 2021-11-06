### data source: https://github.com/alexeygrigorev/clothing-dataset-small

from images_similarity.image_similarity import ImageSimilarity
path_images = './data/clothing-dataset-small-master/train'

sim_clothing = ImageSimilarity(path_images)
sim_clothing.create_similarity_model()
sim_clothing.explore_similarities(1)

