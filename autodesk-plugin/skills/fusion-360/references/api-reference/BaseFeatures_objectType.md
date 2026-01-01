# BaseFeatures.objectType Property

Parent Object: [BaseFeatures](BaseFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeatures\_var" is a variable referencing a BaseFeatures object.  ```` ``` # Get the value of the property. propertyValue = baseFeatures_var.objectType ``` ```` |

"baseFeatures\_var" is a variable referencing a BaseFeatures object. ```` ``` #include <Fusion/Features/BaseFeatures.h>  // Get the value of the property. string propertyValue = baseFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |