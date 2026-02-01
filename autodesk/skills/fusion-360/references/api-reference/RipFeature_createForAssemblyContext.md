# RipFeature.createForAssemblyContext Method

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object.```` ``` returnValue = ripFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RipFeature](RipFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |