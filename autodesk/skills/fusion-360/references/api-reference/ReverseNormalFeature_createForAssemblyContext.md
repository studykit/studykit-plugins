# ReverseNormalFeature.createForAssemblyContext Method

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a [ReverseNormalFeature](ReverseNormalFeature.htm) object.```` ``` returnValue = reverseNormalFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"reverseNormalFeature\_var" is a variable referencing a [ReverseNormalFeature](ReverseNormalFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReverseNormalFeature](ReverseNormalFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |