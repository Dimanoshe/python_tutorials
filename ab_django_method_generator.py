from django.db import models


class MethodGenerator(object):

    def __init__(self, model, method_name):        
        # Создаём объект MethodGenerator, где method_name - предположительно метод 
        # класса DeliveryState (например get_new)
        self.model = model
        self.method_name = method_name

    def __call__(self):
        # Отсеиваеи get_ и переводим в верхний регистр       
        required_attribute_name = self.method_name[4:].upper()
        # required_attribute_value = DeliveryState.имя метода (например NEW = 1)
        # если атрибут не будет найден - будет вызван exc: AttributeError
        required_attribute_value = getattr(self.model, required_attribute_name)
        print(f'required_attribute_value: {required_attribute_value}')
        # Обращаемся по pk и получаем значение
        value_from_database = self.model.objects.get(pk=required_attribute_value)
        return value_from_database


class DeliveryState(models.Model):
    class Meta:
        verbose_name = u"Состояние доставки"
        verbose_name_plural = u"Состояния доставок"
    NEW = 1  # Новая
    ISSUED = 2  # Выдана курьеру
    DELIVERED = 3  # Доставлена
    HANDED = 4  # Курьер сдал
    REFUSED = 5  # Отказ
    PAID_REFUSED = 6  # Отказ с оплатой курьеру
    COMPLETE = 7  # Завершена
    NONE = 8  # Не определено

    @classmethod
    def __getattr__(cls, attr):
        return MethodGenerator(cls, attr)
