# CombineFeature.objectType Property

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a CombineFeature object.  ```` ``` # Get the value of the property. propertyValue = combineFeature_var.objectType ``` ```` |

"combineFeature\_var" is a variable referencing a CombineFeature object. ```` ``` #include <Fusion/Features/CombineFeature.h>  // Get the value of the property. string propertyValue = combineFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |