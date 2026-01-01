# RibFeatures.itemByName Method

Parent Object: [RibFeatures](RibFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeatures.h>

## Description

Function that returns the specified Rib feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeatures\_var" is a variable referencing a [RibFeatures](RibFeatures.htm) object.```` ``` returnValue = ribFeatures_var.itemByName(name) ``` ```` |

"ribFeatures\_var" is a variable referencing a [RibFeatures](RibFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RibFeature](RibFeature.htm) | Returns the specified item or null if the specified name was not found. |

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