__author__ = 'Nazar Ner'


def test_gsm_server(app):
    app.product.find_by_cod('847372')
    app.product.add_to_cart()
    app.product.set_quantity("2")
    app.product.find_by_cod('849356')
    app.product.add_to_cart()
    app.product.set_quantity("5")
    app.product.go_to_cart_page()
    app.product.assert_discount()
    app.product.proceed_to_checkout()

