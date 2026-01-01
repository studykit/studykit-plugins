# MoveFeatureTranslateAlongEntityDefinition.distance Property

Parent Object: [MoveFeatureTranslateAlongEntityDefinition](MoveFeatureTranslateAlongEntityDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureTranslateAlongEntityDefinition.h>

## Description

Gets the model parameter that controls the offset distance. You can use properties on the returned ModelParameter object to edit the offset distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureTranslateAlongEntityDefinition\_var" is a variable referencing a MoveFeatureTranslateAlongEntityDefinition object. |

"moveFeatureTranslateAlongEntityDefinition\_var" is a variable referencing a MoveFeatureTranslateAlongEntityDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureTranslateAlongEntityDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = moveFeatureTranslateAlongEntityDefinition_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |