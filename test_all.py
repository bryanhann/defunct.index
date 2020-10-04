import subprocess

def test_():
    """This repo (sha=83fba6) must reside at https//github.com/bryanhann/index

    """
    out = subprocess.check_output( ['bash', 'url4sha', '8efba6'] )
    assert out ==  b'https://github.com/bryanhann/index\n'
