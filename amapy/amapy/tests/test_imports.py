import pytest


class TestImports:

    def test_version(self):
        from amapy import __version__
        assert __version__ == '0.0.0'

    def test_author(self):
        from amapy import __author__
        assert __author__ == "Julien Vitard"

    def test_author_email(self):
        from amapy import __author_email__
        assert __author_email__ == "julienvitard+amapy@gmail.com"

    def test_url(self):
        from amapy import __url__
        assert __url__ == "https://github.com/julienvitard/amapy"


if __name__ == '__main__':
    pytest.main()