# SketchControlPointSpline.createForAssemblyContext Method

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a [SketchControlPointSpline](SketchControlPointSpline.htm) object.```` ``` returnValue = sketchControlPointSpline_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchControlPointSpline\_var" is a variable referencing a [SketchControlPointSpline](SketchControlPointSpline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchControlPointSpline](SketchControlPointSpline.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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