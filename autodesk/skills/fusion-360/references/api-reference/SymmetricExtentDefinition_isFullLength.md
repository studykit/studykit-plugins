# SymmetricExtentDefinition.isFullLength Property

Parent Object: [SymmetricExtentDefinition](SymmetricExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SymmetricExtentDefinition.h>

## Description

Gets and sets if the distance defines the full extent length or half the length. A value of True indicates if defines the full length.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. |

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. ```` ``` #include <Fusion/Features/SymmetricExtentDefinition.h>  // Get the value of the property. boolean propertyValue = symmetricExtentDefinition_var->isFullLength();  // Set the value of the property, where value_var is a boolean. bool returnValue = symmetricExtentDefinition_var->isFullLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |