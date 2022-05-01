from odoo.tests.common import TransactionCase


class TestBookState(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestBookState, self).setUp(*args, **kwargs)
        self.test_book = self.env['library.book'].create({'title': 'Naruto'})

    def test_action_change_to_still(self):
        """
        Make start button
        """
        self.test_book.change_to_still()
        self.assertEqual(self.test_book.state, 'still', "Book state should be chagned to still")

    def test_action_change_to_over(self):
        """
          Make close button
        """
        self.test_book.action_close()
        self.assertEqual(self.test_book.state, 'off', "Book state should be chagned to over")