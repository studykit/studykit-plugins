# SplitFaceFeatures.objectType Property

Parent Object: [SplitFaceFeatures](SplitFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatures\_var" is a variable referencing a SplitFaceFeatures object.  ```` ``` # Get the value of the property. propertyValue = splitFaceFeatures_var.objectType ``` ```` |

"splitFaceFeatures\_var" is a variable referencing a SplitFaceFeatures object. ```` ``` #include <Fusion/Features/SplitFaceFeatures.h>  // Get the value of the property. string propertyValue = splitFaceFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |