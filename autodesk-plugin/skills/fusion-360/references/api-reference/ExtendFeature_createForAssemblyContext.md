# ExtendFeature.createForAssemblyContext Method

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an [ExtendFeature](ExtendFeature.htm) object.```` ``` returnValue = extendFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"extendFeature\_var" is a variable referencing an [ExtendFeature](ExtendFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtendFeature](ExtendFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

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