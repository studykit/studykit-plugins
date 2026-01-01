# FormFeatures.itemByName Method

Parent Object: [FormFeatures](FormFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeatures.h>

## Description

Function that returns the specified form feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeatures\_var" is a variable referencing a [FormFeatures](FormFeatures.htm) object.```` ``` returnValue = formFeatures_var.itemByName(name) ``` ```` |

"formFeatures\_var" is a variable referencing a [FormFeatures](FormFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FormFeature](FormFeature.htm) | Returns the specified item or null if the specified name was not found. |

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