# ExtrudeFeatures.itemByName Method

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Function that returns the specified extrude feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object.```` ``` returnValue = extrudeFeatures_var.itemByName(name) ``` ```` |

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtrudeFeature](ExtrudeFeature.htm) | Returns the specified item or null if the specified name was not found. |

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