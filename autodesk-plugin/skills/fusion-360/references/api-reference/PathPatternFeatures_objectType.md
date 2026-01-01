# PathPatternFeatures.objectType Property

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a PathPatternFeatures object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeatures_var.objectType ``` ```` |

"pathPatternFeatures\_var" is a variable referencing a PathPatternFeatures object. ```` ``` #include <Fusion/Features/PathPatternFeatures.h>  // Get the value of the property. string propertyValue = pathPatternFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |