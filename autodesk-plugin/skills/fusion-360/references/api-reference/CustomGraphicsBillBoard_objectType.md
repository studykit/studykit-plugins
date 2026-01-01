# CustomGraphicsBillBoard.objectType Property

Parent Object: [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsBillBoard_var.objectType ``` ```` |

"customGraphicsBillBoard\_var" is a variable referencing a CustomGraphicsBillBoard object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBillBoard.h>  // Get the value of the property. string propertyValue = customGraphicsBillBoard_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |