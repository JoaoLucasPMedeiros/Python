import json
from pprint import pprint
from typing import TypedDict

class CONFIG (TypedDict):
    workbench_colorTheme: str
    workbench_iconTheme: str
    editor_fontSize: int
    editor_fontWeight: int
    editor_fontFamily: str
    editor_minimap_enabled: bool
    editor_wordWrap: str
    terminal_integrated_fontSize: int
    terminal_integrated_fontFamily: str
    terminal_integrated_fontWeight: str

string_json = '''
{
    "workbench_colorTheme": "Default Dark Modern",
    "workbench_iconTheme": "material-icon-theme",
    "editor_fontSize": 20,
    "editor_fontWeight": "500",
    "editor_fontFamily": "Raleway",
    "editor_minimap.enabled": false,
    "editor_wordWrap": "on",
    "terminal_integrated.fontSize": 22,
    "terminal_integrated.fontFamily": "monospace",
    "terminal_integrated.fontWeight": "bold"
}
'''

str_json = {
    'workbench_colorTheme': 'Default Dark Modern', 'workbench_iconTheme': 'material-icon-theme', 'editor_fontSize': 20, 'editor_fontWeight': '500', 'editor_fontFamily': 'Raleway', 'editor_minimap.enabled': False, 'editor_wordWrap': 'on', 'terminal_integrated.fontSize': 22, 'terminal_integrated.fontFamily': 'monospace', 'terminal_integrated.fontWeight': 'bold'
            }

#config:CONFIG = json.loads(string_json)
config = json.loads(string_json)
print(config)
#print(config['editor_wordWrap'])