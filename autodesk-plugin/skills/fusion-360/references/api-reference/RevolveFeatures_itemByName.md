# RevolveFeatures.itemByName Method

Parent Object: [RevolveFeatures](RevolveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

Function that returns the specified revolve feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object.```` ``` returnValue = revolveFeatures_var.itemByName(name) ``` ```` |

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RevolveFeature](RevolveFeature.htm) | Returns the specified item or null if the specified name was not found. |

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