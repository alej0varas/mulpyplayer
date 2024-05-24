import unittest

from .context import bcp


bcp.log.DEBUG = True


class MainTests(unittest.TestCase):
    def test_main_with_artist(self):
        bcp.player.main(
            "https://<bandname>.bandcamp.com/",
            skip_downloaded=not True,
            fullscreen=False,
        )

    def test_main_with_album(self):
        bcp.player.main("https://<bandname>.bandcamp.com/album/<album_name>/")

    def test_main_with_track(self):
        bcp.player.main("https://<bandname>.bandcamp.com/track/<track_name>/")
