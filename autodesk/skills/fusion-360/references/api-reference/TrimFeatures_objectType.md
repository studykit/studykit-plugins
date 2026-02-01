# TrimFeatures.objectType Property

Parent Object: [TrimFeatures](TrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatures\_var" is a variable referencing a TrimFeatures object.  ```` ``` # Get the value of the property. propertyValue = trimFeatures_var.objectType ``` ```` |

"trimFeatures\_var" is a variable referencing a TrimFeatures object. ```` ``` #include <Fusion/Features/TrimFeatures.h>  // Get the value of the property. string propertyValue = trimFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |