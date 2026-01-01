# ProfileLoop.createForAssemblyContext Method

Parent Object: [ProfileLoop](ProfileLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoop\_var" is a variable referencing a [ProfileLoop](ProfileLoop.htm) object.```` ``` returnValue = profileLoop_var.createForAssemblyContext(occurrence) ``` ```` |

"profileLoop\_var" is a variable referencing a [ProfileLoop](ProfileLoop.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ProfileLoop](ProfileLoop.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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