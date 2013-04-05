import re
import subprocess


_undefined = object()


class PDiffer(object):
    __slots__ = ('bin',)

    def __init__(self, bin='perceptualdiff'):
        self.bin = bin

    def make_cmdline(self, image1, image2, fov=_undefined,
                     threshold=_undefined, gamma=_undefined,
                     luminance=_undefined, luminanceonly=False,
                     colorfactor=_undefined, downsample=_undefined,
                     output=_undefined):
        cmdline = [self.bin]
        if fov is not _undefined:
            cmdline.extend(['-fov', '%.2f' % fov])
        if threshold is not _undefined:
            cmdline.extend(['-threshold', '%d' % threshold])
        if gamma is not _undefined:
            cmdline.extend(['-gamma', '%.1f' % gamma])
        if luminance is not _undefined:
            cmdline.extend(['-luminance', '%.1f' % luminance])
        if luminanceonly:
            cmdline.extend(['-luminanceonly'])
        if colorfactor is not _undefined:
            cmdline.extend(['-colorfactor', '%.3f' % colorfactor])
        if downsample is not _undefined:
            cmdline.extend(['-downsample', '%d' % downsample])
        if output is not _undefined:
            cmdline.extend(['-output', output])
        cmdline.extend([image1, image2])
        return cmdline

    def pdiff(self, image1, image2, **kwargs):
        cmdline = self.make_cmdline(image1, image2, **kwargs)
        p = subprocess.Popen(cmdline, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return PDiffResult(p.returncode, stdout.strip())

    def assert_images_similar(self, image1, image2, **kwargs):
        res = self.pdiff(image1, image2, **kwargs)
        if res:
            raise AssertionError("Images are different: %s" % (res,))

    def assert_images_different(self, image1, image2, **kwargs):
        res = self.pdiff(image1, image2, **kwargs)
        if not res:
            raise AssertionError("Images are similar: %s" % (res,))


class PDiffResult(object):
    __slots__ = ('returncode', 'reason')

    def __init__(self, returncode, reason):
        # Older versions of perceptualdiff don't exit with a non-zero status
        # after a failure.
        if returncode == 0 and re.search(r'^FAIL:', reason, re.MULTILINE):
            returncode = 1
        self.returncode = returncode
        self.reason = reason

    def __unicode__(self):
        return self.reason

    def __nonzero__(self):
        return self.returncode


_pdiffer = PDiffer()
pdiff = _pdiffer.pdiff
assert_images_similar = assertImagesSimilar = _pdiffer.assert_images_similar
assert_images_different = assertImagesDifferent = _pdiffer.assert_images_different
