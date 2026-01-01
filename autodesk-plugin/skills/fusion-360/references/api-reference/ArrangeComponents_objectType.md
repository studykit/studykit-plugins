# ArrangeComponents.objectType Property

Parent Object: [ArrangeComponents](ArrangeComponents.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponents.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponents\_var" is a variable referencing an ArrangeComponents object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponents_var.objectType ``` ```` |

"arrangeComponents\_var" is a variable referencing an ArrangeComponents object. ```` ``` #include <Fusion/Arrange/ArrangeComponents.h>  // Get the value of the property. string propertyValue = arrangeComponents_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |