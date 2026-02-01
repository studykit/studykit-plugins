# MoveFeature.definition Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Returns the MoveFeatureDefinition object which provides access to the information that specifies how this MoveFeature is defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object. |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. Ptr<MoveFeatureDefinition> propertyValue = moveFeature_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is a [MoveFeatureDefinition](MoveFeatureDefinition.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |