# PathPatternFeature.entityToken Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeature_var.entityToken ``` ```` |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. string propertyValue = pathPatternFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |