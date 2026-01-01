# RevolveFeature.createForAssemblyContext Method

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.```` ``` returnValue = revolveFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RevolveFeature](RevolveFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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