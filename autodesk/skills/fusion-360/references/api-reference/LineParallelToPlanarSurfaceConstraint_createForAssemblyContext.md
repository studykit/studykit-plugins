# LineParallelToPlanarSurfaceConstraint.createForAssemblyContext Method

Parent Object: [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineParallelToPlanarSurfaceConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm) object.```` ``` returnValue = lineParallelToPlanarSurfaceConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |