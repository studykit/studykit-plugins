# ZebraAnalyses.objectType Property

Parent Object: [ZebraAnalyses](ZebraAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalyses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalyses\_var" is a variable referencing a ZebraAnalyses object.  ```` ``` # Get the value of the property. propertyValue = zebraAnalyses_var.objectType ``` ```` |

"zebraAnalyses\_var" is a variable referencing a ZebraAnalyses object. ```` ``` #include <Fusion/Fusion/ZebraAnalyses.h>  // Get the value of the property. string propertyValue = zebraAnalyses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |