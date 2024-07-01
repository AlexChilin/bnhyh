import unittest
from Card import *
class CardTests(unittest.TestCase):
    def test_init(self):
        card = Card('coconut')
        self.assertEqual(card.kind, 'coconut')

    def test_init_invalid_kind(self):
        with self.assertRaises(ValueError):
            Card('fig')

    def test_str(self):
        card = Card('orange')
        self.assertEqual(str(card), "Card(kind = orange)")

    def test_score(self):
        card = Card('carambola')
        self.assertEqual(Card.score('carambola', 2), 6)

    def test_score_invalid_kind(self):
        card = Card('banana')
        with self.assertRaises(ValueError):
            card.score('banana', 2)

    def test_save(self):
        card = Card('pineapple')
        json_str = card.save()
        self.assertEqual(json_str, '{"kind": "pineapple"}')

    def test_load(self):
        json_str = '{"kind": "pomegranate"}'
        card = Card.load(json_str)
        self.assertEqual(card.kind, 'pomegranate')

if __name__ == "__main__":
    unittest.main()