# CoincidentToSurfaceConstraint.createForAssemblyContext Method

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm) object.```` ``` returnValue = coincidentToSurfaceConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"coincidentToSurfaceConstraint\_var" is a variable referencing a [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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