from rich.syntax import Syntax

from textual.app import App, ComposeResult
from textual.widgets import Input, Switch, Markdown, Label, Footer, Button, Static, RadioSet, RadioButton
from textual.screen import ModalScreen
from textual import containers, lazy
from textual.containers import ScrollableContainer, Vertical
from textual.binding import Binding
from textual.screen import  Screen
from textual.suggester import SuggestFromList

from traceback import print_exc


from .build_utils import *


class Inputs(containers.VerticalGroup):
    ALLOW_MAXIMIZE = True
    DEFAULT_CLASSES = "column"
    DEFAULT_CSS = """
    Inputs {
        Grid {
            background: $boost;
            padding: 0 1;
            height: auto;
            grid-size: 2;
            grid-gutter: 0;
            grid-columns: auto 1fr;
            border: tall blank;
            &:focus-within {
                border: tall $accent;
            }
            Label {
                width: 100%;
                padding: 1;
                text-align: right;
            }
            Button {
                    width: 100%;
                    min-width: 16;
                    height: auto;
                    color: $button-foreground;
                    background: $surface;
                    border: none;
                    border-top: tall $surface-lighten-1;
                    border-bottom: tall $surface-darken-1;
                    text-align: center;
                    content-align: center middle;
                    text-style: bold;
                    line-pad: 1;

                    &.-textual-compact {
                        border: none !important;
                    }

                    &:disabled {            
                        text-opacity: 0.6;
                    }
                    
                    &:focus {
                        text-style: $button-focus-text-style;
                        background-tint: $foreground 5%;
                    }
                    &:hover {
                        border-top: tall $surface;
                        background: $surface-darken-1;
                    }
                    &.-active {
                        background: $surface;
                        border-bottom: tall $surface-lighten-1;
                        border-top: tall $surface-darken-1;
                        tint: $background 30%;
                    }

                    &.-primary {
                        color: $button-color-foreground;
                        background: $primary;
                        border-top: tall $primary-lighten-3;
                        border-bottom: tall $primary-darken-3;

                        &:hover {
                            background: $primary-darken-2;
                            border-top: tall $primary;
                        }

                        &.-active {
                            background: $primary;
                            border-bottom: tall $primary-lighten-3;
                            border-top: tall $primary-darken-3;
                        }
                    }

                    &.-success {
                        color: $button-color-foreground;
                        background: $success;
                        border-top: tall $success-lighten-2;
                        border-bottom: tall $success-darken-3;

                        &:hover {
                            background: $success-darken-2;
                            border-top: tall $success;
                        }

                        &.-active {
                            background: $success;
                            border-bottom: tall $success-lighten-2;
                            border-top: tall $success-darken-2;
                        }
                    }

                    &.-warning{
                        color: $button-color-foreground;
                        background: $warning;
                        border-top: tall $warning-lighten-2;
                        border-bottom: tall $warning-darken-3;

                        &:hover {
                            background: $warning-darken-2;
                            border-top: tall $warning;
                        }

                        &.-active {
                            background: $warning;
                            border-bottom: tall $warning-lighten-2;
                            border-top: tall $warning-darken-2;
                        }
                    }

                    &.-error {
                        color: $button-color-foreground;
                        background: $error;
                        border-top: tall $error-lighten-2;
                        border-bottom: tall $error-darken-3;

                        &:hover {
                            background: $error-darken-1;
                            border-top: tall $error;
                        }

                        &.-active {
                            background: $error;
                            border-bottom: tall $error-lighten-2;
                            border-top: tall $error-darken-2;
                        }
                    }
                }

            #Toggle {
                width: 100%;
            }

            RadioSet {
                border: tall $border-blurred;
                background: $surface;
                padding: 0 1;        
                height: auto;
                width: 1fr;

                &.-textual-compact {
                    border: none !important;
                    padding: 0;
                }

                & > RadioButton {
                    background: transparent;
                    border: none;
                    padding: 0;
                    width: 1fr;

                    & > .toggle--button {
                        color: $panel-darken-2;
                        background: $panel;
                    }

                    &.-selected {
                        background: transparent;
                    }
                }

                & > RadioButton.-on .toggle--button {
                    color: #cc0000;
                }

                &:focus {
                    /* The following rules/styles mimic similar ToggleButton:focus rules in
                    * ToggleButton. If those styles ever get updated, these should be too.
                    */
                    border: tall $border;
                    background-tint: $foreground 5%;
                    & > RadioButton.-selected {
                        color: $block-cursor-foreground;
                        text-style: $block-cursor-text-style;
                        background: $block-cursor-background;
                    }

                }
            }
        }
    }
    """

    def __init__(self, params) -> None:
        super().__init__()
        self.params = params
        print(f'INPUTS: {type(self.params)}')

    

    def on_button_pressed(self, event: Button.Pressed):
        # self.notify(event.button.id)
        if event.button.id.split('_')[0]=='clear':
            # self.notify('clear '+event.button.param.name)
            event.button.param.value = None

            for child in self.children[0].children:
                # self.notify(str(type(child)))
                # break
                if type(child)==MyInput:
                    if child.param.name == event.button.param.name:
                        child.value = 'None'

                        break
        


    def compose(self) -> ComposeResult:
        with containers.Grid():

            visi = [p for p in self.params.children if p.visible]
            for param in visi:


                if not param.nullable:
                    yield Label(param.name) 
                else:
                    yield ClearButton(param)

                match param.type:
                    case "num":
                        yield MyInput(param=param, value=param.s, valid_empty=True )
                    case "bool":
                        yield MySwitch(param=param, value=param.b)
                    case _:

                        if param.name == 'shape':
                            yield ShapeWidget(param=param)
                            continue

                        if len(param.options) > 0 and len(param.options) <= 6:
                            yield MyRadioSet(param=param)
                        elif len(param.options) > 6:
                            yield MyInput(
                                param=param, 
                                value=param.s, 
                                suggester= SuggestFromList(param.options)
                            )
                        else:
                            yield MyInput(
                                param=param, 
                                value=param.s, 
                                # valid_empty=True,
                            )

            yield Label('>'); yield Button('Run',id= 'Run')
            yield Label('>'); yield Button('Console', id='Console')
            yield Label('>');  yield Button('Save', id='Save')
            yield Label('>'); yield Button('Load', id='Load')
            yield Label('>'); yield Button("Exit",id= "Exit")
        # yield Markdown(self.params.shape_desc.s)
        # yield Markdown(self.params.code.s)


class ShapeWidget(Vertical):
    def __init__(self, param, **kwargs):
        super().__init__(**kwargs)
        self.param = param
        self.input_mode = True
    
    def compose(self):
        self.input_widget = MyInput(
                                param=self.param, 
                                value=self.param.s, 
                                suggester= SuggestFromList(self.param.options)
                            )
        yield self.input_widget

        self.radio = MyRadioSet(param=self.param)
        self.radio.display = False
        yield self.radio

        self.btn = Button( 'Shapes', id='Toggle')
        yield self.btn

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "Toggle":
            self.toggle_mode()
            if self.input_mode:
                self.btn.label = 'Shapes'
            else:
                self.btn.label = 'Cancel'

    def on_radio_set_changed(self, event: RadioSet.Changed):
        self.toggle_mode()

        self.input_widget.value = str(event.pressed.label)
        self.app.action_run()
        

    def toggle_mode(self):
        # self.clear()
        if self.input_mode:
            self.input_widget.display = False
            self.radio.display = True
        else:
            self.input_widget.display = True
            self.radio.display = False

        self.input_mode = not self.input_mode
        


class MyRadioSet(RadioSet):

    DEFAULT_CSS = ''
    def __init__(self, param, **kwargs):
        super().__init__(**kwargs)
        self.param = param

    def compose(self) -> ComposeResult:
        for option in self.param.options:
            yield RadioButton(option, value=(option == self.param.value))
        

        
    def highlight(self):
        for btn in list(self.children):
            self.notify ( f' {btn.value}  {btn.label}')

            
class ClearButton(Button):
     def __init__(self, param, **kwargs):
        super().__init__(label=param.name+' ❌', id='clear_'+param.name,**kwargs)
        self.param = param    
        # self.id = 'clear_'+param.name    


class MySwitch(Switch):
    def __init__(self, param, **kwargs):
        super().__init__(**kwargs)
        self.param = param

class MyInput(Input):

    def __init__(self, param, **kwargs):
        super().__init__(**kwargs)
        self.param = param

class CodeScreen(ModalScreen):
    DEFAULT_CSS = """
    CodeScreen {
        #code {
            border: heavy $accent;
            margin: 2 4;
            scrollbar-gutter: stable;
            Static {
                width: auto;
            }
        }
    }
    """
    BINDINGS = [("escape", "dismiss", "Dismiss code")]

    def __init__(self, title: str, code: str) -> None:
        super().__init__()
        self.code = code
        self.title = title

    def compose(self) -> ComposeResult:
        with ScrollableContainer(id="code"):
            yield Static(
                Syntax(
                    self.code, lexer="python", indent_guides=True, line_numbers=True
                ),
                expand=True,
            )

    def on_mount(self):
        code_widget = self.query_one("#code")
        code_widget.border_title = self.title
        code_widget.border_subtitle = "Escape to close"

class WidgetsScreen(Screen):
    """The Widgets screen"""

    CSS = """
    WidgetsScreen { 
        width: 100%;
        height: 1fr;
        overflow-y: auto;        
        align-horizontal: center;
        Markdown { background: transparent; }
        & > VerticalScroll {
            scrollbar-gutter: stable;
            & > * {                          
                &:even { background: $boost; }
                padding-bottom: 1;
            }
        }
    }
    """
    def __init__(self, params) -> None:
        super().__init__()
        self.params = params


    BINDINGS = [Binding("escape", "blur", "Unfocus any focused widget", show=False)]

    def compose(self) -> ComposeResult:
        with lazy.Reveal(containers.VerticalScroll(can_focus=True)):
            yield Inputs(self.params) 

        yield Footer()

class MyApp(App):
    """Individual playable cell in the game."""

    def __init__(self, params, build, show) -> None:
        super().__init__()

        self.params = params
        self.build = build
        self.show = show    
        self.msg = ''
        self.rebuild = False

    BINDINGS = [
        Binding(
            "c",
            "show_code",
            "Code",
            tooltip="Show the code used to generate this screen",
        ),

        Binding(
            'ctrl+r',
            'run',
            'Run',
        ),

        Binding(
            'q',
            'quit',
            'Exit',
        )


    ]

    def action_quit(self):
        self.msg = "e"
        self.exit() 

    def action_run(self):
    #     if not hasattr(self, '_run_count'):
    #         self._run_count = 0
    #     self._run_count += 1

        self.poll_inputs()
        if self.rebuild:
            self.exit()
        else:
            self.notify(f'Building {self.params.shape.s}... ')
            self.show(self.build(self.params))

    async def action_show_code(self):
        # source_file = inspect.getsourcefile(self.__class__)

        code = self.params.code.s
        # self.notify(str(type(code)))
        # self.notify(str(code))
        # print('test')
        # self.msg = 'e'
        # self.exit()
        if code is None:
            self.notify(
                "Could not get the code for this page",
                title="Show code",
                severity="error",
            )
        else:
            self.app.push_screen(CodeScreen("Code for this page", code))

    def get_default_screen(self) -> Screen:
        return WidgetsScreen(self.params)
    
    def poll_inputs(self):
        inputs = self.query(Input)
        switches = self.query(Switch)

        for s in switches:
            s.param.value = s.value


        for widg in inputs:
            if str(widg.value) != '':
                if widg.param.type=='num':
                    widg.param.value = float(widg.value) if widg.value != "None" else None
                else:
                    if widg.value == 'None' and widg.param.value == None:
                        pass
                    else:
                        widg.param.value = str(widg.value)

                ## CHECK FOR SHAPE UPDATE
                if widg.param.name=='shape' and widg.param.value != widg.param.prev:
                    self.rebuild = True

    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id

        if button_id == "Exit":
            
            self.msg = 'e'
            self.exit()
        
        elif button_id == 'Run':
            self.action_run()
        
        elif button_id == 'Console':
            self.poll_inputs()
            self.msg = 'c'
            self.exit()

        elif button_id == 'Other':
            self.notify('OTHER PRESSED')
        
        elif button_id == 'Save':
            self.save_params()
        elif button_id == 'Load':
            self.load_params()
    
    # def on_switch_changed(self, event: Switch.Changed):

    #     self.poll_inputs()
    #     if self.rebuild:
    #         self.exit()
    #     else:
    #         self.show(self.build(self.params))
    
    def on_input_submitted(self, event: Input.Submitted):

        self.action_run()

    def on_radio_set_changed(self, event: RadioSet.Changed):

        event.pressed.parent.param.value = str(event.pressed.label)

    def save_params(self):
        with open('params.json', 'w') as file:
            file.write(self.params.dumps())
        
    def load_params(self, file='params.json'):
        with open(file, 'r') as f:
            data = f.read()
    
        self.params = loadParam(data)
        self.exit()


        
# def launch(pgroup, buildfn, showfn):

#     while True:
#         app = MyApp(pgroup, buildfn, showfn)
#         app.run()

#         match app.msg:
#             case 'c':
#                 from code import interact
#                 print('\n\n\nType Ctrl+Z to return to Parameter UI\n\n')
#                 print(f'obj: {obj}\nparams: {params}')
#                 interact(local=locals())
#             case 'i':
#                 import IPython
#                 IPython.embed()
#             case 'pause':
#                 uip = input('pause ')
#             case 'e':
#                 break
#             case _:
#                 pass

#         obj, pgroup = app.build(app.params)
#         show(obj)
    

def loadinit(file='params.json'):
    with open(file, 'r') as f:
        data = f.read()
    return loadParam(data)


if __name__ == "__main__":
    from .generate import build, init
    from ocp_vscode import show
    import sys
    #from abcq import make as show

    # params = loadinit()
    # obj, params = build(params)

    banner_str = '''Welcome to shell. Type `exit` to return to TUI.

Example:

params.shape.value = "Box"
obj, params = build(params)
show( obj )


''' 


    obj, params = init(sys.argv[1] if len(sys.argv)>1 else None)
    show(obj)

    app = MyApp(params, build, show)
    app.run()

    while True:
        match app.msg:
            case 'c':
                from code import interact

                print(f'obj: {obj}\nparams: {params}')

                # print('\n\n\nType Ctrl+Z to return to Parameter UI\n')
                # interact(local=locals())
                
                import IPython
                IPython.embed(colors='Linux',
                              banner1= banner_str,
                              exit_msg='Returning to TUI. Have a day!')

            case 'e':
                break
            case _:
                  
        
                try:
                    obj, params = build(app.params)
                    show(obj)

                except Exception as e:
                    print_exc()
                    # print(f'ERROR: {e}')
                    input('Continue? ')


        app = MyApp(params, app.build, app.show)
        app.run()

        # pause = input()




def launch(request=None):

    from .generate import build, init
    from ocp_vscode import show

    banner_str = '''Welcome to shell. Type `exit` to return to TUI.

Example:

params.shape.value = "Box"
obj, params = build(params)
show( obj )


''' 


    obj, params = init(request)
    show(obj)

    app = MyApp(params, build, show)
    app.run()

    while True:
        match app.msg:
            case 'c':
                from code import interact

                print(f'obj: {obj}\nparams: {params}')

                # print('\n\n\nType Ctrl+Z to return to Parameter UI\n')
                # interact(local=locals())
                
                import IPython
                IPython.embed(colors='Linux',
                              banner1= banner_str,
                              exit_msg='Returning to TUI. Have a day!')

            case 'e':
                break
            case _:
                  
        
                try:
                    obj, params = build(app.params)
                    show(obj)

                except Exception as e:
                    print_exc()
                    # print(f'ERROR: {e}')
                    input('Continue? ')


        app = MyApp(params, app.build, app.show)
        app.run()