from .build_utils import *
from .build_utils import Parameter as P
from .build_utils import ParameterGroup as PG

# from abcq import make

print('querying fonts... ', end='')
allfonts = get_fonts()
default_font = 'Comic Sans MS' if 'Comic Sans MS' in allfonts else 'Arial'


print('✅')

if default_font != 'Comic Sans MS':
    print('''
https://archive.org/details/ComicSansMSRegularBold
          
The most important font in the world, Comic Sans MS. Includes regular and bold variant.

Designed by Vincent Connare and released by Microsoft in 1994.
'''
          )
    


index = {
    'Box': lambda: PG([
        P('shape', 'Box'),
        P('length',  10.0),
        P('width',  15.0),
        P('height', 40.0),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),
        P('code', sauce(Box), visible=False),

    ]),

    'Cone': lambda: PG([
        P('shape',  'Cone'),
        P('bottom_radius', 15),
        P('top_radius',  0),
        P('height', 50),
        P('arc_size',  360.0),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),
        P('code', sauce(Cone), visible=False),

    ]),

    'CounterBoreHole': lambda: PG([
        P('shape', 'CounterBoreHole'),
        P('radius', 1.0 ),
        P('counter_bore_radius', 1.5 ),
        P('counter_bore_depth', 1.0 ),
        P('depth',None, type='num', nullable=True),

        P('mode','Mode.SUBTRACT'),
        P('companion', True, visible=False),

        P('code', sauce(CounterBoreHole), visible=False),

    ]),

    'CounterSinkHole': lambda: PG([
        P('shape', 'CounterSinkHole'),
        P('radius', 1.0 ),
        P('counter_sink_radius', 2.0 ),
        P('depth',None, type='num', nullable=True),
        P('counter_sink_angle', 82.0),  

        P('mode','Mode.SUBTRACT'),
        P('companion', True, visible=False),

        P('code', sauce(CounterSinkHole), visible=False),

    ]),


    'Cylinder': lambda: PG([
        P('shape', 'Cylinder'),
        P('radius', 10.0 ),
        P('height', 35.0 ),
        P('arc_size', 360.0 ),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),
        

        P('code', sauce(Cylinder), visible=False),      
    ]),

    
    'Hole': lambda: PG([
        P('shape', 'Hole'),
        P('radius', 1.0 ),

        P('depth',None, type='num', nullable=True),

        P('mode','Mode.SUBTRACT'),
        P('companion', True, visible=False),


        P('code', sauce(Hole), visible=False),

    ]),


    'Sphere': lambda: PG([
        P('shape',  'Sphere'),
        P('radius', 10.0),
        P('arc_size1',  -90.0),
        P('arc_size2',  90.0),
        P('arc_size3', 360.0),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),


        P('code', sauce(Sphere), visible=False),

    ]),

    'Torus': lambda: PG([
        P( 'shape', 'Torus' ),
        P( 'major_radius', 15.0 ),
        P( 'minor_radius', 5.0 ),
        P( 'minor_start_angle', 0.0 ),
        P( 'minor_end_angle', 360.0 ),
        P( 'major_angle', 360.0),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),

  
        P('code', sauce(Torus), visible=False),
    ]),

    'Wedge': lambda: PG([
        P( 'shape', 'Wedge'),
        P( 'xsize', 60.0 ),
        P( 'ysize', 60.0 ),
        P( 'zsize', 45.0 ), 
        P( 'xmin', 40.0 ),
        P( 'zmin', 30.0 ),
        P( 'xmax', 60.0 ),
        P( 'zmax', 55.0 ),

        P('rotation', '(0, 0, 0,)'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('align_z', 'Align.CENTER', options=getopts(Align)),
        P('companion', False),

        P('code', sauce(Wedge), visible=False),
    ]),


### 2D
    'Arrow': lambda: PG([
        P('shape', 'Arrow'),
        P('arrow_size', 4.0),
        P('pts0', '(-4, 0)'),
        P('pts1', '(4,0)'),
        P('shaft_width', 1.0),
        P('head_at_start', True),
        P('head_type', 'HeadType.CURVED'),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Arrow), visible=False),

    ]),

    'ArrowHead': lambda: PG([
        P('shape', 'ArrowHead'),
        P('size', 6.0),
        P('head_type', 'HeadType.CURVED'),
        P('rotation', 0.0),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(ArrowHead), visible=False),
    ]),


    'Circle': lambda: PG([
        P('shape', 'Circle'),
        P('radius', 8.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Circle), visible=False),
    ]),

    'Ellipse': lambda: PG([
        P('shape', 'Ellipse'),
        P('x_radius', 12.0),
        P('y_radius', 8.0),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Ellipse), visible=False),
    ]),


    'Polygon': lambda: PG([
        P('shape', 'Polygon'),
        P('pts0', '(-2.0, -2.0)'),
        P('pts1', '(-2.0,2.0)'),
        P('pts2', '(2.0,2.0)'),
        P('pts3', '(2.0, -2.0)'),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Polygon), visible=False),
    ]),

    'Rectangle': lambda: PG([
        P('shape', 'Rectangle'),
        P('width', 15),
        P('height', 10),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Rectangle), visible=False),
    ]),

    'RectangleRounded': lambda: PG([
        P('shape', 'RectangleRounded'),
        P('width', 15),
        P('height', 10),
        P('radius', 2.0),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(RectangleRounded), visible=False),
    ]),

    
    'RegularPolygon': lambda: PG([
        P('shape', 'RegularPolygon'),
        P('radius', 6.0),
        P('side_count', 6.0),
        P('major_radius', True),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(RegularPolygon), visible=False),
    ]),

    'SlotArc': lambda: PG([
        P('shape', 'SlotArc'),
        P('pts0', '(-4, 0)'),
        P('pts1', '(4,0)'),
        P('height', 2.0),
        P('rotation', 0.0),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(SlotArc), visible=False),
    ]),
    'SlotCenterPoint': lambda: PG([
        P('shape', 'SlotCenterPoint'),
        P('center', '(0, 0)'),
        P('point', '(4,0)'),
        P('height', 2.0),
        P('rotation', 0.0),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(SlotCenterPoint), visible=False),
    ]),
    'SlotCenterToCenter': lambda: PG([
        P('shape', 'SlotCenterToCenter'),
        P('center_separation', 8.0),
        P('height', 2.0),
        P('rotation', 0.0),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(SlotCenterToCenter), visible=False),
    ]),
    'SlotOverall': lambda: PG([
        P('shape', 'SlotOverall'),
        P('width', 8.0),
        P('height', 2.0),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(SlotOverall), visible=False),
    ]),

    'Text': lambda: PG([
        P('shape', 'Text'),
        P('txt', 'Hello World'),
        P('font_size', 4.0),
        P('font', default_font, options=allfonts),
        P('font_path', None, type='str', nullable=True),
        P('font_style', 'FontStyle.REGULAR', options=getopts(FontStyle)),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('use_path', False),
        P('path', 'Line ( (-1, -1), (1, 1) )', type='str' ),
        # P('pts0', '(-1,-1)'),
        # P('pts1', '(1,1)'),    
        P('position_on_path', 0.0),
        P('rotation', 0.0),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Text), visible=False),
    ]),



    'Trapezoid': lambda: PG([
        P('shape', 'Trapezoid'),
        P('width', 15.0),
        P('height', 10.0),
        P('left_side_angle', 80.0),
        P('right_side_angle', None, type='num'),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Trapezoid), visible=False),
    ]),

    'Triangle': lambda: PG([
        P('shape', 'Triangle'),
        P('a', 6.0, type='num', nullable=True),
        P('b', None, type='num', nullable=True),
        P('c', None, type='num', nullable=True),
        P('A', None, type='num', nullable=True),
        P('B', 60.0, type='num', nullable=True),
        P('C', 60.0, type='num', nullable=True),
        P('rotation', 0.0),
        P('align_x', 'Align.CENTER', options=getopts(Align)),
        P('align_y', 'Align.CENTER', options=getopts(Align)),
        P('mode', 'Mode.ADD', options=getopts(Mode)),
        P('extrude', 0.001),
        P('companion', False, visible=True),
        P('code', sauce(Triangle), visible=False),
    ]),



    # 1D

    'Bezier': lambda: PG([
        P('shape', 'Bezier'),
        
        P('pts0', '(-0, 0)'),
        P('pts1', '(20, 20)'),  
        P('pts2', '(40, 0)'),
        P('pts3', '(0, -40)' ),
        P('pts4',  '(-60, 0)'),
        P('pts5',  '(0, 100)'),
        P('pts6',  '(100, 0)'),  

        P('wts', '[1.0, 1.0, 2.0, 3.0, 4.0, 2.0, 1.0]'),
        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(Bezier), visible=False), 

    ]),
    'CenterArc': lambda: PG([
        P('shape', 'CenterArc'),
        
        P('center', '(0.0, 0.0)'),
        P('radius', 40.0 ),
        P('start_angle', 0.0),
        P('arc_size', 180.0 ),  

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(CenterArc), visible=False), 

    ]),

    'DoubleTangentArc': lambda: PG([
        P('shape', 'DoubleTangentArc'),
        
        P('pnt', '(25.0, 10.0)'),
        P('tangent', '(0.0, 1.0)'),  
        P('other', 'JernArc(start=(0,0), tangent=(1,0), radius=5.0, arc_size=180) '),
        P('keep', 'Keep.TOP', options=getopts(Keep)),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(DoubleTangentArc), visible=False), 

    ]),
    'EllipticalCenterArc': lambda: PG([
        P('shape', 'EllipticalCenterArc'),
        
        P('center', '(0.0, 0.0)'),
        P('x_radius', 40.0 ),
        P('y_radius', 30.0 ),
        P('start_angle', 0.0),
        P('end_angle', 90.0),
        P('rotation', 0 ),  
        P('angular_direction', 'AngularDirection.COUNTER_CLOCKWISE', options = getopts(AngularDirection)),
        # P('plane', 'Plane.XY'),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(EllipticalCenterArc), visible=False), 

    ]),

    'FilletPolyline': lambda: PG([
        P('shape', 'FilletPolyline'),
        
        P('pts0', '(-0, 0)'),
        P('pts1', '(20, 20)'),  
        P('pts2', '(40, 0)'),
        P('pts3', '(0, -40)' ),
        P('pts4',  '(-60, 0)'),
        P('pts5',  '(0, 100)'),
        P('pts6',  '(100, 0)'),  

        P('radius', 10.0),

        P('close', False),
        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(FilletPolyline), visible=False), 

    ]),
    'Helix': lambda: PG([
        P('shape', 'Helix'),
        
        P('pitch', 10.0),

        P('height', 20.0),

        P('radius', 30.0),
        
        P('center', '(0, 0, 0)'),
        P('direction', '(0, 0, 1)'), 


        P('cone_angle', 0), 

        P('lefthand', False),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(Helix), visible=False), 

    ]),
    'IntersectingLine': lambda: PG([
        P('shape', 'IntersectingLine'),
        
        P('start', '(10, 15.0)'),
        P('direction', '(-1.0, -1.0)'),  
        P('other', 'JernArc(start=(0,0), tangent=(1,0), radius=5.0, arc_size=180) '),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(IntersectingLine), visible=False), 

    ]),


    'JernArc': lambda: PG([
        P('shape', 'JernArc'),
        
        P('start', '(0.0, 0.0)'),
        P('tangent', '(0.0, 1.0)'),  
        P('radius', 40.0 ),
        P('arc_size', 180.0),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(JernArc), visible=False), 

    ]),

    'Line': lambda: PG([
        P('shape', 'Line'),
        
        P('pts0', '(-1,-1)'),
        P('pts1', '(1,1)'),  

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(Line), visible=False), 

    ]),
    'PolarLine': lambda: PG([
        P('shape', 'PolarLine'),
        
        P('start', '(-1,-1)'),
        P('length', 2*2**.5),  
        P('angle', 45),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(PolarLine), visible=False), 

    ]),

    'Polyline': lambda: PG([
        P('shape', 'Polyline'),
        
        P('pts0', '(0, 0)'),
        P('pts1', '(20, 20)'),  
        P('pts2', '(40, 0)'),
        P('pts3', '(0, -40)' ),
        P('pts4',  '(-60, 0)'),
        P('pts5',  '(0, 100)'),
        P('pts6',  '(100, 0)'),  


        P('close', False),
        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(Polyline), visible=False), 

    ]),

    'RadiusArc': lambda: PG([
        P('shape', 'RadiusArc'),
        
        P('start_point', '(-30.0, 0.0)'),
        P('end_point', '(0,30.0)'),  
        P('radius', 30.0 ),
        P('short_sagitta', True),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(RadiusArc), visible=False), 

    ]),

    'SagittaArc': lambda: PG([
        P('shape', 'SagittaArc'),
        
        P('start_point', '(-30.0, 0.0)'),
        P('end_point', '(0,30.0)'),  

        P('sagitta', 20),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(SagittaArc), visible=False), 

    ]),

    'Spline': lambda: PG([
        P('shape', 'Spline'),
        
        P('pts0', '(-0, 0)'),
        P('pts1', '(20, 20)'),  
        P('pts2', '(40, 0)'),
        P('pts3', '(0, -40)' ),
        P('pts4',  '(-60, 0)'),
        P('pts5',  '(0, 100)'),
        P('pts6',  '(100, 0)'),  

        P('tangents', None, type='str', nullable=True),
        P('tangent_scalars', None, type='str', nullable=True),
        P('periodic', False),
        
        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(Spline), visible=False), 

    ]),
    'TangentArc': lambda: PG([
        P('shape', 'TangentArc'),
        
        P('pts0', '(-30.0, 0.0)'),
        P('pts1', '(0,30.0)'),  
        P('tangent', '(0,1)'),
        P('tangent_from_first', True),

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(TangentArc), visible=False), 

    ]),

    
    'ThreePointArc': lambda: PG([
        P('shape', 'ThreePointArc'),
        
        P('pts0', '(0,0)'),
        P('pts1', '(40,40)'),  
        P('pts2', '(80,0)'),  

        P('mode', 'Mode.ADD', options=getopts(Mode)), 
        P('code', sauce(ThreePointArc), visible=False), 

    ]),
}



#blueprint
def build(param):



    if param.shape.v != param.shape.prev:
        print(f'BUILDING: new <{param.shape.s}> prev <{param.shape.prev}>')
        p = index[param.shape.s]()
    else:
        p = param
   

    if p.shape.s in THREED:

        with BuildPart() as obj:


            if p.companion.v:
                Box(30,20,5)

            match p.shape.s:

                case 'Box':    
                    Box(
                        length = p.length.f,
                        width = p.width.f, 
                        height = p.height.f,
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,
                    )

                case 'Cone':
                    Cone(
                        p.bottom_radius.f, 
                        p.top_radius.f, 
                        p.height.f,
                        p.arc_size.f,   
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,
                    )

                case 'CounterBoreHole':
                    with Locations(obj.faces().sort_by(Axis.Z)[-1]):
                        CounterBoreHole(
                            p.radius.f,
                            p.counter_bore_radius.f,
                            p.counter_bore_depth.f,
                            p.depth.f,
                            p.mode.e
                        )

                case 'CounterSinkHole':
                    with Locations(obj.faces().sort_by(Axis.Z)[-1]):
                        CounterSinkHole(
                            p.radius.f,
                            p.counter_sink_radius.f,
                            p.depth.f,
                            p.counter_sink_angle.f,
                            p.mode.e,
                        )
                
                case 'Cylinder':
                    Cylinder(
                        p.radius.f,
                        p.height.f,
                        p.arc_size.f,
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,

                    )
                case 'Hole':
                    with Locations(obj.faces().sort_by(Axis.Z)[-1]):
                        Hole(
                            p.radius.f,
                            p.depth.f,
                            p.mode.e
                        )

                case 'Sphere':
                    Sphere(
                        p.radius.f,
                        p.arc_size1.f, 
                        p.arc_size2.f, 
                        p.arc_size3.f,
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,
                    )
                
                case 'Torus':
                    Torus(
                        p.major_radius.f,
                        p.minor_radius.f,
                        p.minor_start_angle.f,
                        p.minor_end_angle.f,
                        p.major_angle.f,
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,
                    )
                
                case 'Wedge':
                    Wedge(
                        p.xsize.f,
                        p.ysize.f,
                        p.zsize.f,
                        p.xmin.f,
                        p.zmin.f,
                        p.xmax.f,
                        p.zmax.f,
                        rotation= p.rotation.e,
                        align= (p.align_x.e, p.align_y.e, p.align_z.e),
                        mode= p.mode.e,
                    )
        
    elif p.shape.s in TWOD:
        with BuildPart() as obj:
            with BuildSketch(Plane.XY) as sket:

                if p.companion.v:
                    Rectangle(30,20)
                
                match p.shape.s:

                    case 'Arrow':
                        with BuildLine() as bline:
                            l1 = Polyline(p.pts0.e, p.pts1.e)

                        Arrow(
                            p.arrow_size.f,
                            l1,
                            p.shaft_width.f,
                            p.head_at_start.b,
                            p.head_type.e,
                            p.mode.e
                        )
                    
                    case 'ArrowHead':
                        ArrowHead(
                            p.size.f,
                            p.head_type.e,
                            p.rotation.f,
                            p.mode.e
                        )

                    case 'Circle':
                        Circle(
                            p.radius.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )
                    
                    case 'Ellipse':
                        Ellipse(
                            p.x_radius.f,
                            p.y_radius.f,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )
                    
                    case 'Polygon':
                        Polygon(
                            p.pts0.e,
                            p.pts1.e,
                            p.pts2.e,
                            p.pts3.e,
                            rotation = p.rotation.f,
                            align= (p.align_x.e, p.align_y.e),
                            mode=p.mode.e,
                        )
                    case 'Rectangle':
                        Rectangle(
                            p.width.f,
                            p.height.f,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )

                    case 'RectangleRounded':
                        RectangleRounded(
                            p.width.f,
                            p.height.f,
                            p.radius.f,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e,
                        )
                    
                    case 'RegularPolygon':
                        RegularPolygon(
                            p.radius.f,
                            p.side_count.i,
                            p.major_radius.b,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )

                    case 'SlotArc':
                        with BuildLine():
                            l1 = Polyline(p.pts0.e, p.pts1.e)
                        SlotArc(
                            l1,
                            p.height.f,
                            p.rotation.f,
                            p.mode.e
                        )
                    
                    case 'SlotCenterPoint': 
                        SlotCenterPoint(
                            p.center.e,
                            p.point.e,
                            p.height.f,
                            p.rotation.f,
                            p.mode.e
                        )

                    case 'SlotCenterToCenter':
                        SlotCenterToCenter(
                            p.center_separation.f,
                            p.height.f,
                            p.rotation.f,
                            p.mode.e
                        )
                    
                    case 'SlotOverall':
                        SlotOverall(
                            p.width.f,
                            p.height.f,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )

                    case 'Text':

                        if p.use_path.b:
                            l1 = p.path.e
                        else:
                            l1 = None
                        

                        Text(
                            p.txt.s,
                            p.font_size.f,
                            p.font.s,
                            p.font_path.s,
                            p.font_style.e,     
                            (p.align_x.e, p.align_y.e),
                            l1,
                            p.position_on_path.f,
                            p.rotation.f,
                            p.mode.e
                        )
                    case 'Trapezoid':
                        Trapezoid(
                            p.width.f,
                            p.height.f,
                            p.left_side_angle.f,
                            p.right_side_angle.f,
                            p.rotation.f,
                            (p.align_x.e, p.align_y.e),
                            p.mode.e
                        )



                    case 'Triangle':
                        Triangle(
                            a = p.a.f,
                            b = p.b.f,
                            c = p.c.f,
                            A = p.A.f,
                            B = p.B.f, 
                            C = p.C.f,
                            rotation = p.rotation.f,
                            align = (p.align_x.e, p.align_y.e),
                            mode = p.mode.e
                        )

            extrude(amount = p.extrude.f)
        
    else: #elif p.shape.s in ONED:
        
        match p.shape.s:

            case 'Bezier':
                obj = Bezier(p.pts0.e, 
                            p.pts1.e,
                            p.pts2.e,
                            p.pts3.e,
                            p.pts4.e,
                            p.pts5.e,
                            p.pts6.e,

                    
                            weights= p.wts.e
                            )
            case 'CenterArc':
                obj = CenterArc(p.center.e, p.radius.f, p.start_angle.f, p.arc_size.f)
            case 'DoubleTangentArc':
                obj = DoubleTangentArc(p.pnt.e, p.tangent.e, p.other.e)+ p.other.e
            case 'EllipticalCenterArc':
                obj = EllipticalCenterArc(
                    p.center.e,
                    p.x_radius.f, 
                    p.y_radius.f ,
                    p.start_angle.f, 
                    p.end_angle.f,
                    p.rotation.f,
                    p.angular_direction.e,
                    )
                
            case 'Helix':
                obj = Helix(
                    p.pitch.f,
                    p.height.f,
                    p.radius.f,
                    p.center.e,
                    p.direction.e,
                    p.cone_angle.f,
                    p.lefthand.b,

                )

            case 'FilletPolyline':
                obj = FilletPolyline(
                            p.pts0.e, 
                            p.pts1.e,
                            p.pts2.e,
                            p.pts3.e,
                            p.pts4.e,
                            p.pts5.e,
                            p.pts6.e,
                    
                            radius= p.radius.f,
                            close = p.close.b,

                            )
            case 'IntersectingLine':
                obj = IntersectingLine(p.start.e, p.direction.e, p.other.e) + p.other.e
            case 'JernArc':
                obj = JernArc(p.start.e, p.tangent.e, p.radius.f, p.arc_size.f)
            case 'Line':
                obj = Line(p.pts0.e, p.pts1.e)

            case 'PolarLine':
                obj = PolarLine(p.start.e, p.length.f, p.angle.f)
            
            case 'Polyline':
                obj = Polyline(p.pts0.e, 
                               p.pts1.e,
                               p.pts2.e,
                               p.pts3.e,
                               p.pts4.e,
                               p.pts5.e,
                               p.pts6.e,
                        
                               close = p.close.b
                               )
            case 'Spline':
                obj = Spline([
                                p.pts0.e, 
                                p.pts1.e,
                                p.pts2.e,
                                p.pts3.e,
                                p.pts4.e,
                                p.pts5.e,
                                p.pts6.e,
                                ])
            case 'RadiusArc':
                obj = RadiusArc(p.start_point.e, p.end_point.e, p.radius.f, p.short_sagitta.b)
            case 'SagittaArc':
                obj = SagittaArc(p.start_point.e, p.end_point.e, p.sagitta.f)
            case 'TangentArc':
                obj = TangentArc(p.pts0.e, p.pts1.e, tangent=p.tangent.e, tangent_from_first=p.tangent_from_first.b)
            case 'ThreePointArc':
                obj = ThreePointArc(p.pts0.e, p.pts1.e, p.pts2.e,)
            

    p.shape.options = list(index.keys())
    return obj, p


def init(request = None):

    shapelist = list(index.keys())
    if request and request in shapelist:
        shape = request

    else:
        from random import randint as rand
        shape = shapelist [ rand(0, len(shapelist)-1) ]

    return build(index[shape]())



if __name__ == '__main__':
    from .abcq_tui import launch

    print ('building init...')
        
    obj, params = init()

    print('template ✅')

    show(obj)
    launch(params, build, show)

    print('goodbye')

        
