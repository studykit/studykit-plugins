# SketchDiameterDimension.createForAssemblyContext Method

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a [SketchDiameterDimension](SketchDiameterDimension.htm) object.```` ``` returnValue = sketchDiameterDimension_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchDiameterDimension\_var" is a variable referencing a [SketchDiameterDimension](SketchDiameterDimension.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchDiameterDimension](SketchDiameterDimension.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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