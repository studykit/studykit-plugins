# SphereFeatures.itemByName Method

Parent Object: [SphereFeatures](SphereFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeatures.h>

## Description

Function that returns the specified sphere feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeatures\_var" is a variable referencing a [SphereFeatures](SphereFeatures.htm) object.```` ``` returnValue = sphereFeatures_var.itemByName(name) ``` ```` |

"sphereFeatures\_var" is a variable referencing a [SphereFeatures](SphereFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SphereFeature](SphereFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |