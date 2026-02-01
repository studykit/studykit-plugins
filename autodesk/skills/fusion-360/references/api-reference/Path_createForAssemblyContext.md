# Path.createForAssemblyContext Method

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"path\_var" is a variable referencing a [Path](Path.htm) object.```` ``` returnValue = path_var.createForAssemblyContext(occurrence) ``` ```` |

"path\_var" is a variable referencing a [Path](Path.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Path](Path.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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