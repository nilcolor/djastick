# encoding: utf-8
"""
Something, that looks like Enum ;)

usage:

>> import Enum
>> 
>> class SEX(Enum):
>>     MALE = EnumItem(100, "Male creature")
>>     FEMALE = EnumItem(200, "Female creature")
>>     HYBRID = EnumItem(300, "'Not sure' creature")
>> 
>> 
>> foo = FOO.HYBRID.id
>> print "foo sex is %s" % SEX.get(foo)

You can pass it like (as) choices to a field:
>> bar = SomeField(choices=SEX.as_choices())
And of course you can extend both Enum and EnumItem via classic inheritance ;) And make it looks like unicorn with cookies.
"""

class EnumItem(object):
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc
    
    def __eq__(self, other):
        return self.id == other.id if hasattr(other, 'id') else self.id == other
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.id < other.id if hasattr(other, 'id') else self.id < other
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __le__(self, other):
        return self.id <= other.id if hasattr(other, 'id') else self.id <= other
    
    def __gt__(self, other):
        return not self.__le__(other)


class Enum(object):
    class ItemDoesNotExist(Exception):
        pass
    
    @classmethod
    def as_choices(cls):
        return [(item.id, item.desc) for item in sorted(cls._get_items(), key=lambda item: item.id)]
    
    @classmethod
    def get(cls, id):
        for item in cls._get_items():
            if item.id == id:
                return item
        
        raise Enum.ItemDoesNotExist(u'The enum item with the id = %s does not exist.' % id)
    
    @classmethod
    def _get_items(cls):
        return [attr for attr_name, attr in cls.__dict__.items() if not (attr_name.startswith('__') or isinstance(attr, classmethod))]
