# ParallelConstraint.createForAssemblyContext Method

Parent Object: [ParallelConstraint](ParallelConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ParallelConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parallelConstraint\_var" is a variable referencing a [ParallelConstraint](ParallelConstraint.htm) object.```` ``` returnValue = parallelConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"parallelConstraint\_var" is a variable referencing a [ParallelConstraint](ParallelConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ParallelConstraint](ParallelConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |