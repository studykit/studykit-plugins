# CutPasteBodies.itemByName Method

Parent Object: [CutPasteBodies](CutPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBodies.h>

## Description

Function that returns the specified Cut/Paste Body feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object.```` ``` returnValue = cutPasteBodies_var.itemByName(name) ``` ```` |

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CutPasteBody](CutPasteBody.htm) | Returns the specified item or null if the specified name was not found. |

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