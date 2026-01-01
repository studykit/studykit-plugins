# Setup.additiveContainerByType Method

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Returns the additive container with the specified type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a [Setup](Setup.htm) object.```` ``` returnValue = setup_var.additiveContainerByType(containerType) ``` ```` |

"setup\_var" is a variable referencing a [Setup](Setup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMAdditiveContainer](CAMAdditiveContainer.htm) | Returns the specified container or null in the case where there is no container with the specified type. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| containerType | [CAMAdditiveContainerTypes](CAMAdditiveContainerTypes.htm) | The type of the container |

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |