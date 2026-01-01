# Snapshots.revertPendingSnapshot Method

Parent Object: [Snapshots](Snapshots.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshots.h>

## Description

Reverts and changes that have been made that can be snapshot. This effectively reverts the design back to the last snapshot. This is only valid when the HasPendingSnapshot property returns true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshots\_var" is a variable referencing a [Snapshots](Snapshots.htm) object.```` ``` returnValue = snapshots_var.revertPendingSnapshot() ``` ```` |

"snapshots\_var" is a variable referencing a [Snapshots](Snapshots.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the revert was successful. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |