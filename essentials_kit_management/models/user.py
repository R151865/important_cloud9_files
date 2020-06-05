from django.db import models

from django.contrib.auth.models import AbstractUser

from essentials_kit_management.constants.enums import (
    FormStatusEnum, TransactionTypeEnum, TransactionStatusEnum
)


class User(AbstractUser):
    name = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    min_quantity = models.IntegerField(default=0)
    max_quantity = models.IntegerField()
    price_per_item = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.ManyToManyField(Brand)


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    items = models.ManyToManyField(Item)


class Form(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=[(status.name, status.value) for status in FormStatusEnum],
        max_length=10, null=True
        )
    description = models.TextField()
    close_date = models.DateTimeField(null=True)
    expected_delivery_date = models.DateTimeField(null=True)
    sections = models.ManyToManyField(Section)


class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ForeignKey(Item, on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
   form = models.ForeignKey(Form, on_delete=models.CASCADE)
   section = models.ForeignKey(Section, on_delete=models.CASCADE)
   count = models.IntegerField(default=0)
   pending_count = models.IntegerField()
   out_of_stock = models.IntegerField()


class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    amount =  models.IntegerField(default=0)
    status = models.CharField(
        choices = [
            (status.name, status.value) for status in TransactionStatusEnum
            ],
            max_length=50,
            default=TransactionStatusEnum.PENDING.value
        )
    transaction_type = models.CharField(
        choices = [
            (transaction_type.name, transaction_type.value)
                for transaction_type in TransactionTypeEnum
            ],
            max_length=50
        )
    screen_shot = models.TextField()
    remark = models.CharField(max_length=100)


class Account(models.Model):
    upi_id = models.CharField(primary_key=True, max_length=50)
    account_holder = models.CharField(max_length=100)
