from essentials_kit_management.interactors.storages.item_storage_interface \
    import ItemStorageInterface

from essentials_kit_management.models import Item


class ItemStorageImplementation(ItemStorageInterface):

    def are_they_valid_item_ids(self, item_ids):
        item_ids = list(set(item_ids))
        count = len(item_ids)

        objs_count = Item.objects.filter(id__in=item_ids).count()

        are_all_valid_item_ids = objs_count == count
        return are_all_valid_item_ids
