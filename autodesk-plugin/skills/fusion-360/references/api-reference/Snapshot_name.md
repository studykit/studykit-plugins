# Snapshot.name Property

Parent Object: [Snapshot](Snapshot.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshot.h>

## Description

Gets and sets the name of the snapshot as seen in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshot\_var" is a variable referencing a Snapshot object. |

"snapshot\_var" is a variable referencing a Snapshot object. ```` ``` #include <Fusion/Fusion/Snapshot.h>  // Get the value of the property. string propertyValue = snapshot_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = snapshot_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |