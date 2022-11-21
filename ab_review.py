@classmethod
def buy(cls, user, item_id):
    product_qs = Product.objects.filter(item_id=item_id).first()
    '''
    product_qs вернёт None, если не будет найден, иначе вернет 0 элемент.
    Перед return хорошобы еще Logger вставить что бы было понятно что ф-я
    завершилась тк product_qs = None
    ''' 
    # if product_qs.exists():
    #     product = product_qs[0]
    if not product_qs:
        return False

    '''
    После проверки на доступность лучше сразу сделать available = False, что
    повысит безопасность при взломе.
    Meтод withdraw должен проверить баланс счета списания и выдать шибку в случае,
    если операция списания не прошла.
    Exception нужно уточнить.
    Вернуть available = True в случае неудачи и лучше через какоето время.
    '''
    if product.available:
        product.available = False
        # списание средств со счета пользователя
        try:
            user.withdraw(product.price)
        except Exception:
            product.available = True
            return False

        # информация о купленном товаре
        send_email_to_user_of_buy_product(user)
        product.buyer = user
        product.save()
        return True
    else:
        return False