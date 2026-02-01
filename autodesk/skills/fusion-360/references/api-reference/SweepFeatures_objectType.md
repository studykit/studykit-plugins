# SweepFeatures.objectType Property

Parent Object: [SweepFeatures](SweepFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatures\_var" is a variable referencing a SweepFeatures object.  ```` ``` # Get the value of the property. propertyValue = sweepFeatures_var.objectType ``` ```` |

"sweepFeatures\_var" is a variable referencing a SweepFeatures object. ```` ``` #include <Fusion/Features/SweepFeatures.h>  // Get the value of the property. string propertyValue = sweepFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |