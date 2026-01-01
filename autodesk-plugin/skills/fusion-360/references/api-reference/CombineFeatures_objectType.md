# CombineFeatures.objectType Property

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a CombineFeatures object.  ```` ``` # Get the value of the property. propertyValue = combineFeatures_var.objectType ``` ```` |

"combineFeatures\_var" is a variable referencing a CombineFeatures object. ```` ``` #include <Fusion/Features/CombineFeatures.h>  // Get the value of the property. string propertyValue = combineFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |