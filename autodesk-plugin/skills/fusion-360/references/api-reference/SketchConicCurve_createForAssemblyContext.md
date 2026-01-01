# SketchConicCurve.createForAssemblyContext Method

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a [SketchConicCurve](SketchConicCurve.htm) object.```` ``` returnValue = sketchConicCurve_var.createForAssemblyContext(occurrence) ``` ```` |

"sketchConicCurve\_var" is a variable referencing a [SketchConicCurve](SketchConicCurve.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchConicCurve](SketchConicCurve.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |