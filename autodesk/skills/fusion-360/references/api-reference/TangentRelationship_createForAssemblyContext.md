# TangentRelationship.createForAssemblyContext Method

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a [TangentRelationship](TangentRelationship.htm) object.```` ``` returnValue = tangentRelationship_var.createForAssemblyContext(occurrence) ``` ```` |

"tangentRelationship\_var" is a variable referencing a [TangentRelationship](TangentRelationship.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TangentRelationship](TangentRelationship.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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