# EllipticalCylinder.isValid Property

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. |

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. ```` ``` #include <Core/Geometry/EllipticalCylinder.h>  // Get the value of the property. boolean propertyValue = ellipticalCylinder_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |