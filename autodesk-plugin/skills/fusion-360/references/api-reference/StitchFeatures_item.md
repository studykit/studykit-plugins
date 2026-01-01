# StitchFeatures.item Method

Parent Object: [StitchFeatures](StitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

Function that returns the specified stitch feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object.```` ``` returnValue = stitchFeatures_var.item(index) ``` ```` |

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StitchFeature](StitchFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |