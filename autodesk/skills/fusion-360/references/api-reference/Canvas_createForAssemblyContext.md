# Canvas.createForAssemblyContext Method

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a [Canvas](Canvas.htm) object.```` ``` returnValue = canvas_var.createForAssemblyContext(occurrence) ``` ```` |

"canvas\_var" is a variable referencing a [Canvas](Canvas.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Canvas](Canvas.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |