# TemporaryBRepManager.createRuledSurface Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a new body by creating a ruled surface between the two input wire bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createRuledSurface(sectionOne, sectionTwo) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the created ruled surface as a BRepBody object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sectionOne | [BRepWire](BRepWire.htm) | BRepWire that defines the shape of the first section. |
| sectionTwo | [BRepWire](BRepWire.htm) | BRepWire that defines the shape of the second section. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |