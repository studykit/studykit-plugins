# UnstitchFeature.createForAssemblyContext Method

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a [UnstitchFeature](UnstitchFeature.htm) object.```` ``` returnValue = unstitchFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"unstitchFeature\_var" is a variable referencing a [UnstitchFeature](UnstitchFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnstitchFeature](UnstitchFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |