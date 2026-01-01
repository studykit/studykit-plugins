# TimelineGroup.deleteMe Method

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Deletes the group with the option of deleting or keeping the contents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.```` ``` returnValue = timelineGroup_var.deleteMe(deleteGroupAndContents) ``` ```` |

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| deleteGroupAndContents | boolean | Indicates if the group and its contents should be deleted or if only the group should be deleted and the contents kept and expanded. A value of true will delete the group and its contents. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |