# RuledSurfaceFeature.createForAssemblyContext Method

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a [RuledSurfaceFeature](RuledSurfaceFeature.htm) object.```` ``` returnValue = ruledSurfaceFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"ruledSurfaceFeature\_var" is a variable referencing a [RuledSurfaceFeature](RuledSurfaceFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuledSurfaceFeature](RuledSurfaceFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |