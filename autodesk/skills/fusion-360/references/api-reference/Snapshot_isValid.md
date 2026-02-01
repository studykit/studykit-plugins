# Snapshot.isValid Property

Parent Object: [Snapshot](Snapshot.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshot.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshot\_var" is a variable referencing a Snapshot object. |

"snapshot\_var" is a variable referencing a Snapshot object. ```` ``` #include <Fusion/Fusion/Snapshot.h>  // Get the value of the property. boolean propertyValue = snapshot_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |