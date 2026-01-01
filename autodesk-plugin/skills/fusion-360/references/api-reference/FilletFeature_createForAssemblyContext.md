# FilletFeature.createForAssemblyContext Method

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a [FilletFeature](FilletFeature.htm) object.```` ``` returnValue = filletFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"filletFeature\_var" is a variable referencing a [FilletFeature](FilletFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FilletFeature](FilletFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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