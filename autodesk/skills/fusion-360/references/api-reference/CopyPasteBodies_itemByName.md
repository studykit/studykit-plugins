# CopyPasteBodies.itemByName Method

Parent Object: [CopyPasteBodies](CopyPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBodies.h>

## Description

Function that returns the specified Copy/Paste Body feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object.```` ``` returnValue = copyPasteBodies_var.itemByName(name) ``` ```` |

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CopyPasteBody](CopyPasteBody.htm) | Returns the specified item or null if the specified name was not found. |

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