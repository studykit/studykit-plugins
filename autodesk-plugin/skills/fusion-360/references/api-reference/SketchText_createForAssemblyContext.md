# SketchText.createForAssemblyContext Method

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Creates a proxy object for the SketchText object that represents the SketchText object in the context of an assembly. The context is defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object.```` ``` returnValue = sketchText_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchText](SketchText.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |