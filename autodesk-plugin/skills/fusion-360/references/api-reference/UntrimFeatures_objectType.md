# UntrimFeatures.objectType Property

Parent Object: [UntrimFeatures](UntrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatures\_var" is a variable referencing a UntrimFeatures object.  ```` ``` # Get the value of the property. propertyValue = untrimFeatures_var.objectType ``` ```` |

"untrimFeatures\_var" is a variable referencing a UntrimFeatures object. ```` ``` #include <Fusion/Features/UntrimFeatures.h>  // Get the value of the property. string propertyValue = untrimFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |