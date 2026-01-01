# Canvases.isValid Property

Parent Object: [Canvases](Canvases.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvases.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvases\_var" is a variable referencing a Canvases object. |

"canvases\_var" is a variable referencing a Canvases object. ```` ``` #include <Fusion/Image/Canvases.h>  // Get the value of the property. boolean propertyValue = canvases_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |