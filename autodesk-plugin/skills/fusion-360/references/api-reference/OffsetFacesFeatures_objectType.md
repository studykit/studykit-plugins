# OffsetFacesFeatures.objectType Property

Parent Object: [OffsetFacesFeatures](OffsetFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeatures\_var" is a variable referencing an OffsetFacesFeatures object.  ```` ``` # Get the value of the property. propertyValue = offsetFacesFeatures_var.objectType ``` ```` |

"offsetFacesFeatures\_var" is a variable referencing an OffsetFacesFeatures object. ```` ``` #include <Fusion/Features/OffsetFacesFeatures.h>  // Get the value of the property. string propertyValue = offsetFacesFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |