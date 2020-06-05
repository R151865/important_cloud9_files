# from 


# class CreateUserInteractor:

#     def __init__(self,
#                  user_storage: UserStorageInterface,
#                  user_presenter: UserPresenterInterface):

#         user_storage = user_storage
#         user_presenter = user_presenter

#     def create_user(self,
#                     name: str,
#                     phone_number: int,
#                     password: int):

#         new_user_id = user_storage.create_user(name=name,
#                                               phone_number=phone_number,
#                                               password=password)
#         response = user_presenter.get_create_user_response(
#             user_id=new_user_id
#         )
#         return response