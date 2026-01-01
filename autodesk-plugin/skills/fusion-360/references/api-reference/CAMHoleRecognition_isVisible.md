# CAMHoleRecognition.isVisible Property

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. |

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. ```` ``` #include <Cam/CAM/CAMHoleRecognition.h>  // Get the value of the property. boolean propertyValue = cAMHoleRecognition_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |