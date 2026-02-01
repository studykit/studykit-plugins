# CAMHoleRecognition.children Property

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this folder in the order they appear in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. |

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. ```` ``` #include <Cam/CAM/CAMHoleRecognition.h>  // Get the value of the property. Ptr<ChildOperationList> propertyValue = cAMHoleRecognition_var->children(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChildOperationList](ChildOperationList.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |