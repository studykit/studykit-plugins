# CanvasInput.objectType Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object.  ```` ``` # Get the value of the property. propertyValue = canvasInput_var.objectType ``` ```` |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. string propertyValue = canvasInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |