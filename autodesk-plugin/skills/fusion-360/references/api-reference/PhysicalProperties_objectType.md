# PhysicalProperties.objectType Property

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"physicalProperties\_var" is a variable referencing a PhysicalProperties object.  ```` ``` # Get the value of the property. propertyValue = physicalProperties_var.objectType ``` ```` |

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. ```` ``` #include <Fusion/Fusion/PhysicalProperties.h>  // Get the value of the property. string propertyValue = physicalProperties_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |