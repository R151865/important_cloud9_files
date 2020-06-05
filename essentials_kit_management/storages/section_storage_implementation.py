from essentials_kit_management.interactors.storages.section_storage_interface \
    import SectionStorageInterface

from essentials_kit_management.models import Section

class SectionStorageImplementation(SectionStorageInterface):

    def are_they_valid_section_ids(self, section_ids):
        section_ids = list(set(section_ids))
        count = len(section_ids)

        objs_count = Section.objects.filter(id__in=section_ids).count()

        are_all_valid_section_ids = objs_count == count
        return are_all_valid_section_ids
