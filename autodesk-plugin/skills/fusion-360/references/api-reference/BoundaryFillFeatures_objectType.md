# BoundaryFillFeatures.objectType Property

Parent Object: [BoundaryFillFeatures](BoundaryFillFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatures\_var" is a variable referencing a BoundaryFillFeatures object.  ```` ``` # Get the value of the property. propertyValue = boundaryFillFeatures_var.objectType ``` ```` |

"boundaryFillFeatures\_var" is a variable referencing a BoundaryFillFeatures object. ```` ``` #include <Fusion/Features/BoundaryFillFeatures.h>  // Get the value of the property. string propertyValue = boundaryFillFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |