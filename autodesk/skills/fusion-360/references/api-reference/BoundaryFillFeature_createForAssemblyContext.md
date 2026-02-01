# BoundaryFillFeature.createForAssemblyContext Method

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a [BoundaryFillFeature](BoundaryFillFeature.htm) object.```` ``` returnValue = boundaryFillFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a [BoundaryFillFeature](BoundaryFillFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundaryFillFeature](BoundaryFillFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |