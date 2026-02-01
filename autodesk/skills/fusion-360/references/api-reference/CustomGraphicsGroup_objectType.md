# CustomGraphicsGroup.objectType Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsGroup_var.objectType ``` ```` |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. string propertyValue = customGraphicsGroup_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |