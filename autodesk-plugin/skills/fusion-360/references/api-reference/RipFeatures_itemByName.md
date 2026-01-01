# RipFeatures.itemByName Method

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Function that returns the specified Rip feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object.```` ``` returnValue = ripFeatures_var.itemByName(name) ``` ```` |

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RipFeature](RipFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |