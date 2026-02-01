# ExtrudeFeature.createForAssemblyContext Method

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.```` ``` returnValue = extrudeFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtrudeFeature](ExtrudeFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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