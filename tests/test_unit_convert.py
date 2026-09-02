import pytest as pt
from src.common.unit_convert import Mass
def test_mass():
    a = Mass('10kg')
    b = Mass('2000g')
    c = Mass('200000 mg')
    d = Mass('< 20 ng')
    e = Mass('> 20 ng')
    
    assert '40.0ng' == d.calc(e, 'ng') # TODO: 40 is the same as 40.0, throws an error anyways. Fix rounding
    
    with pt.raises(TypeError):
        Mass('1kg1')
    with pt.raises(TypeError):
        Mass('1t')
    
    assert b.get() == '2kg', '2000g = 2kg'
    with pt.raises(NameError):
        a.get('abc')
    with pt.raises(TypeError):
        a.calc(132,'kg')
    with pt.raises(NameError):
        a.calc(b,'auto')