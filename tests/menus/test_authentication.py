from views.authentication import AuthenticationMenu
from click.testing import CliRunner


def test_authentication_menu():
    """Test the authentication menu"""
    authentication_menu = AuthenticationMenu()
    runner = CliRunner()
    result = runner.invoke(authentication_menu.authentication, ["Peter"])
    assert authentication_menu.authentication() == ("main", None)
