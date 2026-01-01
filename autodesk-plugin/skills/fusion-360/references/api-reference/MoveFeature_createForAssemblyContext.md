# MoveFeature.createForAssemblyContext Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeature](MoveFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |