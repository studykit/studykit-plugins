# Palette.snapTo Method

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Snaps this palette to another palette.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a [Palette](Palette.htm) object.```` ``` returnValue = palette_var.snapTo(palette, snapOption) ``` ```` |

"palette\_var" is a variable referencing a [Palette](Palette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the palette was successfully snapped to the other palette. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| palette | [Palette](Palette.htm) | Specifies the palette to snap to. |
| snapOption | [PaletteSnapOptions](PaletteSnapOptions.htm) | Specifies how this palette should be snapped to the other palette. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |