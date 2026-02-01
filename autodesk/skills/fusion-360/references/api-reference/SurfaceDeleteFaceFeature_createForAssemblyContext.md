# SurfaceDeleteFaceFeature.createForAssemblyContext Method

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) object.```` ``` returnValue = surfaceDeleteFaceFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"surfaceDeleteFaceFeature\_var" is a variable referencing a [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |