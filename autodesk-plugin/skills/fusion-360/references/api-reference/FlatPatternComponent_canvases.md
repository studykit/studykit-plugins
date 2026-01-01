# FlatPatternComponent.canvases Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the canvases collection associated with this component. This provides access to the existing canvases and supports the creation of new canvases.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<Canvases> propertyValue = flatPatternComponent_var->canvases(); ``` ```` |

## Property Value

This is a read only property whose value is a [Canvases](Canvases.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |