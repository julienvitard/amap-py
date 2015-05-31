
class TestImports:

    def test_version(self):
        from amappy import __version__
        assert __version__ == '0.0.0'

    def test_author(self):
        from amappy import __author__
        assert __author__ == "Julien Vitard"

    def test_author_email(self):
        from amappy import __author_email__
        assert __author_email__ == "julienvitard+amappy@gmail.com"

    def test_url(self):
        from amappy import __url__
        assert __url__ == "https://github.com/julienvitard/amappy"
