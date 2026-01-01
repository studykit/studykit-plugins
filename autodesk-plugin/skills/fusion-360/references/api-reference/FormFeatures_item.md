# FormFeatures.item Method

Parent Object: [FormFeatures](FormFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeatures.h>

## Description

Function that returns the specified Form feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeatures\_var" is a variable referencing a [FormFeatures](FormFeatures.htm) object.```` ``` returnValue = formFeatures_var.item(index) ``` ```` |

"formFeatures\_var" is a variable referencing a [FormFeatures](FormFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FormFeature](FormFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |