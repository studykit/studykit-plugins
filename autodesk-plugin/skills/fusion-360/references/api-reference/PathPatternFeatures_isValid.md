# PathPatternFeatures.isValid Property

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a PathPatternFeatures object. |

"pathPatternFeatures\_var" is a variable referencing a PathPatternFeatures object. ```` ``` #include <Fusion/Features/PathPatternFeatures.h>  // Get the value of the property. boolean propertyValue = pathPatternFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |