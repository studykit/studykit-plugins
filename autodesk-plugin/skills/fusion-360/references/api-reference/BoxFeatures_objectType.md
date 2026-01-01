# BoxFeatures.objectType Property

Parent Object: [BoxFeatures](BoxFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeatures\_var" is a variable referencing a BoxFeatures object.  ```` ``` # Get the value of the property. propertyValue = boxFeatures_var.objectType ``` ```` |

"boxFeatures\_var" is a variable referencing a BoxFeatures object. ```` ``` #include <Fusion/Features/BoxFeatures.h>  // Get the value of the property. string propertyValue = boxFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |