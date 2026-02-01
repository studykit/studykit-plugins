# PathPatternFeature.createForAssemblyContext Method

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a [PathPatternFeature](PathPatternFeature.htm) object.```` ``` returnValue = pathPatternFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"pathPatternFeature\_var" is a variable referencing a [PathPatternFeature](PathPatternFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathPatternFeature](PathPatternFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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