# CanvasEffects.objectType Property

Parent Object: [CanvasEffects](CanvasEffects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CanvasEffects.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasEffects\_var" is a variable referencing a CanvasEffects object.  ```` ``` # Get the value of the property. propertyValue = canvasEffects_var.objectType ``` ```` |

"canvasEffects\_var" is a variable referencing a CanvasEffects object. ```` ``` #include <Core/Application/CanvasEffects.h>  // Get the value of the property. string propertyValue = canvasEffects_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |