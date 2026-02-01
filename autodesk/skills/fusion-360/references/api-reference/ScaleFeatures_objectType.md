# ScaleFeatures.objectType Property

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a ScaleFeatures object.  ```` ``` # Get the value of the property. propertyValue = scaleFeatures_var.objectType ``` ```` |

"scaleFeatures\_var" is a variable referencing a ScaleFeatures object. ```` ``` #include <Fusion/Features/ScaleFeatures.h>  // Get the value of the property. string propertyValue = scaleFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |