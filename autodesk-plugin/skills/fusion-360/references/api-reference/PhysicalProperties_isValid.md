# PhysicalProperties.isValid Property

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. |

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. ```` ``` #include <Fusion/Fusion/PhysicalProperties.h>  // Get the value of the property. boolean propertyValue = physicalProperties_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |