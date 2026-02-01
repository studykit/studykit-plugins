# UnstitchFeatures.isValid Property

Parent Object: [UnstitchFeatures](UnstitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeatures\_var" is a variable referencing a UnstitchFeatures object. |

"unstitchFeatures\_var" is a variable referencing a UnstitchFeatures object. ```` ``` #include <Fusion/Features/UnstitchFeatures.h>  // Get the value of the property. boolean propertyValue = unstitchFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |