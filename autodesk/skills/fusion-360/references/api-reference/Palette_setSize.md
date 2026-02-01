# Palette.setSize Method

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Sets the size of the palette. This is best used for a floating palette because either the width or height can be locked when a palette is docked.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a [Palette](Palette.htm) object.```` ``` returnValue = palette_var.setSize(width, height) ``` ```` |

"palette\_var" is a variable referencing a [Palette](Palette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the sizing was succesful. It is still considered a success even if the width or height could not be changed because of how the palette is docked or snapped. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | Specifies the width of the palette. Depending on how the palette is docked or snapped, the width may not be editable. |
| height | integer | Specifies the height of the palette. Depending on how the palette is docked or snapped, the height may not be editable. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |