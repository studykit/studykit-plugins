# RigidGroup.parentComponent Property

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Returns the parent component that owns this rigid group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a RigidGroup object. |

"rigidGroup\_var" is a variable referencing a RigidGroup object. ```` ``` #include <Fusion/Components/RigidGroup.h>  // Get the value of the property. Ptr<Component> propertyValue = rigidGroup_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |