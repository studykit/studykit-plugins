# HoleFeatures.objectType Property

Parent Object: [HoleFeatures](HoleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatures\_var" is a variable referencing a HoleFeatures object.  ```` ``` # Get the value of the property. propertyValue = holeFeatures_var.objectType ``` ```` |

"holeFeatures\_var" is a variable referencing a HoleFeatures object. ```` ``` #include <Fusion/Features/HoleFeatures.h>  // Get the value of the property. string propertyValue = holeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |