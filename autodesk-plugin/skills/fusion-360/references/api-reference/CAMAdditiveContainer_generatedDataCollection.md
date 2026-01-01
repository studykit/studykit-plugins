# CAMAdditiveContainer.generatedDataCollection Property

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. |

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. ```` ``` #include <Cam/CAM/CAMAdditiveContainer.h>  // Get the value of the property. Ptr<GeneratedDataCollection> propertyValue = cAMAdditiveContainer_var->generatedDataCollection(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeneratedDataCollection](GeneratedDataCollection.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |