import unittest

import pdiffer


class PDiffResultTest(unittest.TestCase):

    def test_zero_result_code_is_falsy(self):
        res = pdiffer.PDiffResult(0, u"PASS")
        assert not res

    def test_positive_result_code_is_truthy(self):
        res = pdiffer.PDiffResult(1, u"FAIL")
        assert res

    def test_unicode_result_is_the_message(self):
        res = pdiffer.PDiffResult(1, u"FAIL")
        assert unicode(res) == u'FAIL'


class PDiffTest(unittest.TestCase):

    def test_different_sized_images_are_different(self):
        res = pdiffer.pdiff('test_image.png', 'test_image_smaller.png')
        assert res, "Differently sized images are similar"

    def test_same_images_are_similar(self):
        res = pdiffer.pdiff('test_image.png', 'test_image.png')
        assert not res, "Identical images are different"


class PDiffAssertionTest(unittest.TestCase):

    def test_assert_images_different_raises_AssertionError_on_similar_images(self):
        self.assertRaises(AssertionError, pdiffer.assert_images_different,
                          'test_image.png', 'test_image.png')

    def test_assert_images_different_passes_on_different_images(self):
        pdiffer.assert_images_different('test_image.png', 'test_image_smaller.png')

    def test_assert_images_similar_raises_AssertionError_on_different_images(self):
        self.assertRaises(AssertionError, pdiffer.assert_images_similar,
                          'test_image.png', 'test_image_smaller.png')

    def test_assert_images_similar_passes_on_similar_images(self):
        pdiffer.assert_images_similar('test_image.png', 'test_image.png')
