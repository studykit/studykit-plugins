# TextCommandPalette.setPosition Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Sets the position of the palette. If the palette is docked or snapped, this will result in changing it to be floating.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.setPosition(left, top) ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the position was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| left | integer | The position of the left side of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the left side of the screen and not the Fusion window. |
| top | integer | The position of the top of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the top of the screen and not the Fusion window. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |