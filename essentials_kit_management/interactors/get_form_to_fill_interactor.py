from essentials_kit_management.interactors.storages import \
    FormStorageInterface
from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface

class GetFormToFillInteractor:

    def __init__(self,
                 form_storage: FormStorageInterface,
                 form_presenter: FormPresenterInterface):

        self.form_storage = form_storage
        self.form_presenter = form_presenter

    def get_form_to_fill(self, form_id: int):

        is_valid_form_id = self.form_storage.is_valid_form_id(form_id=form_id)
        invalid_form_id_given = not is_valid_form_id

        if invalid_form_id_given:
            self.form_presenter.raise_invalid_form_id_exception()
            return

        form_dto = self.form_storage.get_form_to_fill_dto(form_id=form_id)
        response = self.form_presenter.get_form_to_fill_response(
            form_dto=form_dto
        )
        return response