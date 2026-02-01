# MoveFeatureTranslateXYZDefinition.yDistance Property

Parent Object: [MoveFeatureTranslateXYZDefinition](MoveFeatureTranslateXYZDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureTranslateXYZDefinition.h>

## Description

Gets the model parameter that controls the Y distance of the translation. You can use properties on the returned ModelParameter object to edit the offset distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureTranslateXYZDefinition\_var" is a variable referencing a MoveFeatureTranslateXYZDefinition object. |

"moveFeatureTranslateXYZDefinition\_var" is a variable referencing a MoveFeatureTranslateXYZDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureTranslateXYZDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = moveFeatureTranslateXYZDefinition_var->yDistance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |