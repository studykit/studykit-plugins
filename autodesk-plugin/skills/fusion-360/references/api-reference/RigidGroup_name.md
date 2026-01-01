# RigidGroup.name Property

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Gets and sets the name of the rigid group as seen in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a RigidGroup object. |

"rigidGroup\_var" is a variable referencing a RigidGroup object. ```` ``` #include <Fusion/Components/RigidGroup.h>  // Get the value of the property. string propertyValue = rigidGroup_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = rigidGroup_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |