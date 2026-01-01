# BaseFeature.objectType Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object.  ```` ``` # Get the value of the property. propertyValue = baseFeature_var.objectType ``` ```` |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. string propertyValue = baseFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |