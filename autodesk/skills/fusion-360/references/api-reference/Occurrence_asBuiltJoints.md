# Occurrence.asBuiltJoints Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the as-built joints that affect the position of this occurrence. If the occurrence is a proxy, the as-built joints returned will also be proxies in the same context as the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<AsBuiltJointList> propertyValue = occurrence_var->asBuiltJoints(); ``` ```` |

## Property Value

This is a read only property whose value is an [AsBuiltJointList](AsBuiltJointList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |