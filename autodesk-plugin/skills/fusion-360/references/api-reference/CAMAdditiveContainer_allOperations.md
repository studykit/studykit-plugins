# CAMAdditiveContainer.allOperations Property

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Gets a collection containing all of the operations in this container. This includes all operations nested in folders and patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. |

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. ```` ``` #include <Cam/CAM/CAMAdditiveContainer.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = cAMAdditiveContainer_var->allOperations(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |