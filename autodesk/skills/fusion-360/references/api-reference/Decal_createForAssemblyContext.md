# Decal.createForAssemblyContext Method

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a [Decal](Decal.htm) object.```` ``` returnValue = decal_var.createForAssemblyContext(occurrence) ``` ```` |

"decal\_var" is a variable referencing a [Decal](Decal.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Decal](Decal.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |