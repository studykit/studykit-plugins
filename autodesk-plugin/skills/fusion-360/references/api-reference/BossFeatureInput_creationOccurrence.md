# BossFeatureInput.creationOccurrence Property

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the boss feature is created based on geometry (e.g. point) in another component AND (the boss) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI A value of null indicates that everything is in the context of a single component. The occurrence provided sets scope for detection of target participant bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. |

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. ```` ``` #include <Fusion/Plastic/BossFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = bossFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = bossFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |