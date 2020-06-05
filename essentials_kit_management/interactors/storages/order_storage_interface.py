from abc import ABC, abstractmethod
from typing import Dict



class OrderStorageInterface():

    def create_new_orders(self,
                          user_id: int,
                          new_order_list: Dict):
        pass
        
    def update_orders(self, update_order_list):
        pass

    def remove_orders(self, remove_order_list):
        pass

    def are_they_valid_order_ids(self, order_ids):
        pass
