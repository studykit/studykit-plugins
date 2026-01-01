# CAMFolder.allOperations Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Gets a collection containing all of the operations in this folder. This includes all operations nested in folders and patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = cAMFolder_var->allOperations(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |