from essentials_kit_management.interactors.storages.brand_storage_interface \
    import BrandStorageInterface

from essentials_kit_management.models import Brand

class BrandStorageImplementation(BrandStorageInterface):

    def are_they_valid_brand_ids(self, brand_ids):
        brand_ids = list(set(brand_ids))
        count = len(brand_ids)

        objs_count = Brand.objects.filter(id__in=brand_ids).count()

        are_all_valid_brand_ids = objs_count == count
        return are_all_valid_brand_ids
