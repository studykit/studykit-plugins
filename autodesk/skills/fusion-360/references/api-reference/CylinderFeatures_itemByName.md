# CylinderFeatures.itemByName Method

Parent Object: [CylinderFeatures](CylinderFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeatures.h>

## Description

Function that returns the specified cylinder feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeatures\_var" is a variable referencing a [CylinderFeatures](CylinderFeatures.htm) object.```` ``` returnValue = cylinderFeatures_var.itemByName(name) ``` ```` |

"cylinderFeatures\_var" is a variable referencing a [CylinderFeatures](CylinderFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CylinderFeature](CylinderFeature.htm) | Returns the specified item or null if the specified name was not found. |

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