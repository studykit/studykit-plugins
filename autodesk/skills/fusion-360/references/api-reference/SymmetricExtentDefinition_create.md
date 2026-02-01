# SymmetricExtentDefinition.create Method

Parent Object: [SymmetricExtentDefinition](SymmetricExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SymmetricExtentDefinition.h>

## Description

Statically creates a new SymmetricExtentDefinition object. This is used as input when create a new feature and defining the starting condition.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SymmetricExtentDefinition](SymmetricExtentDefinition.htm) | Returns the newly created SymmetricExtentDefinition or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| distance | [ValueInput](ValueInput.htm) | An input ValueInput objects that defines either half the extent of the extrude or the full extent, depending on the value of the isFullLength argument. |
| isFullLength | boolean | An input boolean that specifies if the distance specified defines the full or half length of the extrusion. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |