# BoxFeature.objectType Property

Parent Object: [BoxFeature](BoxFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeature\_var" is a variable referencing a BoxFeature object.  ```` ``` # Get the value of the property. propertyValue = boxFeature_var.objectType ``` ```` |

"boxFeature\_var" is a variable referencing a BoxFeature object. ```` ``` #include <Fusion/Features/BoxFeature.h>  // Get the value of the property. string propertyValue = boxFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |