# SketchLinearDiameterDimension.createForAssemblyContext Method

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm) object.```` ``` returnValue = sketchLinearDiameterDimension_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchLinearDiameterDimension\_var" is a variable referencing a [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |