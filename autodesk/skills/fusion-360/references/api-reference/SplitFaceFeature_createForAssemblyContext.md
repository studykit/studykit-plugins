# SplitFaceFeature.createForAssemblyContext Method

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.```` ``` returnValue = splitFaceFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitFaceFeature](SplitFaceFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

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