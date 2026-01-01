# ExtrudeFeatures.isValid Property

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an ExtrudeFeatures object. |

"extrudeFeatures\_var" is a variable referencing an ExtrudeFeatures object. ```` ``` #include <Fusion/Features/ExtrudeFeatures.h>  // Get the value of the property. boolean propertyValue = extrudeFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |