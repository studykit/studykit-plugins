# OffsetFeature.objectType Property

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an OffsetFeature object.  ```` ``` # Get the value of the property. propertyValue = offsetFeature_var.objectType ``` ```` |

"offsetFeature\_var" is a variable referencing an OffsetFeature object. ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Get the value of the property. string propertyValue = offsetFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |