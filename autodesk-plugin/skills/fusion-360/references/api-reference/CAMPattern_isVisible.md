# CAMPattern.isVisible Property

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a CAMPattern object. |

"cAMPattern\_var" is a variable referencing a CAMPattern object. ```` ``` #include <Cam/CAM/CAMPattern.h>  // Get the value of the property. boolean propertyValue = cAMPattern_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |