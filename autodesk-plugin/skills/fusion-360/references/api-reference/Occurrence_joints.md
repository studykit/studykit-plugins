# Occurrence.joints Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the joints that affect the position of this occurrence. For example, if a joint has been created between this occurrence and another occurrence, this property will return that joint. If the occurrence is a proxy, the joints returned will also be proxies in the same context as the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<JointList> propertyValue = occurrence_var->joints(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointList](JointList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |