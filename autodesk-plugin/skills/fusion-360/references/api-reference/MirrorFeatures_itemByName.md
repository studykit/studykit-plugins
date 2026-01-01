# MirrorFeatures.itemByName Method

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Function that returns the specified mirror feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object.```` ``` returnValue = mirrorFeatures_var.itemByName(name) ``` ```` |

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MirrorFeature](MirrorFeature.htm) | Returns the specified item or null if the specified name was not found. |

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