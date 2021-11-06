import turicreate as tc

### data source: https://github.com/alexeygrigorev/clothing-dataset-small

class ImageSimilarity:
    def __init__(self, path_images):
        self.reference_data = tc.image_analysis.load_images(path_images)
        self.reference_data = self.reference_data.add_row_number()

    def create_similarity_model(self):
        self.model = tc.image_similarity.create(self.reference_data)

    def find_similarity_for_id(self, image_id, num_similar_images=10):
        query_results = self.model.query(self.reference_data.filter_by(image_id, 'id'), k=num_similar_images)
        similar_rows = query_results['reference_label']
        similar_images = self.reference_data.filter_by(similar_rows, 'id')
        self.similar_images_with_score = similar_images.join(query_results, how='inner', on={'id':'reference_label'})
        return self.similar_images_with_score

    def explore_similarities(self):
        self.similar_images_with_score.sort('distance', ascending=True).explore()