
import domaincheck.util as util


def test_parent_domain():
    assert util.parent_domain('google.com') == 'com'
    assert util.parent_domain('google.com.') == 'com.'
    assert util.parent_domain('google.co.uk') == 'co.uk'
    assert util.parent_domain('google.co.uk.') == 'co.uk.'


def test_absolute_domain():
    assert util.absolute_domain('com') == 'com.'
    assert util.absolute_domain('google.com') == 'google.com.'
    assert util.absolute_domain('google.com.') == 'google.com.'
