# ThickenFeature.createForAssemblyContext Method

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a [ThickenFeature](ThickenFeature.htm) object.```` ``` returnValue = thickenFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"thickenFeature\_var" is a variable referencing a [ThickenFeature](ThickenFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThickenFeature](ThickenFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |