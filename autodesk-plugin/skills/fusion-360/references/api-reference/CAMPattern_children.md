# CAMPattern.children Property

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this folder in the order they appear in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a CAMPattern object. |

"cAMPattern\_var" is a variable referencing a CAMPattern object. ```` ``` #include <Cam/CAM/CAMPattern.h>  // Get the value of the property. Ptr<ChildOperationList> propertyValue = cAMPattern_var->children(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChildOperationList](ChildOperationList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |