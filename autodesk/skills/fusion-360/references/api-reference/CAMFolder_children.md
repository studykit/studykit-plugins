# CAMFolder.children Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this folder in the order they appear in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. Ptr<ChildOperationList> propertyValue = cAMFolder_var->children(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChildOperationList](ChildOperationList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |