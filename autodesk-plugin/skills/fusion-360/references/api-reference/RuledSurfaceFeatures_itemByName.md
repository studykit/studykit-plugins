# RuledSurfaceFeatures.itemByName Method

Parent Object: [RuledSurfaceFeatures](RuledSurfaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

Function that returns the specified RuledSurface feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object.```` ``` returnValue = ruledSurfaceFeatures_var.itemByName(name) ``` ```` |

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuledSurfaceFeature](RuledSurfaceFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |