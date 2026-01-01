# RipFeature.redefineToAlongEdge Method

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Redefines the feature to be a rip along an edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object.```` ``` returnValue = ripFeature_var.redefineToAlongEdge(edge, gapDistance) ``` ```` |

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the rip definition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edge | [BRepEdge](BRepEdge.htm) | The BRepEdge that defines the rip. |
| gapDistance | [ValueInput](ValueInput.htm) | The gap distance of the rip. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |