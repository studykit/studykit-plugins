# CustomGraphicsEntity.objectType Property

Parent Object: [CustomGraphicsEntity](CustomGraphicsEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsEntity.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsEntity\_var" is a variable referencing a CustomGraphicsEntity object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsEntity_var.objectType ``` ```` |

"customGraphicsEntity\_var" is a variable referencing a CustomGraphicsEntity object. ```` ``` #include <Fusion/Graphics/CustomGraphicsEntity.h>  // Get the value of the property. string propertyValue = customGraphicsEntity_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |