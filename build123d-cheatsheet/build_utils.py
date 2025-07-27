from dataclasses import dataclass, field, asdict, replace
from typing import Any

# from json import dumps, loads
print('loading build123d... ', end='')
from build123d import *
print('✅')
from ocp_vscode import show


def get_fonts():
    from OCP.Font import Font_FontMgr
    from OCP.TCollection import TCollection_AsciiString
    mgr = Font_FontMgr.GetInstance_s()
    fonts = mgr.GetAvailableFonts()

    return [f.FontName().ToCString() for f in fonts]



from inspect import getsource
def sauce(obj):
    return str(getsource(obj))

def getopts(enum):
    return [str(x) for x in list(enum)]

THREED =['Box',
 'Cone',
 'CounterBoreHole',
 'CounterSinkHole',
 'Cylinder',
 'Hole',
 'Sphere',
 'Torus',
 'Wedge',]

TWOD =   [ 'Arrow', 'ArrowHead', 'Circle', 'Ellipse', 'Polygon', 'Rectangle', 'RectangleRounded', 'RegularPolygon', 'SlotArc', 'SlotCenterPoint', 'SlotCenterToCenter', 'SlotOverall', 'Text', 'Trapezoid', 'Triangle']





@dataclass
class Parameter:

    # UI REQUIRED
    name: str
    value: int | float | str | bool 
    nullable: bool = False
    default: int | float | str | bool | None = None
    type: str = None
    enabled: bool = True
    visible: bool = True
    prev: int | float | str | bool | None = None


    # UI HINTS
    options: list[str] = field(default_factory=list)
    # max: float | None = None
    # min: float | None = None
    # step: float | None = None
    # description: str | None = None
    # label: str | None = None
    # type?
    # pytype
    # requires_rebuild: bool = False

    
    def __post_init__(self):
        if self.default is None:
            self.default = self.value
        
        if self.prev is None:
            self.prev = self.value

        if self.type is None:
            if type(self.value) in (int, float):
                self.type = 'num'
            elif type(self.value)  == bool:
                self.type = 'bool'
            else:
                self.type = 'str'
                
            
    def __setattr__(self, name, value):
        postinit = 'name' in self.__dict__
        if postinit and name == 'name':
            print('Renaming after init is PROHIBITED')
        else:
            super().__setattr__(name, value)
            
    def __repr__(self):
                
        return f'{self.name } [{self.type}]: {self.value}'
    
    @property
    def v(self):
        return self.value
    
    @v.setter
    def v(self, val):
        self.value = val
    
    @property
    def e(self):
        return eval( str ( self.value ) )
    
    @property
    def i(self):
        return int( self.value )
    
    @property
    def f(self):

        return float( self.value ) if self.value is not None else None
    
    @property
    def s(self):
        return str( self.value )
    
    @property
    def b(self):
        return bool( self.value )
    
    def exec(self):
        return exec( str( self.value ) )
    

    def copy(self):
        return replace(self)

    
    
  
@dataclass 
class ParameterGroup:
    children: list = field(default_factory=list)
    name: str | None = 'Parameters'

    def __post_init__(self):
        # self._child_map = {child.n: child for child in self.children}
        self._child_map = {}
        for child in self.children:
            self.add(child)

    def __getattr__(self, name):
        if name in self._child_map:
            return self._child_map[name]
        raise AttributeError(f"'ParameterGroup' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):

        if "_child_map" in self.__dict__:
                        
            if name[0] == '_':
                print(f'"{name}" is private...')
            elif name in self._child_map:
                self._child_map[name].value = value
                
            elif name == 'children':
                print(f'Not supported. Try ParameterGroup.add()')
            else:
                super().__setattr__(name, value)
            
        else:
            ## Python default 
            super().__setattr__(name, value)


    
    def __repr__(self):
        out = self.name + ': \n'
        for c in self.children:
            if c.visible:
                out += c.__repr__() + '\n'
        
        return out
    
    def add(self, param: Parameter):
        if param.name in self._child_map:
            print(f'Name "{param.name}" is already in use -- pass')
        else:
            
            if param not in self.children:
                self.children.append(param)
            self._child_map[param.name] = param
    
    def dumps(self):
        from json import dumps
        return dumps(asdict(self))
    
    def load(self, data):
        pass

    def copy(self):
        return ParameterGroup([child.copy() for child in self.children])


def loadParam(data):
    from json import loads
    
    if type(data) == str:
        data = loads(data)
    
    if 'children' in data:
        return ParameterGroup (name=data['name'], children= [ loadParam(param) for param in data['children'] ] )
    else:
        return Parameter(**data)



    




