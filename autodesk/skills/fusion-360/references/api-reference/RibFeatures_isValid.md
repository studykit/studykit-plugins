# RibFeatures.isValid Property

Parent Object: [RibFeatures](RibFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeatures\_var" is a variable referencing a RibFeatures object. |

"ribFeatures\_var" is a variable referencing a RibFeatures object. ```` ``` #include <Fusion/Features/RibFeatures.h>  // Get the value of the property. boolean propertyValue = ribFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |