# RemoveFeature.createForAssemblyContext Method

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a [RemoveFeature](RemoveFeature.htm) object.```` ``` returnValue = removeFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"removeFeature\_var" is a variable referencing a [RemoveFeature](RemoveFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RemoveFeature](RemoveFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |