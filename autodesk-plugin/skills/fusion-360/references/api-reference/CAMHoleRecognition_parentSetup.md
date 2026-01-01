# CAMHoleRecognition.parentSetup Property

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Gets the Setup this operation belongs to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. |

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. ```` ``` #include <Cam/CAM/CAMHoleRecognition.h>  // Get the value of the property. Ptr<Setup> propertyValue = cAMHoleRecognition_var->parentSetup(); ``` ```` |

## Property Value

This is a read only property whose value is a [Setup](Setup.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |