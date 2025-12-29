class FacetEngine:
    def __init__(self, facet_df):
        self.facets = facet_df

    def get_facets(self):
        return self.facets

    def group_by_category(self):
        return self.facets.groupby('category')['facet'].apply(list).to_dict()
