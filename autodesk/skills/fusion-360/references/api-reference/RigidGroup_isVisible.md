# RigidGroup.isVisible Property

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Gets and sets whether the occurrences that are part of this rigid group are visible or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a RigidGroup object. |

"rigidGroup\_var" is a variable referencing a RigidGroup object. ```` ``` #include <Fusion/Components/RigidGroup.h>  // Get the value of the property. boolean propertyValue = rigidGroup_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = rigidGroup_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |