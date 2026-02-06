def validate_unique_pair(
    self,
    model,
    **kwargs
):
    existing = model.query.filter_by(**kwargs).first()

    if existing and existing.id != self.id:
        raise ValueError("This relationship already exists")


# This function is usually run in a function in a model
# It is done in many-to-many relations

#   ContinentCountriesModel.py

        # def validate_unique(self):
        #     validate_unique_pair(
        #         self,
        #         ContinentCountriesModel,
        #         continent_id = self.continent_id
        #         country_id = self.country_id
        #     )