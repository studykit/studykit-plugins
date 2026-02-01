# PathEntity.createForAssemblyContext Method

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a [PathEntity](PathEntity.htm) object.```` ``` returnValue = pathEntity_var.createForAssemblyContext(occurrence) ``` ```` |

"pathEntity\_var" is a variable referencing a [PathEntity](PathEntity.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathEntity](PathEntity.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) |  |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |