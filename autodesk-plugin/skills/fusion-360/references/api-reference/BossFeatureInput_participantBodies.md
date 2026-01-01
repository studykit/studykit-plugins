# BossFeatureInput.participantBodies Property

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

Gets and sets the list of bodies that will participate in the boss feature. If body provided does not intersect with direction vector at proposed position points it will be ignored. If more bodies intersect at given position point only the closest body will be accepted. Boss feature works with solid bodies only. If this property has not been set (or is empty) closest visible bodies will be detected automatically based on proposed positions and orientation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. |

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. ```` ``` #include <Fusion/Plastic/BossFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = bossFeatureInput_var->participantBodies();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = bossFeatureInput_var->participantBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |