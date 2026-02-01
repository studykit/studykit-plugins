# ArrangeFeature.createForAssemblyContext Method

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an [ArrangeFeature](ArrangeFeature.htm) object.```` ``` returnValue = arrangeFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"arrangeFeature\_var" is a variable referencing an [ArrangeFeature](ArrangeFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeFeature](ArrangeFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |