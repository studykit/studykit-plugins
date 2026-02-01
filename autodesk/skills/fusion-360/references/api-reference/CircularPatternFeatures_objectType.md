# CircularPatternFeatures.objectType Property

Parent Object: [CircularPatternFeatures](CircularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatures\_var" is a variable referencing a CircularPatternFeatures object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeatures_var.objectType ``` ```` |

"circularPatternFeatures\_var" is a variable referencing a CircularPatternFeatures object. ```` ``` #include <Fusion/Features/CircularPatternFeatures.h>  // Get the value of the property. string propertyValue = circularPatternFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |