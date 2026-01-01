# ArrangeFeatures.itemByName Method

Parent Object: [ArrangeFeatures](ArrangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatures.h>

## Description

Returns the specified Arrange feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object.```` ``` returnValue = arrangeFeatures_var.itemByName(name) ``` ```` |

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeFeature](ArrangeFeature.htm) | Returns the specified Arrange feature, if it exists. Otherwise it returns null. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the Arrange feature as seen in the timeline. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |