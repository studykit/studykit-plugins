# RipFeatureInput.setAlongEdge Method

Parent Object: [RipFeatureInput](RipFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureInput.h>

## Description

Specifies the rip feature will be along an edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object.```` ``` returnValue = ripFeatureInput_var.setAlongEdge(edge, gapDistance) ``` ```` |

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the defining the rip is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edge | [BRepEdge](BRepEdge.htm) | The BRepEdge that defines the location of the rip. |
| gapDistance | [ValueInput](ValueInput.htm) | The gap distance of the rip. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |