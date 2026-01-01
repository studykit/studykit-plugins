# TextCommandPalette.writeText Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Write the specified text to the TEXT COMMAND window.

## Remarks

Below is some sample code that illustrates making sure the palette is visible and writing some text to it.

```
# Get the palette that represents the TEXT COMMANDS window.
textPalette = ui.palettes.itemById('TextCommands')

# Make sure the palette is visible.
if not textPalette.isVisible:
  textPalette.isVisible = True

# Write some text.
textPalette.writeText('This is a text message.')
```

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.writeText(text) ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| text | string | The text to write to the Text Command window. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |