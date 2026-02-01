# SketchTangentDistanceDimension.createForAssemblyContext Method

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm) object.```` ``` returnValue = sketchTangentDistanceDimension_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchTangentDistanceDimension\_var" is a variable referencing a [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |