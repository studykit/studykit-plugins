# Occurrence.rigidGroups Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the rigid groups that this occurrence is a member of. If the occurrence is a proxy, the joints returned will also be proxies in the same context as the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<RigidGroupList> propertyValue = occurrence_var->rigidGroups(); ``` ```` |

## Property Value

This is a read only property whose value is a [RigidGroupList](RigidGroupList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |