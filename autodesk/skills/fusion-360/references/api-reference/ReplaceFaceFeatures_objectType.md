# ReplaceFaceFeatures.objectType Property

Parent Object: [ReplaceFaceFeatures](ReplaceFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatures\_var" is a variable referencing a ReplaceFaceFeatures object.  ```` ``` # Get the value of the property. propertyValue = replaceFaceFeatures_var.objectType ``` ```` |

"replaceFaceFeatures\_var" is a variable referencing a ReplaceFaceFeatures object. ```` ``` #include <Fusion/Features/ReplaceFaceFeatures.h>  // Get the value of the property. string propertyValue = replaceFaceFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |