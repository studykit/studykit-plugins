# FeatureList.item Method

Parent Object: [FeatureList](FeatureList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FeatureList.h>

## Description

Returns the specified folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"featureList\_var" is a variable referencing a [FeatureList](FeatureList.htm) object.```` ``` returnValue = featureList_var.item(index) ``` ```` |

"featureList\_var" is a variable referencing a [FeatureList](FeatureList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Feature](Feature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the feature to return. The first feature in the list has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |