# ReverseNormalFeatures.objectType Property

Parent Object: [ReverseNormalFeatures](ReverseNormalFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeatures\_var" is a variable referencing a ReverseNormalFeatures object.  ```` ``` # Get the value of the property. propertyValue = reverseNormalFeatures_var.objectType ``` ```` |

"reverseNormalFeatures\_var" is a variable referencing a ReverseNormalFeatures object. ```` ``` #include <Fusion/Features/ReverseNormalFeatures.h>  // Get the value of the property. string propertyValue = reverseNormalFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |