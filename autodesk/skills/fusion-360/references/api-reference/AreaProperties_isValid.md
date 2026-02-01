# AreaProperties.isValid Property

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"areaProperties\_var" is a variable referencing an AreaProperties object. |

"areaProperties\_var" is a variable referencing an AreaProperties object. ```` ``` #include <Fusion/Fusion/AreaProperties.h>  // Get the value of the property. boolean propertyValue = areaProperties_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |