# SplitBodyFeatures.objectType Property

Parent Object: [SplitBodyFeatures](SplitBodyFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatures\_var" is a variable referencing a SplitBodyFeatures object.  ```` ``` # Get the value of the property. propertyValue = splitBodyFeatures_var.objectType ``` ```` |

"splitBodyFeatures\_var" is a variable referencing a SplitBodyFeatures object. ```` ``` #include <Fusion/Features/SplitBodyFeatures.h>  // Get the value of the property. string propertyValue = splitBodyFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |