# OffsetFacesFeatures.itemByName Method

Parent Object: [OffsetFacesFeatures](OffsetFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeatures.h>

## Description

Function that returns the specified Offset Face feature using the name of the feature. Offset Face features are created in the UI using the "Press Pull" command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeatures\_var" is a variable referencing an [OffsetFacesFeatures](OffsetFacesFeatures.htm) object.```` ``` returnValue = offsetFacesFeatures_var.itemByName(name) ``` ```` |

"offsetFacesFeatures\_var" is a variable referencing an [OffsetFacesFeatures](OffsetFacesFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFacesFeature](OffsetFacesFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |