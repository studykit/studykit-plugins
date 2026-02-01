# CAMAdditiveContainer.parentSetup Property

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Gets the Setup this operation belongs to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. |

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. ```` ``` #include <Cam/CAM/CAMAdditiveContainer.h>  // Get the value of the property. Ptr<Setup> propertyValue = cAMAdditiveContainer_var->parentSetup(); ``` ```` |

## Property Value

This is a read only property whose value is a [Setup](Setup.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |