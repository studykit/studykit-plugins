# FlangeFeatures.itemByName Method

Parent Object: [FlangeFeatures](FlangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeatures.h>

## Description

Function that returns the specified flange feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeatures\_var" is a variable referencing a [FlangeFeatures](FlangeFeatures.htm) object.```` ``` returnValue = flangeFeatures_var.itemByName(name) ``` ```` |

"flangeFeatures\_var" is a variable referencing a [FlangeFeatures](FlangeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FlangeFeature](FlangeFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |