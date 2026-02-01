# CustomGraphicsViewScale.objectType Property

Parent Object: [CustomGraphicsViewScale](CustomGraphicsViewScale.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewScale.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsViewScale_var.objectType ``` ```` |

"customGraphicsViewScale\_var" is a variable referencing a CustomGraphicsViewScale object. ```` ``` #include <Fusion/Graphics/CustomGraphicsViewScale.h>  // Get the value of the property. string propertyValue = customGraphicsViewScale_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |