# SketchOffsetDimension.createForAssemblyContext Method

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a [SketchOffsetDimension](SketchOffsetDimension.htm) object.```` ``` returnValue = sketchOffsetDimension_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchOffsetDimension\_var" is a variable referencing a [SketchOffsetDimension](SketchOffsetDimension.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchOffsetDimension](SketchOffsetDimension.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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