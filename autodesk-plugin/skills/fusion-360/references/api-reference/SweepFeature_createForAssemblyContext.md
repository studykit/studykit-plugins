# SweepFeature.createForAssemblyContext Method

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a [SweepFeature](SweepFeature.htm) object.```` ``` returnValue = sweepFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"sweepFeature\_var" is a variable referencing a [SweepFeature](SweepFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SweepFeature](SweepFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |