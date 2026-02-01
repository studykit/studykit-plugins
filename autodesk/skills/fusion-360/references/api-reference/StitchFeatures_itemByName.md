# StitchFeatures.itemByName Method

Parent Object: [StitchFeatures](StitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

Function that returns the specified stitch feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object.```` ``` returnValue = stitchFeatures_var.itemByName(name) ``` ```` |

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StitchFeature](StitchFeature.htm) | Returns the specified item or null if the specified name was not found. |

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