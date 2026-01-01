# UnfoldFeatures.itemByName Method

Parent Object: [UnfoldFeatures](UnfoldFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeatures.h>

## Description

Function that returns the specified unfold feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeatures\_var" is a variable referencing a [UnfoldFeatures](UnfoldFeatures.htm) object.```` ``` returnValue = unfoldFeatures_var.itemByName(name) ``` ```` |

"unfoldFeatures\_var" is a variable referencing a [UnfoldFeatures](UnfoldFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UnfoldFeature](UnfoldFeature.htm) | Returns the specified item or null if the specified name was not found. |

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