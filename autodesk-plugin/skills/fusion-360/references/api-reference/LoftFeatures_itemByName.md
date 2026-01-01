# LoftFeatures.itemByName Method

Parent Object: [LoftFeatures](LoftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatures.h>

## Description

Function that returns the specified loft feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object.```` ``` returnValue = loftFeatures_var.itemByName(name) ``` ```` |

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftFeature](LoftFeature.htm) | Returns the specified item or null if the specified name was not found. |

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