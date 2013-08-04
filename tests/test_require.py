import component


def test_require_calls_settup():
    """This test checks that require calls setup()"""
    orig_setup = component.setup
    global setup_called
    setup_called = False

    def new_setup( *args, **kwargs):
        global setup_called
        setup_called = True
        return orig_setup(*args, **kwargs)

    component.setup = new_setup
    component.require('test')
    component.setup = orig_setup
    assert setup_called


def test_require_calls_setup(monkeypatch):
    """Tests that require() calls setup()"""

    def mock_setup():
        assert True, "Test"
        pass

    monkeypatch.setattr(component, 'setup', mock_setup)

    component.require('test')